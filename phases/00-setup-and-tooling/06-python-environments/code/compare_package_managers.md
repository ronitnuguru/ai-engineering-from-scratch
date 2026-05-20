# Python Package Manager Comparison

## Quick Reference

| Feature | uv | pip | conda |
|---------|----|----|-------|
| **Speed** | ⚡⚡⚡ 10-100x faster | Baseline | Slow |
| **Manages Python versions** | ✅ Yes | ❌ No | ✅ Yes |
| **Handles non-Python deps** | ❌ No | ❌ No | ✅ Yes (CUDA, etc.) |
| **Lockfile generation** | ✅ Automatic | Manual (pip-tools) | Manual |
| **Virtual environments** | ✅ Built-in | ✅ Built-in (venv) | ✅ Built-in |
| **Best for** | Most projects | Legacy projects | CUDA/scientific computing |

## When to Use Each

### Use `uv` (Recommended for this course)
```bash
uv venv
source .venv/bin/activate
uv pip install torch numpy
```

**Advantages:**
- 10-100x faster than pip
- Handles Python version management
- Automatic lockfile generation
- Drop-in replacement for pip

**When:**
- Starting a new project
- Need speed (large dependency trees)
- Want modern tooling

---

### Use `pip + venv`
```bash
python -m venv .venv
source .venv/bin/activate
pip install torch numpy
```

**Advantages:**
- Ships with Python (no install needed)
- Universal compatibility
- Simple and well-documented

**When:**
- Can't install uv
- Working on shared/restricted systems
- Need maximum compatibility

---

### Use `conda`
```bash
conda create -n myenv python=3.12
conda activate myenv
conda install pytorch torchvision pytorch-cuda=12.4 -c pytorch
```

**Advantages:**
- Installs non-Python dependencies (CUDA toolkit, cuDNN)
- Manages system libraries
- Good for scientific computing stacks

**When:**
- Need specific CUDA toolkit version
- Working on HPC/cluster without system access
- Library documentation says "use conda"

**⚠️ Warning:** Never mix `pip` and `conda` in the same environment. Pick one.

---

## Speed Comparison

Typical install times for PyTorch + dependencies:

| Tool | Time |
|------|------|
| **uv** | ~8 seconds |
| **pip** | ~45 seconds |
| **conda** | ~2-5 minutes |

*(Times vary by network, cache, platform)*

---

## This Course Recommendation

Use **`uv`** for everything:

```bash
# Install uv (one time)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Every project
cd my-project
uv venv
source .venv/bin/activate
uv pip install <packages>
```

Only switch to `conda` if:
- You need a specific CUDA toolkit version
- A library explicitly requires conda
- You're on a cluster without uv access

---

## Common Mistakes

### ❌ Installing globally
```bash
pip install torch  # BAD: Goes to system Python
```

### ✅ Install in virtual environment
```bash
source .venv/bin/activate
uv pip install torch  # GOOD: Isolated
```

---

### ❌ Mixing pip and conda
```bash
conda activate myenv
conda install pytorch
pip install transformers  # BAD: Can break conda
```

### ✅ Stick to one
```bash
conda activate myenv
conda install pytorch
conda install transformers  # GOOD: Consistent
```

---

### ❌ Forgetting to activate
```bash
python train.py  # Uses system Python
```

### ✅ Always activate first
```bash
source .venv/bin/activate
python train.py  # Uses project Python
```

---

## Troubleshooting

### "Command not found: uv"
```bash
# Add to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### "Which Python am I using?"
```bash
which python  # Should show .venv/bin/python
python --version
```

### "Packages not found after install"
```bash
# Make sure venv is activated
source .venv/bin/activate
# Reinstall if needed
uv pip install <package>
```

### "CUDA version mismatch"
```bash
# Check driver version
nvidia-smi

# Check PyTorch version
python -c "import torch; print(torch.version.cuda)"

# Install matching version
uv pip install torch --index-url https://download.pytorch.org/whl/cu121
```
