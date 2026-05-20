# Editor Setup Guide for AI Engineering

## Quick Start

### Option 1: VS Code (Recommended)

1. **Install VS Code**
   ```bash
   brew install --cask visual-studio-code
   ```

2. **Add `code` to PATH**
   - Open VS Code
   - Press `Cmd+Shift+P`
   - Type "Shell Command: Install 'code' command in PATH"
   - Select it

3. **Verify Installation**
   ```bash
   code --version
   ```

4. **Install Extensions (Automated)**
   ```bash
   # Navigate to project root
   cd /path/to/ai-engineering-from-scratch
   
   # Install all recommended extensions
   code --install-extension ms-python.python
   code --install-extension ms-python.vscode-pylance
   code --install-extension ms-toolsai.jupyter
   code --install-extension ms-python.debugpy
   code --install-extension ms-python.black-formatter
   code --install-extension charliermarsh.ruff
   code --install-extension eamodio.gitlens
   code --install-extension ms-vscode-remote.remote-ssh
   code --install-extension ms-vscode-remote.remote-containers
   code --install-extension redhat.vscode-yaml
   code --install-extension tamasfe.even-better-toml
   ```

5. **Copy Settings**
   ```bash
   # Create .vscode directory in project root
   mkdir -p .vscode
   
   # Copy recommended settings
   cp phases/00-setup-and-tooling/08-editor-setup/code/vscode/settings.json .vscode/
   cp phases/00-setup-and-tooling/08-editor-setup/code/vscode/extensions.json .vscode/
   ```

6. **Open Project**
   ```bash
   code .
   ```

---

### Option 2: Cursor (AI-Enhanced VS Code Fork)

1. **Install Cursor**
   ```bash
   brew install --cask cursor
   ```

2. **Import VS Code Settings**
   - Cursor automatically imports VS Code settings
   - All VS Code extensions work in Cursor
   - Follow steps 4-6 from VS Code setup above

---

### Option 3: Windsurf (AI-First Editor)

Similar to Cursor, Windsurf is VS Code-compatible:
```bash
# Download from windsurf.com
# Import settings from .vscode/ directory
```

---

## Essential Extensions Explained

| Extension | Purpose | Why Critical for AI |
|-----------|---------|---------------------|
| **Python** | Core Python support | Language detection, virtual env integration |
| **Pylance** | Fast type checking | Catches tensor shape mismatches before runtime |
| **Jupyter** | Notebooks in VS Code | Run experiments without leaving editor |
| **Debugpy** | Python debugger | Step through training loops |
| **Black Formatter** | Auto-formatting | Consistent style, format on save |
| **Ruff** | Fast linting | Catch errors 10-100x faster than pylint |
| **GitLens** | Git history | See who changed what, blame inline |
| **Remote SSH** | Remote development | Edit files on GPU boxes as if local |
| **Remote Containers** | Docker dev | Develop inside containers |

---

## Key Settings Explained

### Python Analysis
```jsonc
"python.analysis.typeCheckingMode": "basic"
```
**Why:** Catches wrong argument types (e.g., passing list instead of tensor) before you run.

### Format on Save
```jsonc
"[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
}
```
**Why:** Never think about formatting. Black handles it automatically.

### Rulers at 88 and 120
```jsonc
"editor.rulers": [88, 120]
```
**Why:** Black wraps at 88. The 120 marker shows when comments get too long.

### Notebook Output Scrolling
```jsonc
"notebook.output.scrolling": true
```
**Why:** Training loops print thousands of lines. Without scrolling, output explodes.

### Auto-save
```jsonc
"files.autoSave": "afterDelay",
"files.autoSaveDelay": 1000
```
**Why:** Prevents running stale code when you forget to save.

### Terminal Scrollback
```jsonc
"terminal.integrated.scrollback": 10000
```
**Why:** Long training logs don't disappear. You can scroll back to see errors.

---

## Remote SSH Setup (Critical for AI Work)

### Why You Need This
You'll train on:
- Cloud VMs (AWS, GCP, Azure)
- GPU rentals (Lambda, Vast.ai, RunPod)
- Lab servers

Remote SSH lets you edit files, run terminals, and debug on these machines as if they were local.

### Setup Steps

