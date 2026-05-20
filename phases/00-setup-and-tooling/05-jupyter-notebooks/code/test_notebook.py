#!/usr/bin/env python3
"""
Test that the tutorial notebook executes without errors.
"""

import subprocess
import sys

def test_notebook():
    """Execute the notebook and check for errors."""
    notebook_path = "phases/00-setup-and-tooling/05-jupyter-notebooks/code/jupyter_tutorial.ipynb"

    print("Testing notebook execution...")
    print(f"Notebook: {notebook_path}\n")

    try:
        # Execute notebook using jupyter nbconvert
        result = subprocess.run(
            [
                "jupyter", "nbconvert",
                "--to", "notebook",
                "--execute",
                "--stdout",
                notebook_path
            ],
            capture_output=True,
            text=True,
            timeout=60
        )

        if result.returncode == 0:
            print("✅ Notebook executed successfully!")
            print("\nThe notebook runs without errors from top to bottom.")
            return True
        else:
            print("❌ Notebook execution failed!")
            print("\nError output:")
            print(result.stderr)
            return False

    except subprocess.TimeoutExpired:
        print("❌ Notebook execution timed out (>60s)")
        return False
    except FileNotFoundError:
        print("❌ jupyter nbconvert not found")
        print("Make sure Jupyter is installed: uv pip install jupyter")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_notebook()
    sys.exit(0 if success else 1)
