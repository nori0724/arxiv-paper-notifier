import sys
import os

# プロジェクトのルートパスを取得
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import datetime
import pytz
import feedparser
from config.settings import ARXIV_CATEGORIES, KEYWORD_SCORES, SCORE_THRESHOLD
from urllib.parse import quote

def get_papers_from_arxiv():
    base_url = "http://export.arxiv.org/api/query?"

    # 日本時間で前日の日付を取得
    today = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    yesterday = today - datetime.timedelta(days=1)
    date_query = yesterday.strftime("submittedDate:[%Y%m%d0000 TO %Y%m%d2359]")

    papers = []
    for category in ARXIV_CATEGORIES:
        search_query = quote(f"cat:{category}+AND+{date_query}")
        query_url = f"{base_url}search_query={search_query}&sortBy=submittedDate&sortOrder=descending"
        print(query_url)
        feed = feedparser.parse(query_url)

        if 'entries' not in feed:
            raise ValueError(f"No entries found for category {category}")

        for entry in feed.entries:
            paper = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "summary": entry.summary
            }

            # スコア計算
            total_score = 0
            hit_keywords = []
            for keyword, score in KEYWORD_SCORES.items():
                if keyword.lower() in paper['title'].lower() or keyword.lower() in paper['summary'].lower():
                    total_score += score
                    hit_keywords.append(keyword)

            # 閾値以上のスコアの場合、リストに追加
            if total_score >= SCORE_THRESHOLD:
                paper['score'] = total_score
                paper['hit_keywords'] = hit_keywords
                papers.append(paper)

    return papers

if __name__ == "__main__":
    papers = get_papers_from_arxiv()
    for paper in papers:
        print(paper["title"])