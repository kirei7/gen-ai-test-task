"""
Module for managing the vector database using Chroma.
Handles storing and retrieving embeddings for semantic search.
"""
import os
import chromadb
from chromadb.errors import NotFoundError
from chromadb.utils import embedding_functions
from langchain_openai import OpenAIEmbeddings
from typing import Dict, Any
from config import OPENAI_API_KEY, VECTOR_DB_PATH

# Create directory for vector DB if it doesn't exist
os.makedirs(VECTOR_DB_PATH, exist_ok=True)

# Initialize the ChromaDB client
client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

# Use OpenAI embeddings
embedding_function = OpenAIEmbeddings(api_key=OPENAI_API_KEY)


def get_or_create_collection(collection_name: str = "news_articles"):
    """
    Get or create a collection in the vector database.

    Args:
        collection_name: Name of the collection

    Returns:
        The collection object
    """
    try:
        # Try to get an existing collection
        collection = client.get_collection(
            name=collection_name,
            embedding_function=embedding_functions.OpenAIEmbeddingFunction(
                api_key=OPENAI_API_KEY,
                model_name="text-embedding-ada-002"
            )
        )
        print(f"Using existing collection: {collection_name}")
        return collection
    except NotFoundError:
        # Create a new collection if it doesn't exist
        collection = client.create_collection(
            name=collection_name,
            embedding_function=embedding_functions.OpenAIEmbeddingFunction(
                api_key=OPENAI_API_KEY,
                model_name="text-embedding-ada-002"
            )
        )
        print(f"Created new collection: {collection_name}")
        return collection


def store_article(processed_article: Dict[str, Any], collection_name: str = "news_articles"):
    """
    Store a processed article in the vector database.

    Args:
        processed_article: Article with summary and topics
        collection_name: Name of the collection to store in
    """
    # Get the collection
    collection = get_or_create_collection(collection_name)

    # Create a unique ID for the article based on URL
    import hashlib
    article_id = hashlib.md5(processed_article["url"].encode()).hexdigest()

    # Prepare the content to be embedded - combine relevant text
    content = f"""
    Title: {processed_article.get('title', '')}

    Summary: {processed_article.get('summary', '')}

    Topics: {', '.join(processed_article.get('topics', []))}
    """

    # Create metadata to store additional information
    metadata = {
        "title": processed_article.get("title", ""),
        "url": processed_article.get("url", ""),
        "publish_date": str(processed_article.get("publish_date", "")),
        "topics": ", ".join(processed_article.get("topics", [])),
    }

    # Add the document to the collection
    try:
        collection.add(
            ids=[article_id],
            documents=[content],
            metadatas=[metadata]
        )
        print(f"Stored article in vector DB: {processed_article.get('title')}")
        return True
    except Exception as e:
        print(f"Error storing article: {e}")
        return False


def get_all_articles(collection_name: str = "news_articles"):
    """
    Retrieve all articles from the vector database.

    Args:
        collection_name: Name of the collection

    Returns:
        List of all stored articles with metadata
    """
    collection = get_or_create_collection(collection_name)
    return collection.get()


def delete_all_articles(collection_name: str = "news_articles"):
    """
    Delete all articles from the vector database.

    Args:
        collection_name: Name of the collection
    """
    try:
        client.delete_collection(collection_name)
        print(f"Deleted collection: {collection_name}")
        return True
    except Exception as e:
        print(f"Error deleting collection: {e}")
        return False