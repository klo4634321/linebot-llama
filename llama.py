from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

model_name = "meta-llama/Meta-Llama-3-8B"  # 請確認你使用的模型名稱

device = "cuda" if torch.cuda.is_available() else "cpu"

# 4-bit 量化配置
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

# 載入模型
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    device_map="auto",
    offload_folder="offload"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

print("Model loaded successfully!")
# 互動式聊天
print("開始聊天吧！輸入 'exit' 來結束對話。")
while True:
    user_input = input("你: ")
    if user_input.lower() in ["exit", "quit", "q"]:
        print("聊天結束，再見！")
        break

    # 編碼輸入
    inputs = tokenizer(user_input, return_tensors="pt").to(device)

    # 產生回應
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=100)

    # 解碼輸出
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("LLaMA:", response)
