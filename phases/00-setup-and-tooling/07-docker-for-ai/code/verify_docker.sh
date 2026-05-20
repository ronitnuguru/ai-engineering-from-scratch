#!/bin/bash
# Docker Installation Verification Script

echo "=== Docker Installation Check ==="
echo ""

# Check Docker version
echo "1. Docker Version:"
docker --version
echo ""

# Check Docker Compose version
echo "2. Docker Compose Version:"
docker compose version
echo ""

# Check Docker daemon status
echo "3. Docker Daemon Status:"
if docker info > /dev/null 2>&1; then
    echo "✅ Docker daemon is running"
else
    echo "❌ Docker daemon is not running"
    echo "   Run: open -a Docker"
    exit 1
fi
echo ""

# Test with hello-world
echo "4. Testing with hello-world:"
if docker run --rm hello-world > /dev/null 2>&1; then
    echo "✅ Docker can pull and run containers"
else
    echo "❌ Failed to run hello-world container"
    exit 1
fi
echo ""

# Check available resources
echo "5. Docker Resources:"
docker info 2>/dev/null | grep -E "CPUs|Total Memory|Operating System" || echo "Could not fetch resource info"
echo ""

echo "=== Docker Installation: VERIFIED ✅ ==="
echo ""
echo "Next steps:"
echo "  - Build AI dev image: docker build -f Dockerfile.macos -t ai-dev-macos ."
echo "  - Run with volumes: docker run --rm -it -v \$(pwd):/workspace ai-dev-macos"
echo "  - Start compose stack: docker compose -f docker-compose.macos.yml up -d"
