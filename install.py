import os
import subprocess
import sys
import requests
from pathlib import Path

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download_model():
    model_url = "https://huggingface.co/TheBloke/Llama-3.2-3B-Instruct-GGUF/resolve/main/llama-3.2-3b-instruct.Q4_K_M.gguf"
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    model_path = models_dir / "Llama-3.2-3B-Instruct-Q4_K_M.gguf"

    if model_path.exists():
        print("✅ Model already exists, skipping download.")
        return

    print("⬇️ Downloading GGUF model (this may take a while)...")
    with requests.get(model_url, stream=True) as r:
        r.raise_for_status()
        with open(model_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print("✅ Model download complete!")

if __name__ == "__main__":
    print("🔧 Installing dependencies...")
    install_requirements()

    print("📦 Downloading model...")
    download_model()

    print("🚀 Setup complete!")
