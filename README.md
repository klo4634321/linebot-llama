# LLaMA LINE Bot

這個專案展示如何將 **LLaMA** 模型與 **LINE Bot** 結合，並使用 `Flask` 框架來處理 LINE Bot 的 webhook。當用戶發送訊息給 LINE Bot 時，Bot 將訊息傳送給本地的 LLaMA 模型，並將 LLaMA 回應回傳給用戶。

## 如何使用

1. **確保以下設置都正確**:  
   a. **linebot.py - CHANNEL_ACCESS_TOKEN、CHANNEL_SECRET**  
     前往 LINE Developers 官方網站: [LINE Developers](https://developers.line.biz/console/channel/2006942829/messaging-api?status=success)  
     進入 **Messaging API** 頁面，選擇你要操作的 Channel。  
     在該頁面中，你會看到 `Channel access token` 和 `Channel secret`。  
     將 `CHANNEL_ACCESS_TOKEN`、`CHANNEL_SECRET` 複製到 `config.txt` 中。  
     
   b. **ngrok 開啟**  
     前往 ngrok 官網: [ngrok Dashboard](https://dashboard.ngrok.com/agents)  
     確認 ngrok 服務開啟中。  

2. **如何執行**:  
   a. **執行 ngrok**  
     進入 `ngrok-v3-stable-windows-amd64` 目錄，執行 `ngrok.exe`，並輸入以下命令：  
     ```bash
     ngrok http 5000
     ```  
     
   b. **執行 llama.py**  
     執行以下命令啟動 LLaMA 模型：  
     ```bash
     python llama.py
     ```  
     註：LLaMA 會佔用端口 `8000` 並與 LINE Bot 連線。  
     
   c. **執行 linebot.py**  
     執行以下命令啟動 LINE Bot：  
     ```bash
     python linebot.py
     ```  
     註：LINE Bot 會佔用端口 `5000` 與 ngrok 連線，並佔用端口 `8000` 與 LLaMA 連線。  

3. **LINE 訊息傳送**:  
   在 LINE 聊天對話中選擇你的聊天機器人，並傳送文字訊息。LINE Bot 會將訊息發送給 LLaMA 模型，並返回 LLaMA 的回應。


## 使用到的技能與技術

1. **Flask**  
   使用 Flask 作為 Web 框架，來處理 LINE Bot 的 webhook 請求，並管理伺服器端的邏輯。

2. **LINE Messaging API**  
   利用 LINE Messaging API 建立並管理 LINE Bot，實現消息的接收與回應。需要使用 LINE Developers 進行 Token 設定與 webhook 配置。

3. **LLaMA 模型**  
   使用 LLaMA (Meta-LLaMA) 進行文本生成，並將其整合進 LINE Bot 中，以便於用戶發送的訊息能夠經過 LLaMA 模型進行處理並返回回應。

4. **ngrok**  
   使用 ngrok 將本地伺服器暴露至公共網路，使得 LINE 的 webhook 請求能夠成功轉發到本地運行的 Flask 伺服器。
