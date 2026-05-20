#!/usr/bin/env python3
"""
Environment Verification Script

Checks that your Python environment is correctly set up and isolated.
"""

import sys
import os
import subprocess
from pathlib import Path

def check_python_location():
    """Verify Python is running from the virtual environment."""
    print("=== Python Location ===")
    python_path = sys.executable
    print(f"Python: {python_path}")

    if ".venv" in python_path:
        print("✅ Running from virtual environment")
        return True
    else:
        print("⚠️  WARNING: Running from system Python (not a venv)")
        return False

def check_python_version():
    """Check Python version meets minimum requirements."""
    print("\n=== Python Version ===")
    version = sys.version_info
    print(f"Version: {version.major}.{version.minor}.{version.micro}")

    if version >= (3, 11):
        print("✅ Python 3.11+ (meets course requirements)")
        return True
    else:
        print("❌ Python 3.11+ required")
        return False

def check_package_manager():
    """Check which package manager is available."""
    print("\n=== Package Manager ===")

    try:
        result = subprocess.run(["uv", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ uv: {result.stdout.strip()}")
            return "uv"
    except FileNotFoundError:
        pass

    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ pip: {result.stdout.strip()}")
            return "pip"
    except:
        pass

    print("❌ No package manager found")
    return None

def check_installed_packages():
    """List key packages and their versions."""
    print("\n=== Key Packages ===")

    packages_to_check = [
        ("numpy", "Array operations"),
        ("matplotlib", "Plotting"),
        ("jupyter", "Notebooks"),
        ("torch", "Deep learning"),
        ("pandas", "Data manipulation"),
        ("anthropic", "Claude API")
    ]

    installed = {}
    for package, description in packages_to_check:
        try:
            module = __import__(package)
            version = getattr(module, "__version__", "unknown")
            print(f"✅ {package:15} {version:12} ({description})")
            installed[package] = version
        except ImportError:
            print(f"❌ {package:15} {'not installed':12} ({description})")

    return installed

def check_cuda_availability():
    """Check if CUDA or Metal is available for GPU acceleration."""
    print("\n=== GPU Support ===")

    try:
        import torch

        # Check CUDA (NVIDIA)
        if torch.cuda.is_available():
            print(f"✅ CUDA available")
            print(f"   Device: {torch.cuda.get_device_name(0)}")
            print(f"   CUDA version: {torch.version.cuda}")
            return "cuda"

        # Check MPS (Apple Silicon)
        elif torch.backends.mps.is_available():
            print(f"✅ Metal (MPS) available")
            print(f"   Device: Apple Silicon GPU")
            return "mps"

        else:
            print("ℹ️  CPU only (no GPU acceleration)")
            return "cpu"

    except ImportError:
        print("⚠️  PyTorch not installed, can't check GPU")
        return None

def check_environment_isolation():
    """Test that the environment is truly isolated."""
    print("\n=== Environment Isolation ===")

    # Check site-packages location
    site_packages = None
    for path in sys.path:
        if "site-packages" in path and ".venv" in path:
            site_packages = path
            break

    if site_packages:
        print(f"✅ Packages installed to: {site_packages}")
        return True
    else:
        print("⚠️  Using system site-packages (not isolated)")
        return False

def generate_summary():
    """Generate a summary report."""
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    checks = {
        "Python in venv": check_python_location(),
        "Python version": check_python_version(),
        "Package manager": check_package_manager() is not None,
        "Isolation": check_environment_isolation()
    }

    installed = check_installed_packages()
    gpu = check_cuda_availability()

    print("\n" + "="*60)

    passed = sum(1 for v in checks.values() if v)
    total = len(checks)

    print(f"\nCore checks: {passed}/{total} passed")
    print(f"Packages: {len(installed)}/6 installed")

    if gpu:
        print(f"GPU: {gpu.upper()} acceleration available")

    print("\n✨ Your environment is ready for AI engineering!" if passed == total else "\n⚠️  Some checks failed, review above")

if __name__ == "__main__":
    print("AI Engineering Environment Check\n")
    generate_summary()
