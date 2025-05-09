"""
Test script to verify the article extraction functionality.
"""
from scraper.extractor import extract_article
from config import TEST_URLS


def main():
    """Test article extraction on sample URLs."""
    print("Testing article extraction...")

    for url in TEST_URLS:
        print(f"\nProcessing: {url}")
        article_data = extract_article(url)

        # Print article info
        print(f"Title: {article_data['title']}")

        # Print first 150 characters of text as preview
        text_preview = article_data.get('text', '')[:150].replace('\n', ' ').strip()
        print(f"Text preview: {text_preview}...")

        # Print other metadata
        print(f"Authors: {article_data.get('authors', [])}")
        print(f"Publish date: {article_data.get('publish_date')}")

        if 'error' in article_data:
            print(f"Error: {article_data['error']}")


if __name__ == "__main__":
    main()