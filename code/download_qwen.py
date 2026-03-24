from modelscope import snapshot_download

# 自动下载 0.5B 小模型，存到当前文件夹
model_dir = snapshot_download(
    "qwen/Qwen2.5-0.5B-Instruct",
    cache_dir="../Qwen2.5-0.5B-Instruct"
)
print("模型下载完成！路径：", model_dir)
