# Arxiv Paper Notifier

## 概要
Arxiv Paper Notifierは、指定した分野やキーワードに関するarXivの論文を取得し、LINEに通知するアプリケーションです。

## 動作環境
- Python 3.8

## インストール方法
1. 本リポジトリをクローン
``` shell
git clone https://github.com/username/arxiv-paper-notifier.git
```
2. 依存パッケージのインストール
``` shell
$ cd arxiv-paper-notifier
$ pip install -r requirements.txt
```
3. LINEのチャネルアクセストークンとチャネルシークレットを環境変数に設定
``` shell
export LINE_CHANNEL_ACCESS_TOKEN='<Your Channel Access Token>'
export LINE_CHANNEL_SECRET='<Your Channel Secret>'
export LINE_USER_ID="your_line_user_id"
``` 
## 設定方法
1. `config/settings.py`を編集  
``` python
# 検索カテゴリー (収集するArxivのカテゴリーをリスト形式で指定します。)
ARXIV_CATEGORIES = [
    "cs.CV",
    "cs.CL",
    "cs.NE",
    "cs.LG",
    "cs.RO",
    "cs.AI",
    "stat.ML",
]

# 検索キーワードとスコア (通知するキーワードと、そのキーワードがヒットした場合に加算されるスコアを指定します。)
KEYWORD_SCORES = {
    "nerf": 3,
}

# 通知の閾値 (通知する論文のスコアの閾値を指定します。)
SCORE_THRESHOLD = 3
``` 
2. `src/arxiv_api.py`を編集
`ARXIV_CATEGORIES`と`KEYWORD_SCORES`を編集して、通知したいカテゴリーとキーワードを指定してください。

3. `src/line_notifier.py`を編集
通知メッセージの形式を変更したい場合、`create_message`を編集してください。

## 実行方法
``` shell
python src/line_notifier.py
```