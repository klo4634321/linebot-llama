import requests
from flask import Flask, request, abort
import json
import os

app = Flask(__name__)

def load_config(filename):
    config = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            key, value = line.strip().split("=", 1)  # 確保去除空白
            config[key] = value.strip()  # 確保去除值的空格與換行
    return config

config = load_config("config.txt")


# 取得 Token 和 Secret
CHANNEL_ACCESS_TOKEN = config.get("CHANNEL_ACCESS_TOKEN", "").strip()
CHANNEL_SECRET = config.get("CHANNEL_SECRET", "").strip()

# LLaMA 3 API 服務網址（如果部署到雲端，請改成你的伺服器網址）
LLAMA_API_URL = "http://localhost:8000/generate"

@app.route("/webhook", methods=["POST"])
def callback():
    body = request.get_data(as_text=True)
    data = json.loads(body)

    events = data.get("events", [])
    for event in events:
        if event["type"] == "message" and "text" in event["message"]:
            user_message = event["message"]["text"]
            reply_token = event["replyToken"]

            # 呼叫 LLaMA 3 API 來獲取回應
            llama_reply = get_llama_response(user_message)

            # 回應使用者
            reply_message(reply_token, llama_reply)

    return "OK"

# 呼叫 LLaMA 3 API 取得回應
def get_llama_response(user_input):
    try:
        response = requests.post(LLAMA_API_URL, json={"text": user_input}, timeout=10)
        data = response.json()
        return data.get("response", "抱歉，我無法回答你的問題。")
    except requests.exceptions.RequestException as e:
        print("Error calling LLaMA API:", e)
        return "抱歉，我的 AI 大腦有點當機了 😵"

# 回應使用者的訊息
def reply_message(reply_token, text):
    url = "https://api.line.me/v2/bot/message/reply"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
    }
    data = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text}],
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    app.run(port=5000)
