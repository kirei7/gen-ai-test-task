# Project description
This project is a Python-based solution designed to extract, summarize, and semantically search news articles
using Generative AI. It automates the process of gathering news content, analyzing it with AI,
and enabling intelligent search functionality. 

## The key features of the project include:
### News Extraction
Scrapes full-text content and headlines from provided URLs to collect news articles efficiently.
### GenAI-Powered Summarization and Topic Identification
Leverages Generative AI model (gpt-3.5-turbo) to generate concise summaries and identify the main topics of each
article, ensuring key insights are captured.
### Semantic Search
Stores extracted articles, summaries, and topics in a vector database. Implements a semantic search feature that
interprets user queries contextually and retrieves relevant articles.
## Summary
This project demonstrates the effective application of GenAI tools for real-world use cases, combining web scraping,
natural language processing, and advanced search capabilities into a cohesive system.

# Pre-requisites
Before you start, make sure you have installed the following software:
1. Git
2. python3
3. This guide assumes that you work in unix shell. For Windows users - consider installing git bash or using Linux subsystem.

### To improve your experience with this project make sure to go through this readme first!

# Quick start
0. All the commands from this guide must be executed in the root project directory unless specified otherwise.
1. Pull the repo
2. Create .env file in root project directory and put your openai api key inside 
    - file content:
    ```dotenv
       OPENAI_API_KEY=<YOUR_API_KEY>
    ```
3. Create venv
   - command:
    ```shell
       python3 -m venv venv
    ```
4. Activate venv
    - command:
    ```shell
       source venv/bin/activate
    ```
5. Set up project dependencies
    - command:
    ```shell
       pip install -r requirements-short.txt
    ```
6. Run the test file you're interested in (full functionality test is in test_search.py)
    - command:
    ```shell
       python3 test_search.py
    ```
7. Observe execution logs
    - application logs inform about the completed stages of execution or errors;
    - search results provide article info;
    - search results contain "Relevance" parameter, which indicates the relevance of the article to the query
      and effectively it inverted distance between query and article (1 - distance = relevance);
    - search results are sorted by relevance (more relevant articles are at the top).

# Customization
To customize via configs, look for "# Customization options" section in config.py
- TEST_URLS - list of URLs to scrape
- TEST_QUERIES - query to search for
- SEARCH_RESULTS_LIMIT - number of vectors to be returned by search from DB

# Few words on project structure
In the root directory there are several test files that demonstrate the functionality of the project. Each next entry
in this list also tests the functionality of the previous one.
- test_extraction.py - scrapping the news articles
- test_genai.py - summarization and topic identification
- test_vector_db.py - embedding and saving summarized articles to database
- test_search.py - semantic search through the database (most complete test which demonstrates the whole project)

# python cheat sheet
Deactivate venv:
```shell
  deactivate
```

Dump dependency versions:
```shell
  pip freeze > requirements.txt
```