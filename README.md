# 🦙 LLaMA 3.2 3B CLI Chat

This is a simple streaming chat interface using LLaMA 3.2 3B (GGUF) in the terminal.

## 🚀 Features

- Prompt history with role separation
- Streaming token-wise output
- Easy configuration

## 🛠 Installation

1. Clone this repository.
2. Download the GGUF model from here: [LLaMA 3.2 3B Instruct Q4_K_M](https://huggingface.co/TheBloke/Llama-3.2-3B-Instruct-GGUF)
3. Place the model in `./models` folder.
4. Run the installer:

```bash
python install.py
```

5. Launch the chat:

```bash
python main.py
```

## 🧠 Model info

- Model: LLaMA 3.2 3B Instruct
- Format: GGUF (Quantized: Q4_K_M)
- Context length: 4096 tokens
- Backend: llama-cpp-python

## 📂 File Structure

```
llama_chat_cli/
├── llama_chat/
│   ├── __init__.py
│   ├── config.py
│   ├── llm_engine.py
│   └── prompt_builder.py
├── main.py
├── install.py
├── requirements.txt
└── README.md
```

## 🏁 Exit

Type `/exit` anytime to stop the chat.
