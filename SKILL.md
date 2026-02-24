---
name: siguyi-ai-daily
description: 为你精选每日最值得关注的 AI 行业资讯，让你用最少的时间掌握最新的行业动态。当用户想要获取每日 AI 新闻摘要、AI 行业动态、或者发送"今日AI报告"时触发此技能。
---

# 萍姐每日AI新闻概览

## Overview

为你精选每日最值得关注的 AI 行业资讯，让你用最少的时间掌握最新的行业动态。

## 触发指令

用户发送以下指令时启动：
- "今日AI报告"
- "萍姐 AI 日报"
- "每日 AI 新闻"
- "AI 行业动态"
- "今天的 AI 新闻"

## 工作流程

### Step 1: 确定日期

获取当天日期，格式化为中文日期：
- 例如：2026年2月24日 → 2026年2月24日 星期一

### Step 2: 抓取 AI 新闻

从以下权威来源收集近 24 小时内的 AI 领域重要新闻：

**主要新闻源：**
- TechCrunch AI 板块
- The Verge AI 板块
- Hacker News (AI 相关)
- 36氪 AI 板块
- 机器之心
- 量子位
- AI 科技评论

**搜索关键词：**
- Artificial Intelligence
- LLM / Large Language Model
- GPT / Claude / Gemini
- AI Model
- Machine Learning
- OpenAI / Anthropic / Google AI / Meta AI

### Step 3: 智能筛选

过滤标准：
1. **时间过滤**：只保留近 24 小时内的新闻
2. **质量过滤**：移除重复、转载、无实质内容的资讯
3. **价值过滤**：保留有技术突破、商业应用、行业趋势的资讯
4. **数量控制**：精选 8-12 条最具价值的新闻

### Step 4: 生成摘要

对每条资讯提炼：
- **标题**：保留原标题或生成吸引人的中文标题
- **核心要点**：50-100 字概括核心内容
- **关键词标签**：标注 2-4 个关键词
- **原文链接**：保留原始链接

### Step 5: 生成 HTML 页面

调用 `scripts/generate_report.py` 生成精美的 HTML 报告页面。

---

## 输出格式

生成的 HTML 页面要求：

1. **顶部标题**：「萍姐AI日报-[日期]」
2. **卡片式设计**：每条资讯独立卡片
3. **卡片内容**：
   - 关键词标签（彩色标签）
   - 新闻标题
   - 核心要点摘要
   - "查看原文" 链接按钮
4. **底部**：版权信息和生成时间

---

## 资源

### scripts/generate_report.py

生成 HTML 报告的核心脚本，需要实现：

```python
def generate_html_report(news_items: list, date: str) -> str:
    """
    生成 HTML 报告

    Args:
        news_items: 新闻列表，每项包含 title, summary, tags, url
        date: 日期字符串

    Returns:
        HTML 内容
    """
    # TODO: 实现 HTML 生成逻辑
    pass
```

### assets/template.html

HTML 模板文件，包含：
- 现代化的卡片式设计
- 响应式布局
- 优雅的配色方案
- 标签样式
- 按钮样式

---

## 输出示例

```
📰 萍姐AI日报 - 2026年2月24日 星期一

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[🔖 GPT-5] [🔖 OpenAI] [🔖 发布]
OpenAI 发布 GPT-5 预览版
OpenAI 今日发布了 GPT-5 预览版，该模型在推理能力和多模态理解方面有显著提升...

[🔖 Claude] [🔖 Anthropic] [🔖 企业版]
Anthropic 推出 Claude 企业版
Anthropic 宣布推出 Claude Enterprise，针对企业用户提供更强大的定制能力和安全特性...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📎 共 X 条资讯 | 生成时间: 2026-02-24 19:00
```

---

## 注意事项

1. 如果某些新闻源无法访问，使用备用源或搜索替代
2. 如果当天没有重大新闻，可以适当放宽筛选标准
3. 确保所有外部链接有效
4. 摘要必须使用简体中文
5. 关键词使用中文标签
