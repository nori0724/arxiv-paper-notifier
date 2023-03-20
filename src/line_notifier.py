import sys
import os

# プロジェクトのルートパスを取得
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from config.settings import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET
from src.arxiv_api import get_papers_from_arxiv

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

def send_papers_to_line(papers, user_id):
    for paper in papers:
        try:
            message = f"Title: {paper['title']}\n" \
                      f"Score: {paper['score']}\n" \
                      f"Hit Keywords: {', '.join(paper['hit_keywords'])}\n" \
                      f"Link: {paper['link']}\n" \
                      f"Published: {paper['published']}\n\n" \
                      f"Abstract:\n{paper['summary']}"

            line_bot_api.push_message(user_id, TextSendMessage(text=message))
        except LineBotApiError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # 環境変数からLINEのユーザーIDを取得
    user_id = os.environ.get("LINE_USER_ID")
    
    if user_id is None:
        print("Error: LINE_USER_ID is not set.")
        exit(1)

    # arXivから論文を取得
    papers = get_papers_from_arxiv()
    
    # 閾値以上のスコアの論文をLINEに通知
    send_papers_to_line(papers, user_id)