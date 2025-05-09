import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Other configuration settings
DEFAULT_MODEL = "gpt-3.5-turbo"
VECTOR_DB_PATH = "./chroma_db"

#GenAI processing parameters
LLM_TEMPERATURE = 0.1
MAX_TEXT_SIZE=8000

# Customization options
TEST_URLS = [
    "https://www.bbc.com/news/articles/ce3985e708lo",
    "https://www.theguardian.com/uk-news/2025/may/09/sadiq-khan-to-announce-plans-to-build-houses-on-london-green-belt",
    "https://edition.cnn.com/2025/05/09/style/queen-elizabeth-ii-memorial-london-shortlist"
]

TEST_QUERIES = [
        "pope election",
        "city houses",
        "royal architecture"
]

SEARCH_RESULTS_LIMIT = 2