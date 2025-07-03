# Kaggle Competition Template

A template project for Kaggle competitions using UV and Kaggle API.

## Setup

### Prerequisites

- Python 3.10+
- Internet connection (for initial setup)
- Kaggle account

### 1. Environment Initialization

```bash
# Run setup script (takes 5-10 minutes on first run)
bash scripts/setup_environment.sh

# Activate virtual environment
source .venv/bin/activate

# Or use uv directly:
export PATH="$HOME/.local/bin:$PATH"
uv sync
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

# Download with organized folder structure (recommended)
python scripts/download_data.py [competition-name] --organize

# Download dataset
python scripts/download_data.py --dataset [username/dataset-name]

# List available competitions
python scripts/download_data.py --list

# Use Kaggle CLI directly
kaggle competitions download -c [competition-name] -p data/raw
kaggle datasets download [username/dataset-name] -p data/external
```

### Notebook Acquisition and Utilization

```bash
# Search competition notebooks
python scripts/download_data.py --list-notebooks [competition-name]

# Download notebook
python scripts/download_data.py --notebook [username/notebook-name]

# Direct Kaggle CLI notebook download
kaggle kernels pull [username/notebook-name] -p notebooks/reference
```

For detailed Kaggle API usage, see **[KAGGLE_API_GUIDE.md](KAGGLE_API_GUIDE.md)**.

### Launch Jupyter Notebook

```bash
# After activating virtual environment
source .venv/bin/activate

# Start Jupyter Notebook
jupyter notebook

# Or start Jupyter Lab
jupyter lab
```

## Project Structure

```
kaggle-template/
├── data/
│   ├── raw/              # Raw data (basic)
│   ├── competitions/     # Competition-specific data (when using --organize)
│   │   ├── titanic/      # Example: Titanic competition
│   │   └── housing/      # Example: Housing price prediction
│   ├── processed/        # Processed data
│   └── external/         # External datasets
├── notebooks/            # Jupyter notebooks
│   ├── reference/        # Downloaded notebooks
│   └── [your_work]/      # Your working notebooks
├── docs/                 # Documentation
│   ├── competitions/     # Competition overviews and rules
│   ├── papers/           # Reference papers
│   ├── references/       # Reference materials
│   └── notes/            # Notes and ideas
├── models/               # Trained models
├── output/               # Submission files
├── logs/                 # Log files
├── configs/              # Configuration files
├── scripts/              # Utility scripts
├── pyproject.toml        # Project configuration
├── CLAUDE.md             # Claude Code guidance
├── KAGGLE_API_GUIDE.md   # Kaggle API usage guide
└── README.md
```

## Key Dependencies

- **Data Processing**: pandas 2.3.0, numpy 2.3.1, scipy 1.16.0
- **Machine Learning**: scikit-learn 1.7.0, xgboost 3.0.2, lightgbm 4.6.0, catboost 1.2.8
- **Deep Learning**: PyTorch 2.7.1+cu126, torchvision 0.22.1, transformers 4.53.0
- **Visualization**: matplotlib 3.10.3, seaborn 0.13.2, plotly 6.2.0
- **Development Environment**: Jupyter Lab 4.4.4, Jupyter Notebook 7.4.4
- **API**: kaggle 1.7.4.5
- **Optimization**: optuna 4.4.0
- **Others**: tqdm, joblib, etc.

## Development Tools

Install development packages:

```bash
# Using uv (recommended)
export PATH="$HOME/.local/bin:$PATH"
uv sync --group dev

# Or traditional method
pip install -e ".[dev]"
```

Code formatting and quality:

```bash
# Format code
black .
isort .

# Check code quality
flake8 .

# Run tests
pytest
```

## Example Usage

### Basic Workflow

1. **Start a new competition**:
   ```bash
   # Download data with organized folder structure
   python scripts/download_data.py titanic --organize
   
   # Search and download reference notebooks
   python scripts/download_data.py --list-notebooks titanic
   python scripts/download_data.py --notebook username/titanic-eda
   ```

2. **Begin EDA and analysis**:
   ```bash
   # Launch Jupyter
   jupyter notebook notebooks/
   
   # Review reference notebooks, then create your own
   # Data path example: data/competitions/titanic/train.csv
   ```

3. **Model training and submission**:
   ```bash
   # After training models, generate submission file
   # Example: output/submission.csv
   
   # Submit to Kaggle
   kaggle competitions submit output/submission.csv -c titanic -m "My submission"
   ```

### Multi-source Data Utilization

```bash
# Main competition data
python scripts/download_data.py house-prices-advanced-regression-techniques --organize

# Additional datasets
python scripts/download_data.py --dataset username/additional-housing-data

# Reference notebooks
python scripts/download_data.py --notebook username/housing-price-eda
```

## Features

- **UV High-Speed Package Management**: Fast dependency resolution and installation
- **Kaggle API Integration**: Automated data downloading functionality
- **GPU Support**: CUDA-enabled PyTorch included by default
- **Complete Development Environment**: Jupyter Lab/Notebook and full development toolkit
- **Professional Configuration**: Well-organized project structure

## Notes

- Files in the `data/` directory are included in `.gitignore`
- Keep Kaggle API credentials secure
- Do not commit large data files to Git
- Initial setup takes time due to large packages (PyTorch, CUDA libraries)
- GPU-enabled PyTorch is installed by default; adjust if CUDA is not available

## Troubleshooting

### uv command not found
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Package installation interrupted
```bash
export PATH="$HOME/.local/bin:$PATH"
uv sync --reinstall
```

### Reset virtual environment
```bash
rm -rf .venv
bash scripts/setup_environment.sh
```

## Quick Start

1. Clone or download this template
2. Run `bash scripts/setup_environment.sh`
3. Configure Kaggle API credentials
4. Download your competition data
5. Start coding in Jupyter notebooks!