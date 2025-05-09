"""
Test script for the semantic search functionality.
"""
from scraper.extractor import extract_article
from genai.processor import process_article
from database.vector_store import store_article, delete_all_articles
from search.semantic_search import semantic_search
from config import TEST_URLS, TEST_QUERIES


def setup_test_data():
    """Prepare test data for search."""
    print("Setting up test data...")

    # Clear existing data
    delete_all_articles()

    # Process and store all test articles
    for url in TEST_URLS:
        article = extract_article(url)
        if article.get("text"):
            processed = process_article(article)
            store_article(processed)

    print("Test data setup complete.\n")


def test_search():
    """Test basic semantic search."""
    print("===== Testing Basic Semantic Search =====")

    for query in TEST_QUERIES:
        print(f"\nSearching for: '{query}'")
        results = semantic_search(query)

        if results:
            print(f"Found {len(results)} results:")
            for i, result in enumerate(results):
                print(f"\n  Result {i + 1}:")
                print(f"  Title: {result['title']}")
                print(f"  URL: {result['url']}")
                print(f"  Topics: {', '.join(result['topics'])}")
                if result.get('relevance_score') is not None:
                    print(f"  Relevance: {result['relevance_score']:.2f}")
        else:
            print("No results found.")


def main():
    """Run search tests."""
    # Setup test data first
    setup_test_data()

    # Run search tests
    test_search()

if __name__ == "__main__":
    main()