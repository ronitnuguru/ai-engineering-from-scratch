# Jupyter Keyboard Shortcuts Cheat Sheet

## Essential Shortcuts (Learn These First)

| Key | Action | Mode |
|-----|--------|------|
| `Shift+Enter` | Run cell, move to next | Both |
| `Ctrl+Enter` | Run cell, stay on same | Both |
| `Esc` | Enter command mode | Edit |
| `Enter` | Enter edit mode | Command |

## Command Mode (Blue bar - press `Esc`)

### Cell Operations
| Key | Action |
|-----|--------|
| `A` | Insert cell above |
| `B` | Insert cell below |
| `DD` | Delete cell |
| `Z` | Undo cell deletion |
| `X` | Cut cell |
| `C` | Copy cell |
| `V` | Paste cell below |
| `Shift+V` | Paste cell above |
| `M` | Convert to markdown |
| `Y` | Convert to code |

### Navigation
| Key | Action |
|-----|--------|
| `↑/K` | Select cell above |
| `↓/J` | Select cell below |
| `Shift+↑/K` | Extend selection above |
| `Shift+↓/J` | Extend selection below |

### Kernel Operations
| Key | Action |
|-----|--------|
| `00` | Restart kernel |
| `II` | Interrupt kernel |

## Edit Mode (Green bar - press `Enter`)

| Key | Action |
|-----|--------|
| `Tab` | Autocomplete or indent |
| `Shift+Tab` | Show function signature/docs |
| `Ctrl+/` | Toggle comment |
| `Ctrl+]` | Indent |
| `Ctrl+[` | Dedent |
| `Ctrl+A` | Select all in cell |
| `Ctrl+Z` | Undo |
| `Ctrl+Shift+Z` | Redo |

## Magic Commands

| Command | Purpose |
|---------|---------|
| `%timeit` | Time a single line (multiple runs) |
| `%%time` | Time entire cell (single run) |
| `%matplotlib inline` | Enable inline plots |
| `%load file.py` | Load code from file |
| `%run script.py` | Run external script |
| `%pwd` | Print working directory |
| `%cd` | Change directory |
| `%env` | Show/set environment variables |
| `%lsmagic` | List all magic commands |
| `!command` | Run shell command |

## Pro Tips

1. **View all shortcuts:** Press `Ctrl+Shift+H` (or `Cmd+Shift+H` on Mac)
2. **Function help:** Type `function?` and run to see docstring
3. **Source code:** Type `function??` to see implementation
4. **Clear output:** Edit > Clear All Outputs before committing to git
5. **Restart & Run All:** Before sharing, ensure notebook runs top-to-bottom

## VS Code Jupyter Extension

Additional shortcuts when using Jupyter in VS Code:

| Key | Action |
|-----|--------|
| `Ctrl+Shift+P` → "Jupyter" | All Jupyter commands |
| `Cmd+K V` | Open preview (Mac) |
| `Ctrl+K V` | Open preview (Windows/Linux) |
