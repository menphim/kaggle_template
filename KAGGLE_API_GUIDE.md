# Kaggle API 利用ガイド

このガイドでは、Kaggle APIの全機能と実用的な使用例を説明します。

## 🔧 初期設定

### 1. API認証の設定
```bash
# 1. Kaggle.com → Account → API → Create New API Token
# 2. kaggle.jsonをダウンロード
# 3. 適切な場所に配置
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# 4. 認証確認
kaggle config view
```

### 2. 環境準備
```bash
# 仮想環境アクティベート
source .venv/bin/activate

# プロジェクト用スクリプト使用
python scripts/download_data.py --list
```

## 🏆 コンペティション操作

### 基本的なコンペティション操作
```bash
# コンペティション一覧
kaggle competitions list
kaggle competitions list --search "nlp"
kaggle competitions list --category "getting-started"

# 特定コンペの詳細
kaggle competitions files titanic
kaggle competitions leaderboard titanic
```

### データダウンロード
```bash
# 全ファイルダウンロード
kaggle competitions download titanic
python scripts/download_data.py titanic

# 特定ファイルのみ
kaggle competitions download titanic --file train.csv

# カスタム出力先
kaggle competitions download titanic -p data/competitions/titanic
python scripts/download_data.py titanic --output data/custom
```

### 提出とスコア確認
```bash
# 提出
kaggle competitions submit submission.csv -c titanic -m "XGBoost baseline model"

# 提出履歴
kaggle competitions submissions titanic

# リーダーボード
kaggle competitions leaderboard titanic --show
kaggle competitions leaderboard titanic --download
```

## 📊 データセット操作

### データセット検索・ダウンロード
```bash
# データセット検索
kaggle datasets list --search "housing"
kaggle datasets list --file-type "csv"
kaggle datasets list --size-range "1MB:100MB"

# ユーザー別データセット
kaggle datasets list --user "alexisbcook"

# ダウンロード
kaggle datasets download zillow/zecon
python scripts/download_data.py --dataset zillow/zecon

# 特定ファイルのみ
kaggle datasets download zillow/zecon --file State_time_series.csv
```

### データセット情報取得
```bash
# メタデータ取得
kaggle datasets metadata zillow/zecon
kaggle datasets files zillow/zecon

# ステータス確認
kaggle datasets status myusername/mydataset
```

### データセット作成・更新
```bash
# 新規データセット初期化
mkdir my-dataset
cd my-dataset
kaggle datasets init

# メタデータ編集後、作成
kaggle datasets create

# 新バージョン作成
kaggle datasets version -m "Updated with 2024 data"
```

## 📝 カーネル/ノートブック操作

### カーネル検索・取得
```bash
# カーネル検索
kaggle kernels list --search "tensorflow"
kaggle kernels list --language "python"
kaggle kernels list --user "dansbecker"

# カーネルダウンロード
kaggle kernels pull dansbecker/housing-prices-eda -p notebooks/housing-eda

# 出力ファイル取得
kaggle kernels output dansbecker/housing-prices-eda
kaggle kernels files dansbecker/housing-prices-eda
```

### カーネル作成・実行
```bash
# カーネル初期化
mkdir my-kernel
cd my-kernel
kaggle kernels init

# メタデータ設定後、実行
kaggle kernels push

# 実行ステータス確認
kaggle kernels status myusername/my-kernel-name
```

## 🤖 モデル操作

### モデル検索・取得
```bash
# モデル検索
kaggle models list --search "bert"
kaggle models instances list --search "classification"

# モデル詳細取得
kaggle models get google/bert

# モデルダウンロード
kaggle models instances versions download google/bert/tf2/1
```

### モデル作成・管理
```bash
# モデル初期化
kaggle models init -p my-model/

# モデル作成
kaggle models create

# インスタンス作成
kaggle models instances create

# バージョン作成
kaggle models instances versions create -p my-model/
```

## ⚙️ 設定管理

### 基本設定
```bash
# 現在の設定確認
kaggle config view

# プロキシ設定
kaggle config set -n proxy -v http://proxy.company.com:8080

# デフォルトダウンロードパス
kaggle config set -n path -v "/custom/download/path"

# 設定削除
kaggle config unset -n proxy
```

## 🛠️ 実用的な使用例

### 1. コンペ参加の典型的ワークフロー
```bash
# 1. コンペ検索・選択
kaggle competitions list --search "tabular"

# 2. データダウンロード
python scripts/download_data.py house-prices-advanced-regression-techniques

# 3. 既存カーネル参考
kaggle kernels list --search "house prices" --sort-by "voteCount"
kaggle kernels pull example-user/house-prices-eda -p notebooks/reference

# 4. 提出
kaggle competitions submit submission.csv -c house-prices-advanced-regression-techniques -m "Random Forest baseline"

# 5. 結果確認
kaggle competitions submissions house-prices-advanced-regression-techniques
```

### 2. データセット活用
```bash
# 関連データセット検索
kaggle datasets list --search "real estate"

# 複数データセット一括取得
python scripts/download_data.py --dataset username/housing-extra-features
python scripts/download_data.py --dataset username/economic-indicators

# 外部データ統合後、新データセット作成
kaggle datasets init -p data/processed/combined-housing
# メタデータ編集後
kaggle datasets create -p data/processed/combined-housing
```

### 3. 学習・参考カーネル活用
```bash
# トップカーネル取得
kaggle kernels list --competition titanic --sort-by "voteCount" | head -5

# 複数の参考カーネルダウンロード
kaggle kernels pull user1/titanic-eda -p notebooks/reference/eda
kaggle kernels pull user2/titanic-feature-engineering -p notebooks/reference/features
kaggle kernels pull user3/titanic-ensemble -p notebooks/reference/models
```

### 4. バッチ処理スクリプト例
```bash
#!/bin/bash
# 複数コンペのデータ一括ダウンロード
competitions=("titanic" "house-prices-advanced-regression-techniques" "spaceship-titanic")

for comp in "${competitions[@]}"; do
    echo "Downloading $comp..."
    python scripts/download_data.py "$comp"
done
```

## 📋 コマンドクイックリファレンス

| 操作 | コマンド |
|------|----------|
| コンペ一覧 | `kaggle competitions list` |
| データダウンロード | `python scripts/download_data.py [comp_name]` |
| 提出 | `kaggle competitions submit [file] -c [comp] -m "[message]"` |
| データセット検索 | `kaggle datasets list --search "[keyword]"` |
| カーネル検索 | `kaggle kernels list --search "[keyword]"` |
| 設定確認 | `kaggle config view` |

## 🚨 トラブルシューティング

### よくあるエラーと解決法

```bash
# 認証エラー
# → kaggle.jsonの場所・権限確認
ls -la ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json

# ダウンロードエラー
# → コンペ/データセット名確認
kaggle competitions list --search "[partial_name]"

# 提出エラー
# → ファイル形式・サイズ確認
kaggle competitions files [competition_name]

# API制限エラー
# → 一定時間待機後再実行
sleep 60 && kaggle competitions list
```

## 🔗 参考リンク

- [Kaggle API Documentation](https://github.com/Kaggle/kaggle-api)
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Kaggle Learn](https://www.kaggle.com/learn)