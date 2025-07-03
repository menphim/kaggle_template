#!/bin/bash
# Kaggle environment setup script

set -e

echo "Setting up Kaggle competition environment..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv is not installed. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

# Create virtual environment and install dependencies
echo "Creating virtual environment and installing dependencies..."
uv venv
source .venv/bin/activate
uv pip install -e .

# Create necessary directories
echo "Creating project directories..."
mkdir -p data/{raw,processed,external}
mkdir -p notebooks
mkdir -p models
mkdir -p output
mkdir -p logs

# Set up Kaggle API
echo "Setting up Kaggle API..."
mkdir -p ~/.kaggle

if [ ! -f ~/.kaggle/kaggle.json ]; then
    echo "Warning: kaggle.json not found!"
    echo "Please download kaggle.json from https://www.kaggle.com/settings/account"
    echo "and place it at ~/.kaggle/kaggle.json"
else
    chmod 600 ~/.kaggle/kaggle.json
    echo "Kaggle API credentials found and configured."
fi

# Create .env file template
if [ ! -f .env ]; then
    echo "Creating .env file template..."
    cat > .env << 'EOF'
# Kaggle API credentials (optional, if not using ~/.kaggle/kaggle.json)
# KAGGLE_USERNAME=your_username
# KAGGLE_KEY=your_api_key

# Project settings
PROJECT_NAME=kaggle-competition
RANDOM_SEED=42
EOF
fi

# Create .gitignore
if [ ! -f .gitignore ]; then
    echo "Creating .gitignore..."
    cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb

# Data files
data/raw/*
data/processed/*
data/external/*
!data/raw/.gitkeep
!data/processed/.gitkeep
!data/external/.gitkeep

# Models
models/*
!models/.gitkeep

# Output
output/*
!output/.gitkeep

# Logs
logs/*
!logs/.gitkeep

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Kaggle
kaggle.json
EOF
fi

# Create .gitkeep files
touch data/raw/.gitkeep
touch data/processed/.gitkeep
touch data/external/.gitkeep
touch models/.gitkeep
touch output/.gitkeep
touch logs/.gitkeep

# Make scripts executable
chmod +x scripts/*.py
chmod +x scripts/*.sh

echo "Environment setup complete!"
echo ""
echo "To activate the environment, run:"
echo "source .venv/bin/activate"
echo ""
echo "To download competition data, run:"
echo "python scripts/download_data.py [competition-name]"
echo ""
echo "To start Jupyter notebook, run:"
echo "jupyter notebook"