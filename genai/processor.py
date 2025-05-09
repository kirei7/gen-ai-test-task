"""
Module for processing articles with GenAI capabilities.
Uses LangChain and OpenAI to summarize text and extract topics.
"""
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from typing import Dict, List, Any
from config import OPENAI_API_KEY, DEFAULT_MODEL, LLM_TEMPERATURE, MAX_TEXT_SIZE

# Initialize the OpenAI model
llm = ChatOpenAI(
    name=DEFAULT_MODEL,
    temperature=LLM_TEMPERATURE,
    api_key=OPENAI_API_KEY
)


def generate_summary(article: Dict[str, Any]) -> str:
    """
    Generate a concise summary of the article using GenAI.

    Args:
        article (Dict): Article data including title and text

    Returns:
        str: A summary of the article
    """
    # Skip if no text
    if not article.get('text'):
        return "Unable to generate summary: No article text available."

    # Create a prompt template
    summary_template = """
    You are an expert news summarizer. Create a concise summary of the following news article.
    The summary should capture the main points and key information.
    Keep the summary to about 3-5 sentences.

    TITLE: {title}

    ARTICLE: {text}

    SUMMARY:
    """

    prompt = ChatPromptTemplate.from_template(summary_template)

    # Create the chain and run it
    chain = prompt | llm
    try:
        response = chain.invoke({
            "title": article["title"],
            "text": article["text"][:MAX_TEXT_SIZE]  # Limit text to avoid token limits
        })
        return response.content
    except Exception as e:
        print(f"Error generating summary: {e}")
        return f"Error generating summary: {str(e)}"


def extract_topics(article: Dict[str, Any]) -> List[str]:
    """
    Extract main topics/themes from the article using GenAI.

    Args:
        article (Dict): Article data including title and text

    Returns:
        List[str]: A list of main topics
    """
    # Skip if no text
    if not article.get('text'):
        return ["Unable to extract topics: No article text available."]

    # Create an output parser
    output_parser = CommaSeparatedListOutputParser()

    # Create a prompt template
    topics_template = """
    Based on the following news article, identify the main topics or themes.
    Return a comma-separated list of 5-8 key topics.
    Topics should be individual terms or short phrases.

    TITLE: {title}

    ARTICLE: {text}

    TOPICS:
    """

    prompt = ChatPromptTemplate.from_template(topics_template)

    # Create the chain and run it
    chain = prompt | llm | output_parser
    try:
        topics = chain.invoke({
            "title": article["title"],
            "text": article["text"][:MAX_TEXT_SIZE]  # Limit text to avoid token limits
        })
        return topics
    except Exception as e:
        print(f"Error extracting topics: {e}")
        return [f"Error extracting topics: {str(e)}"]


def process_article(article: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process an article with GenAI to add summary and topics.

    Args:
        article (Dict): Article data from the extraction phase

    Returns:
        Dict: Original article data enriched with summary and topics
    """
    # Make a copy of the original article
    processed = article.copy()

    # Add summary
    processed["summary"] = generate_summary(article)

    # Add topics
    processed["topics"] = extract_topics(article)

    return processed