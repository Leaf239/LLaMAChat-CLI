import os
import subprocess
import sys
import requests
from pathlib import Path
from tqdm import tqdm

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download_model():
    model_url = "https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf"
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    model_path = models_dir / "Llama-3.2-3B-Instruct-Q4_K_M.gguf"

    if model_path.exists():
        print("✅ Model already exists. Skipping download.")
        return

    print("⬇️ Downloading the model (~2GB). This may take a while...")

    with requests.get(model_url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get("content-length", 0))
        block_size = 8192
        with open(model_path, "wb") as f, tqdm(
            total=total_size, unit='B', unit_scale=True, desc="📥 Downloading", ncols=70
        ) as bar:
            for chunk in r.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))

    print("✅ Model download completed.")

if __name__ == "__main__":
    print("🔧 Installing Python dependencies...")
    install_requirements()

    print("📦 Checking and downloading model...")
    download_model()

    print("🚀 Setup complete. You can now run `python main.py` to start chatting.")
