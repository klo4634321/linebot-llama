from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

app = Flask(__name__)

# LLaMA 3 設定
model_name = "meta-llama/Meta-Llama-3-8B"  # 或你的本地模型路徑
device = "cuda" if torch.cuda.is_available() else "cpu"

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

# 載入 LLaMA 3
print("Loading LLaMA 3 model...")
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto",
    offload_folder="offload"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
print("Model loaded successfully!")


# 建立 API 來接收請求
@app.route("/generate", methods=["POST"])
def generate_response():
    data = request.json
    user_input = data.get("text", "")

    if not user_input:
        return jsonify({"error": "No input text provided"}), 400

    # 產生回應
    inputs = tokenizer(user_input, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=100, pad_token_id=tokenizer.eos_token_id)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # 移除輸入部分，避免輸出包含原始輸入
    response = response[len(user_input):].strip()

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(port=8000)  # LLaMA 3 API 會在 http://localhost:8000 運行
