from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 你的模型路径（已经帮你填好）
model_path = "../Qwen2.5-0.5B-Instruct/qwen/Qwen2___5-0___5B-Instruct"

# 加载模型
print("正在加载模型，请稍候...")
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

print("模型加载完成！你可以开始聊天了，输入 exit 退出。\n")

# 无限循环聊天
while True:
    # 你输入问题
    prompt = input("你：")

    # 输入 exit 退出
    if prompt.lower() == "exit":
        print("对话结束！")
        break

    # 构造对话
    messages = [
        {"role": "system", "content": "你是一个有用的助手。"},
        {"role": "user", "content": prompt}
    ]

    # 处理输入
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    # 生成回答
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=1024,
        do_sample=True,
        temperature=0.7
    )

    # 截取回答
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    # 输出
    print("AI：" + response + "\n")