"""
Test script for the vector database functionality.
"""
from scraper.extractor import extract_article
from genai.processor import process_article
from database.vector_store import store_article, get_all_articles, delete_all_articles
from config import TEST_URLS


def main():
    """Test vector database operations."""
    print("Testing Vector Database...\n")

    # Clear existing data (optional)
    print("Clearing existing data...")
    delete_all_articles()

    # Process articles and store in vector DB
    for i, url in enumerate(TEST_URLS):
        print(f"\n===== Processing Article {i + 1} =====")

        # Extract article
        print(f"Extracting: {url}")
        article = extract_article(url)

        if not article.get("text"):
            print(f"Error: Could not extract article from {url}")
            continue

        print(f"Extracted: {article['title']}")

        # Process with GenAI
        print("Generating summary and topics...")
        processed_article = process_article(article)

        # Store in vector DB
        print("Storing in vector database...")
        success = store_article(processed_article)

        if success:
            print(f"Successfully stored article: {processed_article['title']}")
        else:
            print(f"Failed to store article: {processed_article.get('title', 'Unknown')}")

    # Retrieve all articles
    print("\n===== Retrieving All Articles =====")
    results = get_all_articles()

    if results and results['ids']:
        print(f"Found {len(results['ids'])} articles in the database:")
        for i, (id, doc, metadata) in enumerate(zip(results['ids'], results['documents'], results['metadatas'])):
            print(f"\nArticle {i + 1}:")
            print(f"ID: {id}")
            print(f"Title: {metadata['title']}")
            print(f"URL: {metadata['url']}")
            print(f"Topics: {metadata['topics']}")
    else:
        print("No articles found in the database")


if __name__ == "__main__":
    main()