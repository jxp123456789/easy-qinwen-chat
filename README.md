# easy-qinwen-chat
# Qwen 文本系列模型本地部署、推理与 Web Demo
基于 Qwen1.5、Qwen2.5、Qwen3 系列大模型实现本地部署、命令行推理、可视化 Web 演示，支持一键运行，适合学习与快速部署轻量级大模型。

## 项目介绍
本项目实现 **Qwen 全系列文本模型** 的本地化运行，包含：
- Qwen1.5 本地部署与推理
- Qwen2.5 本地部署与推理
- Qwen3 基于官方案例适配修改
- 统一命令行交互入口
- 可视化 Web Demo 界面
- 支持 CPU / GPU 自动运行

无需复杂配置，下载模型 → 安装依赖 → 直接运行。

## 功能亮点
✅ 支持 Qwen1.5 / Qwen2.5 / Qwen3 多模型切换  
✅ 本地离线推理，无需联网调用 API  
✅ 命令行聊天交互  
✅ Web 可视化界面（Streamlit）  
✅ 轻量化、低资源占用、可直接学习使用  
✅ 完整项目结构，易读易改  

## 项目结构
easy-qinwen-chat/├── Qwen1.5/ # Qwen1.5 模型目录├── Qwen2.5/ # Qwen2.5 模型目录├── code-tuili,bushu/ # 核心代码│ ├── download_models.py # 模型下载│ ├── cli_chat.py # 命令行推理│ └── web_demo.py # Web 演示界面├── requirements.txt # 依赖包└── README.md
plaintext

## 快速开始
### 1. 安装环境
```bash
pip install -r requirements.txt
2. 下载模型
bash
运行
python download_models.py
3. 命令行聊天
bash
运行
python cli_chat.py
4. 启动 Web Demo
bash
运行
streamlit run web_demo.py
访问地址：http://localhost:8501
技术栈
Python
PyTorch
Transformers
Streamlit
ModelScope
适用人群
大模型初学者
希望本地部署轻量级大模型的开发者
需要快速实现聊天界面的学生 / 开发者
学习模型部署、推理、Web Demo 实践
作业说明（如为课程项目）
本项目完成：
Qwen1.5、Qwen2.5、Qwen3 本地部署
推理脚本实现
Web Demo 开发与适配
项目打包上传 GitHub
项目地址
GitHub：https://github.com/jxp123456789/easy-qinwen-chat
License
本项目仅用于学习与非商业使用。