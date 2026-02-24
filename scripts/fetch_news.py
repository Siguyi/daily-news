#!/usr/bin/env python3
"""
AI 新闻抓取器
从多个来源抓取 AI 行业新闻
"""

import requests
from datetime import datetime, timedelta
from typing import List, Dict
import json
import re


class AINewsFetcher:
    """AI 新闻抓取器"""

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.news_sources = [
            {
                'name': 'TechCrunch',
                'url': 'https://techcrunch.com/category/artificial-intelligence/',
                'selector': 'article.post-block'
            },
            {
                'name': 'The Verge',
                'url': 'https://www.theverge.com/ai',
                'selector': 'article'
            },
            {
                'name': 'Hacker News',
                'url': 'https://hn.algolia.com/?q=AI',
                'selector': 'item'
            }
        ]

    def fetch_techcrunch(self) -> List[Dict]:
        """抓取 TechCrunch AI 新闻"""
        news = []
        try:
            response = requests.get(
                'https://techcrunch.com/wp-json/tc/v1/tc-archive-stream?category=artificial-intelligence&page=1',
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                for item in data[:10]:
                    news.append({
                        'title': item.get('title', ''),
                        'url': item.get('URL', ''),
                        'source': 'TechCrunch',
                        'published': item.get('date', '')
                    })
        except Exception as e:
            print(f"抓取 TechCrunch 失败: {e}")
        return news

    def fetch_hackernews(self, keyword: str = 'AI') -> List[Dict]:
        """抓取 Hacker News AI 相关新闻"""
        news = []
        try:
            response = requests.get(
                f'https://hn.algolia.com/api/v1/search_by_date?query={keyword}&tags=story&hitsPerPage=20',
                headers=self.headers,
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                cutoff_time = datetime.now() - timedelta(hours=24)

                for hit in data.get('hits', []):
                    created_at = datetime.fromisoformat(hit.get('created_at', '').replace('Z', '+00:00'))
                    if created_at.replace(tzinfo=None) > cutoff_time:
                        news.append({
                            'title': hit.get('title', ''),
                            'url': hit.get('url', f'https://news.ycombinator.com/item?id={hit.get("objectID")}'),
                            'source': 'Hacker News',
                            'published': hit.get('created_at', '')
                        })
        except Exception as e:
            print(f"抓取 Hacker News 失败: {e}")
        return news

    def fetch_all(self) -> List[Dict]:
        """从所有来源抓取新闻"""
        all_news = []

        # 优先使用 API 的来源
        all_news.extend(self.fetch_hackernews())

        # 去重
        seen = set()
        unique_news = []
        for item in all_news:
            title_lower = item['title'].lower()
            if title_lower not in seen:
                seen.add(title_lower)
                unique_news.append(item)

        return unique_news[:15]

    def filter_by_time(self, news: List[Dict], hours: int = 24) -> List[Dict]:
        """按时间过滤新闻"""
        cutoff_time = datetime.now() - timedelta(hours=hours)
        filtered = []

        for item in news:
            try:
                published = item.get('published', '')
                if published:
                    # 尝试解析多种日期格式
                    for fmt in ['%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%d %H:%M:%S']:
                        try:
                            dt = datetime.strptime(published[:19], fmt[:len(published[:19])])
                            if dt > cutoff_time:
                                filtered.append(item)
                            break
                        except:
                            continue
                else:
                    # 如果没有时间信息，保留
                    filtered.append(item)
            except:
                filtered.append(item)

        return filtered


def generate_summary(title: str, max_length: int = 100) -> str:
    """
    使用 Claude API 生成新闻摘要
    如果没有 API，可以使用简单的标题提取作为后备

    Args:
        title: 新闻标题
        max_length: 最大长度

    Returns:
        摘要文本
    """
    # 简单后备方案：清理标题作为摘要
    # 实际使用时应该调用 Claude API 生成更好的摘要

    # 移除括号内容
    summary = re.sub(r'\([^)]*\)', '', title)
    summary = re.sub(r'\[.*?\]', '', summary)
    summary = summary.strip()

    if len(summary) > max_length:
        summary = summary[:max_length-3] + '...'

    return summary


def main():
    """测试抓取功能"""
    fetcher = AINewsFetcher()
    print("🔍 正在抓取 AI 新闻...")

    news = fetcher.fetch_all()
    print(f"✅ 获取到 {len(news)} 条新闻")

    for i, item in enumerate(news[:5], 1):
        print(f"\n{i}. {item['title']}")
        print(f"   来源: {item['source']}")
        print(f"   链接: {item['url']}")


if __name__ == "__main__":
    main()
