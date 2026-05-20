# Docker for AI - Cheat Sheet

## Essential Commands

### Images
```bash
# Build an image from Dockerfile
docker build -t my-image .
docker build -f Dockerfile.macos -t ai-dev-macos .

# List images
docker images

# Remove an image
docker rmi my-image

# Remove unused images (free disk space)
docker image prune -a
```

### Containers
```bash
# Run a container (interactive)
docker run --rm -it my-image

# Run with volume mounts
docker run --rm -it -v $(pwd):/workspace my-image

# Run with port mapping
docker run --rm -it -p 8888:8888 my-image

# Run in background (detached)
docker run -d --name my-container my-image

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Stop a container
docker stop my-container

# Remove a container
docker rm my-container

# View container logs
docker logs -f my-container

# Execute command in running container
docker exec -it my-container bash
docker exec -it my-container python script.py
```

### Docker Compose
```bash
# Start services in background
docker compose up -d

# Start and see logs
docker compose up

# Stop services
docker compose down

# Stop and remove volumes
docker compose down -v

# View logs
docker compose logs -f

# Rebuild images
docker compose build

# Restart a service
docker compose restart ai-dev
```

---

## AI-Specific Patterns

### Volume Mounts for AI Projects
```bash
# Mount code directory
-v $(pwd):/workspace

# Mount models directory (persistent)
-v ~/models:/models

# Mount datasets directory
-v ~/datasets:/data

# All together
docker run --rm -it \
  -v $(pwd):/workspace \
  -v ~/models:/models \
  -v ~/datasets:/data \
  my-image
```

### Running Jupyter in Docker
```bash
# Run Jupyter notebook server
docker run --rm -it \
  -v $(pwd):/workspace \
  -p 8888:8888 \
  my-image \
  jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# JupyterLab
docker run --rm -it \
  -v $(pwd):/workspace \
  -p 8888:8888 \
  my-image \
  jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

### GPU Passthrough (NVIDIA only)
```bash
# Single GPU
docker run --rm -it --gpus all my-image

# Specific GPU
docker run --rm -it --gpus '"device=0"' my-image

# Multiple GPUs
docker run --rm -it --gpus '"device=0,1"' my-image

# Test GPU in container
docker run --rm --gpus all nvidia/cuda:12.4.1-base-ubuntu22.04 nvidia-smi
```

### Copy Files To/From Container
```bash
# Copy from host to container
docker cp ./model.pt my-container:/workspace/

# Copy from container to host
docker cp my-container:/workspace/results.csv ./

# Copy entire directory
docker cp ./data/ my-container:/workspace/data/
```

---

## Common AI Base Images

### NVIDIA CUDA
```dockerfile
# Full CUDA toolkit (for building packages)
FROM nvidia/cuda:12.4.1-devel-ubuntu22.04

# Runtime only (smaller, for running code)
FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04

# Base (minimal, just drivers)
FROM nvidia/cuda:12.4.1-base-ubuntu22.04
```

### PyTorch
```dockerfile
# Official PyTorch image (CUDA pre-installed)
FROM pytorch/pytorch:2.3.1-cuda12.4-cudnn9-runtime

# CPU only
FROM pytorch/pytorch:2.3.1-cpu
```

### Python
```dockerfile
# Full Python
FROM python:3.12

# Slim (smaller, no build tools)
FROM python:3.12-slim

# Alpine (smallest, but may have compatibility issues)
FROM python:3.12-alpine
```

---

## Dockerfile Best Practices for AI

### 1. Layer Caching
```dockerfile
# ✅ GOOD: Install dependencies first (changes rarely)
FROM python:3.12-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ❌ BAD: Copy everything first (cache invalidated on any change)
FROM python:3.12-slim
COPY . .
RUN pip install -r requirements.txt
```

### 2. Use .dockerignore
```
# .dockerignore
.venv/
__pycache__/
*.pyc
.git/
.DS_Store
*.ipynb_checkpoints/
models/
datasets/
*.pt
*.pth
```

### 3. Pin Versions
```dockerfile
# ✅ GOOD: Reproducible builds
RUN pip install torch==2.3.1 numpy==1.26.4

# ❌ BAD: May break in future
RUN pip install torch numpy
```

### 4. Multi-Stage Builds (Advanced)
```dockerfile
# Build stage
FROM python:3.12 as builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage (smaller)
FROM python:3.12-slim
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
```

---

## Troubleshooting

### Container Won't Start
```bash
# Check logs
docker logs my-container

# Start with shell to debug
docker run --rm -it my-image /bin/bash
```

### Permission Issues
```bash
# Run as current user (not root)
docker run --rm -it --user $(id -u):$(id -g) my-image

# Fix file ownership
sudo chown -R $USER:$USER ./
```

### Disk Space Issues
```bash
# See disk usage
docker system df

# Clean up everything unused
docker system prune -a --volumes

# Remove specific items
docker image prune    # unused images
docker container prune # stopped containers
docker volume prune   # unused volumes
```

### Port Already in Use
```bash
# Find what's using the port
lsof -i :8888

# Use a different port
docker run -p 8889:8888 my-image

# Kill the process
kill -9 <PID>
```

---

## Quick Start for This Course

```bash
# Build the macOS image
cd phases/00-setup-and-tooling/07-docker-for-ai/code
docker build -f Dockerfile.macos -t ai-dev-macos .

# Run with Jupyter
docker run --rm -it \
  -v $(pwd)/../../../:/workspace \
  -v ~/models:/models \
  -p 8888:8888 \
  ai-dev-macos \
  jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root

# Or use Docker Compose
docker compose -f docker-compose.macos.yml up -d
```

---

## Further Reading

- [Docker Docs](https://docs.docker.com/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
- [PyTorch Docker Images](https://hub.docker.com/r/pytorch/pytorch)
