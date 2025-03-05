# LLaMA LINE Bot

這個專案展示如何將 **LLaMA** 模型與 **LINE Bot** 結合，並使用 `Flask` 框架來處理 LINE Bot 的 webhook。當用戶發送訊息給 LINE Bot 時，Bot 將訊息傳送給本地的 LLaMA 模型，並將 LLaMA 回應回傳給用戶。

## 如何使用

1. 確保以下設置都正確 :
   a. linebot.py - CHANNEL_ACCESS_TOKEN、CHANNEL_SECRET.
     前往 LINE Developers 官方網站 : https://developers.line.biz/console/channel/2006942829/messaging-api?status=success
     進入 Messaging API 頁面，選擇你要操作的 Channel。
     在該頁面中，你會看到 Channel access token 和 Channel secret。
     將 CHANNEL_ACCESS_TOKEN、CHANNEL_SECRET 複製到 config.txt 中。
   b. ngrok 開啟:
     前往ngrok官網: https://dashboard.ngrok.com/agents
     確認服務開啟中。
2. 如何執行 :
  a. 執行 ngrok
    進入 ngrok-v3-stable-windows-amd64 執行 ngrok.exe 輸入: ngrok https 5000
  b. 執行 llama.py
    python llama.py
    注: llama 占用 prot 8000 與 linebot 連線
  c. 執行 linebot.py
    python linebot.py
    注: linebot 占用 prot 8000 與 llama 連線 、 占用 port 5000 與 ngrok 連線
3. LINE 訊息傳送 :
   在LINE聊天對話中選中聊天機器人，傳送文字。
