FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN CUDACXX=/usr/local/cuda-12/bin/nvcc CMAKE_ARGS="-DLLAMA_CUBLAS=on -DCMAKE_CUDA_ARCHITECTURES=all-major" FORCE_CMAKE=1 pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]