1. **Generate SSH Key (if you don't have one)**
   ```bash
   ssh-keygen -t ed25519 -C "your-email@example.com"
   # Press Enter for all prompts (use defaults)
   ```

2. **Copy Key to Remote Machine**
   ```bash
   ssh-copy-id user@remote-gpu-ip
   ```

3. **Test Connection**
   ```bash
   ssh user@remote-gpu-ip
   # Should connect without password
   exit
   ```

4. **Add to SSH Config (Optional but Recommended)**
   ```bash
   # Edit ~/.ssh/config
   cat >> ~/.ssh/config <<EOF
   
   Host gpu-box
       HostName 203.0.113.50
       User ubuntu
       IdentityFile ~/.ssh/id_ed25519
       ForwardAgent yes
   EOF
   ```

5. **Connect in VS Code**
   - Press `Cmd+Shift+P`
   - Type "Remote-SSH: Connect to Host"
   - Select "gpu-box" (or enter `user@ip`)
   - VS Code installs its server component automatically
   - Open a folder on the remote machine
   - Edit files, run terminals, debug - all remote!

---

## Keyboard Shortcuts (Essential)

### Editor
| Action | macOS | Linux/Windows |
|--------|-------|---------------|
| Command Palette | `Cmd+Shift+P` | `Ctrl+Shift+P` |
| Quick Open | `Cmd+P` | `Ctrl+P` |
| Find in Files | `Cmd+Shift+F` | `Ctrl+Shift+F` |
| Format Document | `Shift+Alt+F` | `Shift+Alt+F` |

### Terminal
| Action | macOS | Linux/Windows |
|--------|-------|---------------|
| Toggle Terminal | `` Ctrl+` `` | `` Ctrl+` `` |
| New Terminal | `` Ctrl+Shift+` `` | `` Ctrl+Shift+` `` |
| Split Terminal | `Cmd+\` | `Ctrl+\` |

### Jupyter
| Action | macOS | Linux/Windows |
|--------|-------|---------------|
| Run Cell | `Shift+Enter` | `Shift+Enter` |
| Run Cell Below | `Alt+Enter` | `Alt+Enter` |
| Insert Cell Above | `A` | `A` |
| Insert Cell Below | `B` | `B` |

---

## Verification Checklist

After setup, verify everything works:

- [ ] `code --version` shows VS Code version
- [ ] Open a `.py` file, see type hints and autocomplete (Pylance)
- [ ] Save a Python file, see it auto-format (Black)
- [ ] Open a `.ipynb` file, can run cells (Jupyter)
- [ ] Open integrated terminal with `` Ctrl+` ``
- [ ] Git blame shows inline (GitLens)

---

## Troubleshooting

### Extensions Not Installing
```bash
# Check VS Code can access extension marketplace
code --list-extensions

# Force reinstall
code --install-extension ms-python.python --force
```

### Format on Save Not Working
1. Open Settings (`Cmd+,`)
2. Search "format on save"
3. Ensure "Editor: Format On Save" is checked
4. Check "Default Formatter" is set to "Black Formatter" for Python

### Pylance Type Hints Not Showing
1. Open Command Palette (`Cmd+Shift+P`)
2. Type "Python: Select Interpreter"
3. Choose the one from your `.venv` directory
4. Reload window (`Cmd+Shift+P` → "Reload Window")

### Remote SSH Connection Fails
```bash
# Test SSH connection manually
ssh user@remote-ip

# Check SSH config
cat ~/.ssh/config

# Check SSH key permissions (must be 600)
chmod 600 ~/.ssh/id_ed25519
```

---

## Alternative: Vim/Neovim

If you already use Vim/Neovim productively, stay there. Minimum setup:

```lua
-- ~/.config/nvim/init.lua (Neovim)
require('packer').startup(function()
  use 'neovim/nvim-lspconfig'        -- LSP support
  use 'williamboman/mason.nvim'      -- Package manager
  use 'jose-elias-alvarez/null-ls.nvim'  -- Formatting/linting
  use 'nvim-telescope/telescope.nvim'    -- Fuzzy finder
  use 'kiyoon/jupyter-vim'           -- Jupyter integration
end)

-- Configure pyright
require('lspconfig').pyright.setup{}

-- Configure black and ruff
local null_ls = require('null-ls')
null_ls.setup({
    sources = {
        null_ls.builtins.formatting.black,
        null_ls.builtins.diagnostics.ruff,
    },
})
```

**Warning:** If you don't already use Vim, don't start now. The learning curve will compete with learning AI engineering.

---

## Next Steps

1. Install VS Code or preferred editor
2. Install all extensions
3. Copy settings to `.vscode/` directory
4. Open the project and verify setup
5. If you have a remote GPU, set up SSH access

You're now ready for efficient AI development!
