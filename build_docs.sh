#!/bin/bash
# Build script for WTHM IoT Device Documentation
# Usage: 
#   ./build_docs.sh              # Build Chinese version (default)
#   ./build_docs.sh zh           # Build Chinese version
#   ./build_docs.sh en           # Build English version
#   ./build_docs.sh all          # Build both Chinese and English versions

# Exit on any error
set -e

# Determine build language from first argument, default to Chinese
BUILD_LANG=${1:-zh}
BUILD_LANG=$(echo "$BUILD_LANG" | tr '[:upper:]' '[:lower:]')

echo "Building WTHM IoT Device Documentation for language: $BUILD_LANG..."

# Check if sphinx-build is available
if ! command -v sphinx-build &> /dev/null; then
    echo "sphinx-build could not be found. Please install Sphinx first."
    echo "You can install it using: pip install -r requirements.txt"
    exit 1
fi

case "$BUILD_LANG" in
    "zh"|"cn"|"chinese")
        echo "Building Chinese version..."
        # Clean previous build
        echo "Cleaning previous build..."
        rm -rf docs/_build/html_zh
        
        # Build the Chinese documentation
        echo "Building Chinese documentation..."
        SPHINX_LANGUAGE=zh_CN sphinx-build -b html docs docs/_build/html_zh
        echo "Chinese documentation build completed successfully!"
        echo "You can view it by opening docs/_build/html_zh/index.html in your browser."
        ;;
    "en"|"english")
        echo "Building English version..."
        # Clean previous build
        echo "Cleaning previous build..."
        rm -rf docs/_build/html_en
        
        # Build the English documentation
        echo "Building English documentation..."
        SPHINX_LANGUAGE=en sphinx-build -b html docs docs/_build/html_en
        echo "English documentation build completed successfully!"
        echo "You can view it by opening docs/_build/html_en/index.html in your browser."
        ;;
    "all")
        echo "Building both Chinese and English versions..."
        
        # Build Chinese version
        echo "Building Chinese version..."
        rm -rf docs/_build/html_zh
        SPHINX_LANGUAGE=zh_CN sphinx-build -b html docs docs/_build/html_zh
        echo "Chinese documentation build completed successfully!"
        
        # Build English version
        echo "Building English version..."
        rm -rf docs/_build/html_en
        SPHINX_LANGUAGE=en sphinx-build -b html docs docs/_build/html_en
        echo "English documentation build completed successfully!"
        
        echo "Both versions built successfully!"
        echo "Chinese version: docs/_build/html_zh/index.html"
        echo "English version: docs/_build/html_en/index.html"
        ;;
    *)
        echo "Usage: $0 [zh|en|all]"
        echo "  zh (default) - Build Chinese version"
        echo "  en - Build English version" 
        echo "  all - Build both versions"
        exit 1
        ;;
esac

echo "Documentation build completed successfully!"