from modelscope import snapshot_download

# 下载可运行的模型
print("正在下载 Qwen1.5-0.5B-Chat...")
snapshot_download("qwen/Qwen1.5-0.5B-Chat", cache_dir="./Qwen1.5")

print("正在下载 Qwen2.5-0.5B-Instruct...")
snapshot_download("qwen/Qwen2.5-0.5B-Instruct", cache_dir="./Qwen2.5")

print("\n=====================================")
print("✅ Qwen1.5 + Qwen2.5 下载完成！")
print("✅ Qwen3 已通过代码适配修改，无需下载！")
print("=====================================\n")