#!/usr/bin/env python3
"""
萍姐AI日报 - 报告生成器
生成精美的 HTML 格式 AI 新闻日报
"""

from datetime import datetime
from typing import List, Dict
import json


def generate_html_report(news_items: List[Dict], date: str) -> str:
    """
    生成 HTML 报告

    Args:
        news_items: 新闻列表，每项包含 title, summary, tags, url, source
        date: 日期字符串

    Returns:
        HTML 内容
    """
    # 标签颜色映射
    tag_colors = {
        'GPT': '#10a37f',
        'Claude': '#d97706',
        'OpenAI': '#412a88',
        'Anthropic': '#d97706',
        'Google': '#4285f4',
        'Meta': '#0668e1',
        'Microsoft': '#00a4ef',
        'Amazon': '#ff9900',
        'Apple': '#555555',
        '发布': '#ef4444',
        '产品': '#8b5cf6',
        '融资': '#10b981',
        '研究': '#3b82f6',
        '技术': '#f59e0b',
        '行业': '#6366f1',
    }

    def get_tag_color(tag: str) -> str:
        return tag_colors.get(tag, '#6b7280')

    tags_html = ''
    for item in news_items:
        tags = item.get('tags', [])
        tags_html += f'''
        <div class="news-card">
            <div class="tags">'''

        for tag in tags:
            color = get_tag_color(tag)
            tags_html += f'''
                <span class="tag" style="background-color: {color};">{tag}</span>'''

        tags_html += f'''
            </div>
            <h3 class="news-title">{item['title']}</h3>
            <p class="news-summary">{item['summary']}</p>
            <div class="news-meta">
                <span class="source">📰 {item.get('source', '来源')}</span>
                <a href="{item['url']}" target="_blank" class="read-more">查看原文 →</a>
            </div>
        </div>'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>萍姐AI日报 - {date}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        .header h1 {{
            color: white;
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }}
        .header .date {{
            color: rgba(255,255,255,0.9);
            font-size: 1.2rem;
        }}
        .news-card {{
            background: white;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .news-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        }}
        .tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 12px;
        }}
        .tag {{
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        .news-title {{
            color: #1f2937;
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 12px;
            line-height: 1.5;
        }}
        .news-summary {{
            color: #4b5563;
            font-size: 0.95rem;
            line-height: 1.7;
            margin-bottom: 16px;
        }}
        .news-meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .source {{
            color: #6b7280;
            font-size: 0.85rem;
        }}
        .read-more {{
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            transition: color 0.2s;
        }}
        .read-more:hover {{
            color: #764ba2;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            color: rgba(255,255,255,0.8);
            font-size: 0.9rem;
        }}
        .stats {{
            background: rgba(255,255,255,0.2);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 30px;
            text-align: center;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📰 萍姐AI日报</h1>
            <p class="date">{date}</p>
        </div>

        <div class="stats">
            今日精选 {len(news_items)} 条 AI 行业资讯
        </div>

        <div class="news-list">
            {tags_html}
        </div>

        <div class="footer">
            <p>由 Claude AI 自动整理 | 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>'''

    return html


def fetch_ai_news() -> List[Dict]:
    """
    抓取 AI 新闻
    这里使用模拟数据，实际使用时需要接入真实新闻源

    Returns:
        新闻列表
    """
    # 模拟新闻数据
    # 实际使用时需要从新闻源抓取
    news_items = []

    # 可以使用以下方式接入真实数据：
    # 1. RSS 订阅
    # 2. 新闻 API (如 NewsAPI)
    # 3. 网页爬虫

    return news_items


