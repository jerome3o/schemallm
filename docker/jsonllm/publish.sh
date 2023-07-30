sudo docker login
sudo docker build -f docker/jsonllm/Dockerfile -t jerome3o/jsonllm:latest .

# Push
sudo docker push jerome3o/jsonllm:latest
