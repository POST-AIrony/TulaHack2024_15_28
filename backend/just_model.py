from constant import MODEL_PATH
from llama_cpp import Llama
model = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=-1,
    n_batch=512,
    n_ctx=4096,
    n_parts=1,
)