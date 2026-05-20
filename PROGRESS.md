# My Learning Progress

## Phase 0: Setup & Tooling ✅

### Completed Lessons:

#### ✅ Lesson 1: Dev Environment (~45 min)
- **Date:** 2026-05-20
- **What I Built:**
  - Installed Python 3.14.5 with uv package manager
  - Set up virtual environment with NumPy, Matplotlib, Jupyter
  - Installed Node.js 22 and Rust 1.95.0
  - Configured PyTorch 2.12.0 with Metal support for M4 Pro
  - All verification checks passed (7/7 core, 1/2 GPU - Metal ready)

#### ✅ Lesson 2: Git & Collaboration (~30 min)
- **Date:** 2026-05-20
- **What I Learned:**
  - Git workflow: working directory → staging → local repo → remote
  - Core commands: add, commit, push, branch, merge
  - Created `my-progress` branch for tracking work
  - Set up `.gitignore` for AI projects
  - Explored repo commit history

#### ✅ Lesson 3: GPU Setup & Cloud (~45 min)
- **Date:** 2026-05-20
- **What I Built:**
  - Verified M4 Pro GPU with Metal support
  - Benchmarked CPU vs GPU: 1.3x speedup on 5000x5000 matrix
  - System capacity: 51.5GB unified memory, ~2.9B parameter models
  - Created Metal benchmark script and Colab notebook
  - Learned about GPU options: local (Metal), Colab (free), cloud (paid)

#### ✅ Lesson 4: APIs & Keys (~30 min)
- **Date:** 2026-05-20
- **What I Built:**
  - Learned API anatomy: endpoint + auth + request → response
  - Created .env.example template for secure key storage
  - Built sdk_example.py (Anthropic SDK usage)
  - Built raw_http_example.py (understanding under-the-hood)
  - Built test_error_handling.py (authentication errors)
  - Installed Anthropic SDK and tested error handling
  - APIs needed: Anthropic (Phase 11+), OpenAI (comparison), HuggingFace (models)

#### ✅ Lesson 5: Jupyter Notebooks (~30 min)
- **Date:** 2026-05-20
- **What I Built:**
  - Created comprehensive jupyter_tutorial.ipynb with all key features
  - Learned magic commands: %timeit, %%time, %matplotlib inline
  - Practiced inline visualization with matplotlib and pandas
  - Keyboard shortcuts cheat sheet created
  - Tested notebook execution: NumPy ~100x faster than list comprehension
  - Understood shared kernel state and common traps
  - Rule: "Explore in notebooks, ship in scripts"
  - Installed pandas for data manipulation

---

## Next Up:
- [ ] Lesson 6: Python Environments
- [ ] Lesson 7: Docker for AI
- [ ] Phase 1: Math Foundations
