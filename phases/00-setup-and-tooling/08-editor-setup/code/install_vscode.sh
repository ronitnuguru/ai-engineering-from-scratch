#!/bin/bash
# VS Code Installation and Setup Script for AI Engineering

set -e

echo "=== VS Code Setup for AI Engineering ==="
echo ""

# Check if VS Code is already installed
if command -v code &> /dev/null; then
    echo "✅ VS Code is already installed"
    code --version
    echo ""
else
    echo "📥 Installing VS Code..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        brew install --cask visual-studio-code
        echo "✅ VS Code installed"
        echo ""
        echo "⚠️  Please add 'code' command to PATH:"
        echo "   1. Open VS Code"
        echo "   2. Press Cmd+Shift+P"
        echo "   3. Type 'Shell Command: Install code command in PATH'"
        echo "   4. Select it"
        echo ""
        echo "Then run this script again to install extensions."
        exit 0
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
        sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
        sudo sh -c 'echo "deb [arch=amd64,arm64,armhf] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
        rm -f packages.microsoft.gpg
        sudo apt update
        sudo apt install -y code
        echo "✅ VS Code installed"
        echo ""
    else
        echo "❌ Unsupported OS: $OSTYPE"
        echo "Please install VS Code manually from https://code.visualstudio.com/"
        exit 1
    fi
fi

# Install extensions
echo "📦 Installing VS Code extensions..."
echo ""

extensions=(
    "ms-python.python"
    "ms-python.vscode-pylance"
    "ms-toolsai.jupyter"
    "ms-python.debugpy"
    "ms-python.black-formatter"
    "charliermarsh.ruff"
    "eamodio.gitlens"
    "ms-vscode-remote.remote-ssh"
    "ms-vscode-remote.remote-containers"
    "redhat.vscode-yaml"
    "tamasfe.even-better-toml"
)

for ext in "${extensions[@]}"; do
    echo "  Installing $ext..."
    code --install-extension "$ext" --force 2>&1 | grep -v "is already installed" || true
done

echo ""
echo "✅ All extensions installed"
echo ""

# Copy settings to project
echo "⚙️  Copying recommended settings to .vscode/..."
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../../.." && pwd)"

mkdir -p "$PROJECT_ROOT/.vscode"

if [ ! -f "$PROJECT_ROOT/.vscode/settings.json" ]; then
    cp "$SCRIPT_DIR/vscode/settings.json" "$PROJECT_ROOT/.vscode/"
    echo "✅ Copied settings.json"
else
    echo "ℹ️  .vscode/settings.json already exists (not overwriting)"
fi

if [ ! -f "$PROJECT_ROOT/.vscode/extensions.json" ]; then
    cp "$SCRIPT_DIR/vscode/extensions.json" "$PROJECT_ROOT/.vscode/"
    echo "✅ Copied extensions.json"
else
    echo "ℹ️  .vscode/extensions.json already exists (not overwriting)"
fi

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "Next steps:"
echo "  1. Open VS Code: code ."
echo "  2. Open a Python file to verify Pylance works"
echo "  3. Edit and save to verify Black formatting works"
echo "  4. Open a .ipynb file to verify Jupyter works"
echo ""
echo "For remote development:"
echo "  - Press Cmd+Shift+P (or Ctrl+Shift+P)"
echo "  - Type 'Remote-SSH: Connect to Host'"
echo "  - Enter your GPU box IP or hostname"
echo ""
