# Kaggle Competition Template

UVとKaggle APIを使用したKaggleコンペティション用のテンプレートプロジェクト。

## セットアップ

### 前提条件

- Python 3.10以上
- インターネット接続（初回セットアップ時）
- Kaggleアカウント

### 1. 環境の初期化

```bash
# セットアップスクリプトを実行（初回は5-10分程度かかります）
bash scripts/setup_environment.sh

# 仮想環境をアクティベート
source .venv/bin/activate

# またはuvを直接使用する場合：
export PATH="$HOME/.local/bin:$PATH"
uv sync
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
# 仮想環境をアクティベート後
source .venv/bin/activate

# Jupyter Notebookを起動
jupyter notebook

# またはJupyter Labを起動
jupyter lab
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

- **データ処理**: pandas 2.3.0, numpy 2.3.1, scipy 1.16.0
- **機械学習**: scikit-learn 1.7.0, xgboost 3.0.2, lightgbm 4.6.0, catboost 1.2.8
- **深層学習**: PyTorch 2.7.1+cu126, torchvision 0.22.1, transformers 4.53.0
- **可視化**: matplotlib 3.10.3, seaborn 0.13.2, plotly 6.2.0
- **開発環境**: Jupyter Lab 4.4.4, Jupyter Notebook 7.4.4
- **API**: kaggle 1.7.4.5
- **最適化**: optuna 4.4.0
- **その他**: tqdm, joblib など

## 開発用ツール

開発用パッケージをインストール:

```bash
# uvを使用する場合（推奨）
export PATH="$HOME/.local/bin:$PATH"
uv sync --group dev

# または従来の方法
pip install -e ".[dev]"
```

コードフォーマット:

```bash
# コードフォーマット実行
black .
isort .

# コード品質チェック
flake8 .

# テスト実行
pytest
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

## 特徴

- **UV高速パッケージ管理**: 依存関係の高速解決とインストール
- **Kaggle API統合**: データの自動ダウンロード機能
- **GPU対応**: CUDA対応PyTorchを標準搭載
- **完全な開発環境**: Jupyter Lab/Notebook、開発ツール一式
- **プロ仕様の構成**: 整理されたプロジェクト構造

## 注意事項

- `data/`ディレクトリ内のファイルは`.gitignore`に含まれています
- Kaggle APIの認証情報は安全に管理してください
- 大きなデータファイルはGitにコミットしないでください
- 初回セットアップ時は大きなパッケージ（PyTorch、CUDA等）のダウンロードのため時間がかかります
- GPU版PyTorchがインストールされているため、CUDA環境でない場合は適宜調整してください

## トラブルシューティング

### uvが見つからない場合
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### パッケージのインストールが途中で止まった場合
```bash
export PATH="$HOME/.local/bin:$PATH"
uv sync --reinstall
```

### 仮想環境のリセット
```bash
rm -rf .venv
bash scripts/setup_environment.sh
```

## クイックスタート

1. このテンプレートをクローンまたはダウンロード
2. `bash scripts/setup_environment.sh`を実行
3. Kaggle API認証情報を設定
4. コンペティションデータをダウンロード
5. Jupyter notebookでコーディング開始！