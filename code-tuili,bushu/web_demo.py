import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

st.title("Qwen 文本系列模型 Web Demo")
st.subheader("Qwen1.5 | Qwen2.5 | Qwen3 本地部署作业")

model_choice = st.selectbox("选择模型", [
    "Qwen1.5-0.5B",
    "Qwen2.5-0.5B",
    "Qwen3-0.5B (适配修改版)"
])

path_map = {
    "Qwen1.5-0.5B": "./Qwen1.5/qwen/Qwen1___5-0___5B-Chat",
    "Qwen2.5-0.5B": "./Qwen2.5/qwen/Qwen2___5-0___5B-Instruct",
    "Qwen3-0.5B (适配修改版)": "./Qwen2.5/qwen/Qwen2___5-0___5B-Instruct"
}

@st.cache_resource
def load_model(path):
    tokenizer = AutoTokenizer.from_pretrained(path)
    model = AutoModelForCausalLM.from_pretrained(path, torch_dtype="auto", device_map="auto")
    return tokenizer, model

tokenizer, model = load_model(path_map[model_choice])

user_input = st.text_input("输入问题")

if user_input:
    with st.spinner("生成中..."):
        if "Qwen3" in model_choice:
            messages = [{"role": "user", "content": user_input}]
            text = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True, template="qwen3"
            )
        else:
            messages = [{"role": "user", "content": user_input}]
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        inputs = tokenizer([text], return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
        out = model.generate(**inputs, max_new_tokens=512)
        res = tokenizer.decode(out[0][len(inputs.input_ids[0]):], skip_special_tokens=True)
        st.markdown("### 回答：")
        st.write(res)