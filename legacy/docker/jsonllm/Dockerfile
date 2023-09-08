# Run from repo root
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY parserllm/parserllm parserllm/
COPY rellm/rellm rellm/

COPY jsonllm/ jsonllm/

ENV PYTHONPATH=/app

# hacky fix for bitsandbytes
# https://github.com/TimDettmers/bitsandbytes/issues/156
RUN cp /opt/conda/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_cuda117.so \
    /opt/conda/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_cpu.so

CMD ["python", "jsonllm/server/server.py"]
