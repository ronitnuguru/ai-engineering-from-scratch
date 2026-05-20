#!/bin/bash
# Demo: Virtual Environment Isolation
#
# This script demonstrates how two virtual environments can have
# different package versions installed side-by-side.

set -e

echo "=== Virtual Environment Isolation Demo ==="
echo ""
echo "This demonstrates why virtual environments are essential."
echo ""

# Create a temporary directory
DEMO_DIR=$(mktemp -d)
cd "$DEMO_DIR"

echo "📁 Working in: $DEMO_DIR"
echo ""

# Create first environment
echo "1️⃣  Creating environment A with NumPy 1.24..."
uv venv env-a
source env-a/bin/activate
uv pip install numpy==1.24.0 > /dev/null 2>&1
NUMPY_A=$(python -c "import numpy; print(numpy.__version__)")
deactivate
echo "   ✅ Environment A has NumPy $NUMPY_A"
echo ""

# Create second environment
echo "2️⃣  Creating environment B with NumPy 2.4..."
uv venv env-b
source env-b/bin/activate
uv pip install numpy==2.4.0 > /dev/null 2>&1
NUMPY_B=$(python -c "import numpy; print(numpy.__version__)")
deactivate
echo "   ✅ Environment B has NumPy $NUMPY_B"
echo ""

# Verify isolation
echo "3️⃣  Verifying isolation..."
echo ""

echo "   Activating environment A:"
source env-a/bin/activate
NUMPY_CHECK=$(python -c "import numpy; print(numpy.__version__)")
echo "   → NumPy version: $NUMPY_CHECK"
deactivate

echo ""
echo "   Activating environment B:"
source env-b/bin/activate
NUMPY_CHECK=$(python -c "import numpy; print(numpy.__version__)")
echo "   → NumPy version: $NUMPY_CHECK"
deactivate

echo ""
echo "✨ Each environment is isolated with its own package versions!"
echo ""
echo "Without virtual environments, only ONE version could exist globally,"
echo "and switching projects would require reinstalling different versions."
echo ""

# Cleanup
cd -
rm -rf "$DEMO_DIR"
echo "🧹 Cleaned up demo environments"
