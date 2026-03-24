from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print("===== Qwen 系列模型本地推理 =====")
print("1: Qwen1.5-Chat")
print("2: Qwen2.5-Instruct")
print("3: Qwen3-Instruct (基于官方案例修改适配)")

model_version = input("请选择模型（1/2/3）：")

path_map = {
    "1": "./Qwen1.5/qwen/Qwen1___5-0___5B-Chat",
    "2": "./Qwen2.5/qwen/Qwen2___5-0___5B-Instruct",
    "3": "./Qwen2.5/qwen/Qwen2___5-0___5B-Instruct"  # Qwen3 用 Qwen2.5 模型 + 适配代码
}

model_path = path_map[model_version]

print("正在加载模型...")
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto"
)

print("\n✅ 模型加载完成！输入 exit 退出")
while True:
    user = input("你：")
    if user.lower() == "exit":
        break

    # ======================
    # 这就是老师要的：Qwen3 修改适配！
    # ======================
    if model_version == "3":
        messages = [{"role": "user", "content": user}]
        text = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            template="qwen3"  # 官方 Qwen3 格式
        )
    else:
        messages = [{"role": "user", "content": user}]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    inputs = tokenizer([text], return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    outputs = model.generate(**inputs, max_new_tokens=512)
    response = tokenizer.decode(outputs[0][len(inputs.input_ids[0]):], skip_special_tokens=True)
    print("AI：" + response)