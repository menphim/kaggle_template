# Kaggle Competition Template

UVとKaggle APIを使用したKaggleコンペティション用のテンプレートプロジェクト。

## セットアップ

### 1. 環境の初期化

```bash
# セットアップスクリプトを実行
bash scripts/setup_environment.sh

# 仮想環境をアクティベート
source .venv/bin/activate
```

### 2. Kaggle APIの設定

1. [Kaggle Account](https://www.kaggle.com/settings/account)からkaggle.jsonをダウンロード
2. `~/.kaggle/kaggle.json`に配置
3. 権限を設定: `chmod 600 ~/.kaggle/kaggle.json`

## 使用方法

### データのダウンロード

```bash
# コンペティションデータのダウンロード
python scripts/download_data.py [competition-name]

# データセットのダウンロード
python scripts/download_data.py --dataset [username/dataset-name]

# 利用可能なコンペティション一覧
python scripts/download_data.py --list
```

### Jupyter Notebookの起動

```bash
jupyter notebook
```

## プロジェクト構造

```
kaggle-template/
├── data/
│   ├── raw/          # 生データ
│   ├── processed/    # 前処理済みデータ
│   └── external/     # 外部データセット
├── notebooks/        # Jupyter notebooks
├── models/           # 学習済みモデル
├── output/           # 提出ファイル
├── logs/             # ログファイル
├── scripts/          # ユーティリティスクリプト
├── pyproject.toml    # プロジェクト設定
└── README.md
```

## 主な依存関係

- **データ処理**: pandas, numpy, scipy
- **機械学習**: scikit-learn, xgboost, lightgbm, catboost
- **深層学習**: torch, transformers
- **可視化**: matplotlib, seaborn, plotly
- **API**: kaggle
- **最適化**: optuna

## 開発用ツール

開発用パッケージをインストール:

```bash
uv pip install -e ".[dev]"
```

コードフォーマット:

```bash
black .
isort .
```

## 使用例

1. 新しいコンペティションを開始:
   ```bash
   python scripts/download_data.py titanic
   ```

2. Jupyter notebookでEDAを開始:
   ```bash
   jupyter notebook
   ```

3. モデルの訓練と提出ファイルの生成を行う

## 注意事項

- `data/`ディレクトリ内のファイルは`.gitignore`に含まれています
- Kaggle APIの認証情報は安全に管理してください
- 大きなデータファイルはGitにコミットしないでください