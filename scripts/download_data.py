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


def download_competition_data(api, competition_name, download_path="data/raw"):
    """Download competition data"""
    Path(download_path).mkdir(parents=True, exist_ok=True)
    
    try:
        print(f"Downloading competition data for: {competition_name}")
        api.competition_download_files(
            competition_name, 
            path=download_path, 
            unzip=True
        )
        print(f"Data downloaded successfully to {download_path}")
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
            path=download_path, 
            unzip=True
        )
        print(f"Dataset downloaded successfully to {download_path}")
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        sys.exit(1)


def list_competitions():
    """List available competitions"""
    api = setup_kaggle_api()
    competitions = api.competitions_list()
    
    print("Available competitions:")
    for comp in competitions[:10]:  # Show first 10
        print(f"- {comp.ref}: {comp.title}")


def main():
    parser = argparse.ArgumentParser(description="Download Kaggle competition data")
    parser.add_argument("competition", nargs="?", help="Competition name")
    parser.add_argument("--dataset", help="Dataset name (format: username/dataset-name)")
    parser.add_argument("--list", action="store_true", help="List available competitions")
    parser.add_argument("--output", default="data/raw", help="Output directory")
    
    args = parser.parse_args()
    
    if args.list:
        list_competitions()
        return
    
    api = setup_kaggle_api()
    
    if args.dataset:
        download_dataset(api, args.dataset, args.output)
    elif args.competition:
        download_competition_data(api, args.competition, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()