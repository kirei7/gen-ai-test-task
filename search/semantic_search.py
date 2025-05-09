"""
Module for semantic search functionality.
Enables natural language queries against the vector database.
"""
from database.vector_store import get_or_create_collection
from typing import List, Dict, Any


def semantic_search(query: str,
                    collection_name: str = "news_articles",
                    limit: int = 5) -> List[Dict[str, Any]]:
    """
    Perform semantic search on stored articles.

    Args:
        query: The search query text
        collection_name: Name of the collection to search in
        limit: Maximum number of results to return

    Returns:
        List of articles matching the search query
    """
    # Get the collection
    collection = get_or_create_collection(collection_name)

    # Query the collection
    try:
        results = collection.query(
            query_texts=[query],
            n_results=limit
        )

        # Format the results
        formatted_results = []
        print(f"Distances: {results['distances']}")
        if results and results['ids'] and len(results['ids'][0]) > 0:
            for i in range(len(results['ids'][0])):
                # Get the document and metadata for this result
                doc_id = results['ids'][0][i]
                document = results['documents'][0][i]
                metadata = results['metadatas'][0][i]
                distance = results.get('distances', [[]])[0][i] if 'distances' in results else None

                # Format the result
                result = {
                    'id': doc_id,
                    'title': metadata.get('title', ''),
                    'url': metadata.get('url', ''),
                    'topics': metadata.get('topics', '').split(', '),
                    'relevance_score': 1 - distance if distance is not None else None,
                    'document': document
                }
                formatted_results.append(result)

        return formatted_results

    except Exception as e:
        print(f"Error performing semantic search: {e}")
        return []