#!/usr/bin/env python3
"""
GPU vs CPU Benchmark - Metal (Apple Silicon) Edition

Compares matrix multiplication performance on CPU vs GPU (Metal Performance Shaders).
"""

import torch
import time

def benchmark_matmul(size=5000):
    """Benchmark matrix multiplication on CPU and GPU."""

    print("=== GPU vs CPU Benchmark ===\n")
    print(f"Matrix size: {size}x{size}\n")

    # Generate random matrices
    a_cpu = torch.randn(size, size)
    b_cpu = torch.randn(size, size)

    # CPU benchmark
    print("Running on CPU...")
    start = time.time()
    c_cpu = a_cpu @ b_cpu
    cpu_time = time.time() - start
    print(f"CPU time: {cpu_time:.3f}s\n")

    # GPU (Metal) benchmark
    if torch.backends.mps.is_available():
        print("Running on GPU (Metal)...")
        device = torch.device("mps")

        a_gpu = a_cpu.to(device)
        b_gpu = b_cpu.to(device)

        # Warmup
        _ = a_gpu @ b_gpu

        # Actual benchmark
        start = time.time()
        c_gpu = a_gpu @ b_gpu
        torch.mps.synchronize()  # Wait for GPU to finish
        gpu_time = time.time() - start

        print(f"GPU time: {gpu_time:.3f}s")
        print(f"Speedup: {cpu_time / gpu_time:.1f}x\n")

        # Memory info
        print(f"GPU Device: Apple M4 Pro")
        print(f"Metal available: Yes")
        print(f"\nNote: Apple Silicon uses unified memory (shared RAM/VRAM)")

    else:
        print("Metal (GPU) not available. Running on CPU only.")
        print("This shouldn't happen on M4 Pro - check PyTorch installation.")

    return cpu_time, gpu_time if torch.backends.mps.is_available() else None

def estimate_model_capacity():
    """Estimate how large a model can fit in memory."""
    import psutil

    total_ram = psutil.virtual_memory().total / 1e9
    available_ram = psutil.virtual_memory().available / 1e9

    print("\n=== Model Capacity Estimate ===\n")
    print(f"Total RAM: {total_ram:.1f} GB")
    print(f"Available RAM: {available_ram:.1f} GB")
    print("\nRule of thumb (fp16 training):")
    print(f"  - Model size: ~{available_ram * 0.3:.1f} GB")
    print(f"  - Max parameters: ~{(available_ram * 0.3 * 1e9) / 2 / 1e6:.0f}M parameters")
    print("\n(M4 Pro uses unified memory, so this is shared for CPU+GPU)")

if __name__ == "__main__":
    try:
        cpu_time, gpu_time = benchmark_matmul(size=5000)
        estimate_model_capacity()
    except ImportError:
        print("Error: psutil not installed. Run: pip install psutil")
