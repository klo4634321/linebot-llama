import requests
from flask import Flask, request, abort
import json
app = Flask(__name__)

# 在此替換為您的 Channel Access Token 和 Channel Secret
CHANNEL_ACCESS_TOKEN = 'MFT+qmC8b+wXdDxEwDhoowlIYHywzeHokFSkdDAnRO8QgmbaQGOsQySyll9eGmfkEONFSI3JInzS6BvXxEJ1NcP5g3Zeia0dJK1dC0umekodQIEBVpsL8wWjmCILkSHgYiw7NwtbW1KbTSr6IdiGZwdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = 'd3c994bd28bdd5874b319b79e6e7901c'

@app.route("/webhook", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    # 驗證簽名
    if not is_valid_signature(body, signature):
        abort(400)
    # 處理訊息
    handle_message(body)
    return 'OK'

def is_valid_signature(body, signature):
    # 在此實作簽名驗證邏輯
    # 例如，使用 HMAC-SHA256 進行驗證
    return True

def handle_message(body):
    data = json.loads(body)
    events = data.get("events", [])

    for event in events:
        if event["type"] == "message" and "text" in event["message"]:
            reply_token = event["replyToken"]  # 確保是從事件取得的
            user_message = event["message"]["text"]
            bot_reply = f"你說了: {user_message}"
            reply_message(reply_token, bot_reply)


def reply_message(reply_token, text):
    url = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {CHANNEL_ACCESS_TOKEN}'
    }
    data = {
        'replyToken': reply_token,
        'messages': [{'type': 'text', 'text': text}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f'Error: {response.status_code} - {response.text}')

if __name__ == "__main__":
    app.run(port=5000)
