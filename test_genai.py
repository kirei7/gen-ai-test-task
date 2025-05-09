"""
Test script to verify GenAI processing capabilities.
"""
from scraper.extractor import extract_article
from genai.processor import process_article
from config import TEST_URLS


def main():
    """Test GenAI processing on sample articles."""
    print("Testing GenAI processing...\n")

    for i, url in enumerate(TEST_URLS):
        print(f"===== Processing Article {i + 1} =====")
        print(f"URL: {url}")

        # Extract the article
        print("Extracting article...")
        article = extract_article(url)

        if not article.get("text"):
            print(f"Error: Could not extract text from {url}")
            continue

        print(f"\nTitle: {article['title']}")
        text_preview = article['text'][:100] + "..." if article['text'] else "No text extracted"
        print(f"Text preview: {text_preview}")

        # Process the article with GenAI
        print("\nProcessing with GenAI...")
        processed_article = process_article(article)

        # Display results
        print("\nResults:")
        print(f"Summary: {processed_article['summary']}")
        print(f"Topics: {', '.join(processed_article['topics'])}")
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()