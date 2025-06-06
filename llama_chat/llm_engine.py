from llama_cpp import Llama
from .config import MODEL_PATH, N_CTX, N_THREADS

llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=N_CTX,
    n_threads=N_THREADS,
    stream=True,
    verbose=False
)
