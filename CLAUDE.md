# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

This project uses **uv** for dependency management and virtual environment creation. The setup process requires significant time due to large packages (PyTorch, CUDA libraries).

### Key Commands
```bash
# Environment setup (takes 5-10 minutes)
export PATH="$HOME/.local/bin:$PATH"
bash scripts/setup_environment.sh

# Activate environment
source .venv/bin/activate

# Sync dependencies after pyproject.toml changes
uv sync

# Install development tools
uv sync --group dev
```

### Development Tools
```bash
# Code formatting
black .
isort .
flake8 .

# Start Jupyter environment
jupyter lab  # or jupyter notebook
```

## Project Architecture

This is a **Kaggle competition template** designed for data science workflows. The architecture follows a standard ML project structure:

### Directory Structure
- `data/` - Data storage (git-ignored)
  - `raw/` - Original competition/dataset files
  - `processed/` - Cleaned/transformed data
  - `external/` - Additional datasets
- `notebooks/` - Jupyter notebooks for EDA and experimentation
- `models/` - Trained model artifacts (git-ignored)
- `output/` - Submission files and results (git-ignored)
- `logs/` - Training/experiment logs (git-ignored)
- `scripts/` - Utility scripts
- `configs/` - Configuration files

### Key Dependencies
- **Data Science Stack**: pandas 2.3.0, numpy 2.3.1, scipy 1.16.0
- **ML Libraries**: scikit-learn 1.7.0, xgboost 3.0.2, lightgbm 4.6.0, catboost 1.2.8
- **Deep Learning**: PyTorch 2.7.1+cu126 (GPU-enabled), transformers 4.53.0
- **Visualization**: matplotlib, seaborn, plotly
- **Experiment Tracking**: optuna for hyperparameter optimization

## Kaggle Integration

### Data Download Script
The `scripts/download_data.py` script handles Kaggle API integration:

```bash
# Download competition data
python scripts/download_data.py titanic

# Download external dataset
python scripts/download_data.py --dataset username/dataset-name

# List available competitions
python scripts/download_data.py --list
```

**Prerequisites**: 
- Download `kaggle.json` from Kaggle account settings
- Place at `~/.kaggle/kaggle.json`
- The setup script will set proper permissions (600)

### Configuration Management
- Environment variables in `.env` file (created by setup script)
- Project uses `RANDOM_SEED=42` for reproducibility
- All data directories are git-ignored to prevent accidental commits

## Package Configuration Notes

The `pyproject.toml` is configured with `packages = []` under `[tool.setuptools]` to prevent setuptools from treating data directories as Python packages. This is essential for the build process to work correctly.

## Development Workflow

1. **Setup**: Run setup script once per environment
2. **Data**: Use download script to fetch competition data
3. **Explore**: Use Jupyter notebooks for EDA in `notebooks/`
4. **Process**: Save cleaned data to `data/processed/`
5. **Model**: Train models, save artifacts to `models/`
6. **Submit**: Generate submission files in `output/`

## Important Notes

- GPU-enabled PyTorch is installed by default
- Initial setup downloads ~3GB of packages
- All model artifacts and data files are git-ignored
- The template supports both traditional ML and deep learning workflows