import os
import subprocess
import sys
import requests
from pathlib import Path

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download_model():
    model_url = "https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF/resolve/main/Llama-3.2-3B-Instruct-Q4_K_M.gguf"
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    model_path = models_dir / "Llama-3.2-3B-Instruct-Q4_K_M.gguf"

    if model_path.exists():
        print("✅ 모델 이미 있음. 다운로드 스킵함.")
        return

    print("⬇️ 모델 다운로드 중... (좀 걸릴 수 있음)")
    with requests.get(model_url, stream=True) as r:
        r.raise_for_status()
        with open(model_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print("✅ 모델 다운로드 완료!")

if __name__ == "__main__":
    print("🔧 의존성 설치 중...")
    install_requirements()

    print("📦 모델 다운로드 중...")
    download_model()

    print("🚀 셋업 완료! 이제 main.py 실행 ㄱㄱ")
