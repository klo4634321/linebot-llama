import asyncio
import edge_tts
import playsound  # 如果 playsound 有問題，請改用 pydub 來播放音檔

async def text_to_speech(text):
    """使用 edge-tts 生成語音"""
    tts = edge_tts.Communicate(text, "zh-TW-YunJheNeural")  # 選擇台灣男聲
    output_file = "output.mp3"
    await tts.save(output_file)  # 儲存語音檔
    print("語音合成完成，播放中...")
    playsound.playsound(output_file)  # 播放語音

async def main():
    text = "你好，我是你的 AI VTuber！"
    await text_to_speech(text)

asyncio.run(main())