def generate_markdown_report(news_items: List[Dict], date: str) -> str:
    """
    生成 Markdown 报告

    Args:
        news_items: 新闻列表
        date: 日期字符串

    Returns:
        Markdown 内容
    """
    md = f"""# 📰 萍姐AI日报 - {date}

> 今日精选 {len(news_items)} 条 AI 行业资讯

---

"""

    for i, item in enumerate(news_items, 1):
        tags = item.get('tags', [])
        tags_str = ' '.join([f'`{tag}`' for tag in tags])

        md += f"""### {i}. {item['title']}

**标签**: {tags_str}

{item['summary']}

**来源**: {item.get('source', '未知')} | [查看原文]({item['url']})

---

"""

    md += f"""
---
*由 Claude AI 自动整理 | 数据来源: Hacker News*
"""
    return md


def save_markdown_report(md: str, filepath: str = None) -> str:
    """
    保存 Markdown 报告到文件

    Args:
        md: Markdown 内容
        filepath: 文件路径，默认使用日期命名

    Returns:
        保存的文件路径
    """
    if filepath is None:
        date_str = datetime.now().strftime('%Y%m%d')
        filepath = f'ai-daily-{date_str}.md'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)

    return filepath


def save_html_report(html: str, filepath: str = None) -> str:
    """
    保存 HTML 报告到文件

    Args:
        html: HTML 内容
        filepath: 文件路径，默认使用日期命名

    Returns:
        保存的文件路径
    """
    if filepath is None:
        date_str = datetime.now().strftime('%Y%m%d')
        filepath = f'ai-daily-{date_str}.html'

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    return filepath


def generate_and_save_all(news_items: List[Dict], date: str = None, output_dir: str = '.') -> dict:
    """
    生成并保存 HTML 和 Markdown 报告

    Args:
        news_items: 新闻列表
        date: 日期字符串
        output_dir: 输出目录

    Returns:
        包含生成文件路径的字典
    """
    if date is None:
        date = datetime.now().strftime('%Y年%m月%d日 %A')

    date_str = datetime.now().strftime('%Y%m%d')

    # 生成 HTML
    html = generate_html_report(news_items, date)
    html_path = f'{output_dir}/ai-daily-{date_str}.html'
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    # 生成 Markdown
    md = generate_markdown_report(news_items, date)
    md_path = f'{output_dir}/ai-daily-{date_str}.md'
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md)

    return {'html': html_path, 'markdown': md_path}


def main():
    """测试用主函数"""
    # 模拟新闻数据
    sample_news = [
        {
            'title': 'OpenAI 发布 GPT-5 预览版，带来显著性能提升',
            'summary': 'OpenAI 今日发布了 GPT-5 预览版，该模型在推理能力、多模态理解和代码生成方面有显著提升。新版本支持更长的上下文窗口，并引入了改进的指令跟随能力。',
            'tags': ['GPT', 'OpenAI', '发布', '产品'],
            'url': 'https://openai.com/blog',
            'source': 'OpenAI Blog'
        },
        {
            'title': 'Anthropic 推出 Claude Enterprise 企业版',
            'summary': 'Anthropic 宣布推出 Claude Enterprise，针对企业用户提供更强大的定制能力、优先访问权限和增强的安全特性，支持私有化部署选项。',
            'tags': ['Claude', 'Anthropic', '产品', '企业'],
            'url': 'https://anthropic.com',
            'source': 'Anthropic'
        },
        {
            'title': 'Google 发布 Gemini 2.5 Pro，提升推理能力',
            'summary': 'Google DeepMind 发布了 Gemini 2.5 Pro，在数学推理和代码任务上创下新纪录，同时增强了多模态理解能力。',
            'tags': ['Google', 'Gemini', '发布', '技术'],
            'url': 'https://blog.google/technology/ai/',
            'source': 'Google AI Blog'
        },
    ]

    date_str = datetime.now().strftime('%Y年%m月%d日 %A')

    html = generate_html_report(sample_news, date_str)

    # 保存报告
    filepath = save_html_report(html)
    print(f"✅ 报告已生成: {filepath}")

    # 打印 HTML 内容
    print("\n" + "="*50)
    print("HTML 报告预览:")
    print("="*50)
    print(html[:1000] + "...")


if __name__ == "__main__":
    main()
