"""
Module for extracting news articles from URLs.
Uses newspaper3k to handle various news site formats automatically.
"""
from newspaper import Article
from typing import Dict, Any, Optional


def extract_article(url: str) -> Dict[str, Any]:
    """
    Extract article content from a given URL.

    Args:
        url (str): URL of the news article to extract

    Returns:
        Dict containing article information:
        - title: Article headline
        - text: Full article text
        - url: Original article URL
        - publish_date: Publication date (if available)
        - authors: List of authors (if available)
    """
    try:
        # Create an Article object
        article = Article(url)

        # Download and parse the article
        article.download()
        article.parse()

        print(f"Article text length: {len(article.text)}")
        # Extract relevant information
        return {
            "title": article.title,
            "text": article.text,
            "url": url,
            "publish_date": article.publish_date,
            "authors": article.authors
        }
    except Exception as e:
        print(f"Error extracting article from {url}: {str(e)}")
        return {
            "title": None,
            "text": None,
            "url": url,
            "error": str(e)
        }