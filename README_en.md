# Kaggle Competition Template

A template project for Kaggle competitions using UV and Kaggle API.

## Setup

### 1. Environment Initialization

```bash
# Run setup script
bash scripts/setup_environment.sh

# Activate virtual environment
source .venv/bin/activate
```

### 2. Kaggle API Configuration

1. Download kaggle.json from [Kaggle Account](https://www.kaggle.com/settings/account)
2. Place it at `~/.kaggle/kaggle.json`
3. Set permissions: `chmod 600 ~/.kaggle/kaggle.json`

## Usage

### Data Download

```bash
# Download competition data
python scripts/download_data.py [competition-name]

# Download dataset
python scripts/download_data.py --dataset [username/dataset-name]

# List available competitions
python scripts/download_data.py --list
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

## Project Structure

```
kaggle-template/
├── data/
│   ├── raw/          # Raw data
│   ├── processed/    # Processed data
│   └── external/     # External datasets
├── notebooks/        # Jupyter notebooks
├── models/           # Trained models
├── output/           # Submission files
├── logs/             # Log files
├── scripts/          # Utility scripts
├── pyproject.toml    # Project configuration
└── README.md
```

## Key Dependencies

- **Data Processing**: pandas, numpy, scipy
- **Machine Learning**: scikit-learn, xgboost, lightgbm, catboost
- **Deep Learning**: torch, transformers
- **Visualization**: matplotlib, seaborn, plotly
- **API**: kaggle
- **Optimization**: optuna

## Development Tools

Install development packages:

```bash
uv pip install -e ".[dev]"
```

Code formatting:

```bash
black .
isort .
```

## Example Usage

1. Start a new competition:
   ```bash
   python scripts/download_data.py titanic
   ```

2. Begin EDA with Jupyter notebook:
   ```bash
   jupyter notebook
   ```

3. Train models and generate submission files

## Notes

- Files in the `data/` directory are included in `.gitignore`
- Keep Kaggle API credentials secure
- Do not commit large data files to Git

## Features

- **UV Package Manager**: Fast dependency resolution and installation
- **Kaggle API Integration**: Automated data downloading
- **Kaggle Notebook Compatibility**: Same dependencies as Kaggle environment
- **Pre-configured Environment**: Ready-to-use setup for competitions
- **Organized Structure**: Clean project layout for efficient workflow

## Requirements

- Python 3.10+
- UV package manager
- Kaggle account with API access

## Getting Started

1. Clone or download this template
2. Run `bash scripts/setup_environment.sh`
3. Configure Kaggle API credentials
4. Download your competition data
5. Start coding in Jupyter notebooks!

This template provides everything you need to quickly start participating in Kaggle competitions with a professional, organized approach.