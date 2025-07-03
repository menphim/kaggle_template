#!/usr/bin/env python3
"""
Kaggle dataset download script
Usage: python scripts/download_data.py [competition_name]
"""

import os
import sys
import argparse
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi


def setup_kaggle_api():
    """Setup Kaggle API authentication"""
    api = KaggleApi()
    
    # Check if kaggle.json exists
    kaggle_config_path = Path.home() / ".kaggle" / "kaggle.json"
    if not kaggle_config_path.exists():
        print("Error: kaggle.json not found!")
        print("Please download kaggle.json from https://www.kaggle.com/settings/account")
        print(f"and place it at {kaggle_config_path}")
        sys.exit(1)
    
    # Set proper permissions
    os.chmod(kaggle_config_path, 0o600)
    
    try:
        api.authenticate()
        print("Kaggle API authentication successful!")
        return api
    except Exception as e:
        print(f"Error authenticating with Kaggle API: {e}")
        sys.exit(1)


def download_competition_data(api, competition_name, download_path="data/raw", organize=False):
    """Download competition data"""
    if organize:
        # Create organized folder structure
        competition_path = Path("data/competitions") / competition_name
        competition_path.mkdir(parents=True, exist_ok=True)
        download_path = str(competition_path)
    else:
        Path(download_path).mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"Downloading competition data for: {competition_name}")
        api.competition_download_files(
            competition_name, 
            path=download_path
        )
        
        # Unzip downloaded files
        import zipfile
        zip_path = Path(download_path) / f"{competition_name}.zip"
        if zip_path.exists():
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(download_path)
            print(f"Files extracted to {download_path}")
        print(f"Data downloaded successfully to {download_path}")
        
        if organize:
            print(f"💡 Tip: Use 'data/competitions/{competition_name}/' as your data path in notebooks")
            
    except Exception as e:
        print(f"Error downloading competition data: {e}")
        sys.exit(1)


def download_dataset(api, dataset_name, download_path="data/external"):
    """Download dataset"""
    Path(download_path).mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"Downloading dataset: {dataset_name}")
        api.dataset_download_files(
            dataset_name, 
            path=download_path
        )
        
        # Unzip downloaded files
        import zipfile
        zip_files = list(Path(download_path).glob("*.zip"))
        for zip_path in zip_files:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(download_path)
            print(f"Files extracted from {zip_path.name}")
        print(f"Dataset downloaded successfully to {download_path}")
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        sys.exit(1)


def download_notebook(api, notebook_ref, download_path="notebooks/reference"):
    """Download Kaggle notebook"""
    Path(download_path).mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"Downloading notebook: {notebook_ref}")
        api.kernels_pull(notebook_ref, path=download_path)
        print(f"Notebook downloaded successfully to {download_path}")
        print(f"💡 Tip: Modify data paths in the notebook to match your local structure")
    except Exception as e:
        print(f"Error downloading notebook: {e}")
        sys.exit(1)


def list_competitions():
    """List available competitions"""
    api = setup_kaggle_api()
    competitions = api.competitions_list()
    
    print("Available competitions:")
    for comp in competitions[:10]:  # Show first 10
        print(f"- {comp.ref}: {comp.title}")


def list_notebooks_for_competition(api, competition_name):
    """List popular notebooks for a competition"""
    try:
        print(f"Popular notebooks for {competition_name}:")
        notebooks = api.kernels_list(competition=competition_name)
        for nb in notebooks[:5]:  # Show top 5
            print(f"- {nb.ref}: {nb.title} (votes: {nb.totalVotes})")
    except Exception as e:
        print(f"Error listing notebooks: {e}")


def main():
    parser = argparse.ArgumentParser(description="Download Kaggle competition data, datasets, and notebooks")
    parser.add_argument("competition", nargs="?", help="Competition name")
    parser.add_argument("--dataset", help="Dataset name (format: username/dataset-name)")
    parser.add_argument("--notebook", help="Notebook reference (format: username/notebook-name)")
    parser.add_argument("--list", action="store_true", help="List available competitions")
    parser.add_argument("--list-notebooks", help="List popular notebooks for competition")
    parser.add_argument("--output", default="data/raw", help="Output directory")
    parser.add_argument("--organize", action="store_true", help="Organize data in competition-specific folders")
    
    args = parser.parse_args()
    
    if args.list:
        list_competitions()
        return
    
    api = setup_kaggle_api()
    
    if args.list_notebooks:
        list_notebooks_for_competition(api, args.list_notebooks)
        return
    
    if args.dataset:
        download_dataset(api, args.dataset, args.output)
    elif args.notebook:
        download_notebook(api, args.notebook, args.output if args.output != "data/raw" else "notebooks/reference")
    elif args.competition:
        download_competition_data(api, args.competition, args.output, args.organize)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()