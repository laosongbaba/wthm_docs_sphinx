#!/bin/bash
# Build script for WTHM IoT Device Documentation

# Exit on any error
set -e

echo "Building WTHM IoT Device Documentation..."

# Check if sphinx-build is available
if ! command -v sphinx-build &> /dev/null; then
    echo "sphinx-build could not be found. Please install Sphinx first."
    echo "You can install it using: pip install -r requirements.txt"
    exit 1
fi

# Clean previous build
echo "Cleaning previous build..."
rm -rf docs/_build

# Build the documentation
echo "Building documentation..."
sphinx-build -b html docs docs/_build/html

echo "Documentation build completed successfully!"
echo "You can view it by opening docs/_build/html/index.html in your browser."