# Pre-requisites
Before you start, make sure you have installed the following software:
1. Git
2. python3

This guide assumes that you work in unix shell. For Windows users - consider installing git bash or using Linux subsystem.

# Project description
This project is a Python-based solution designed to extract, summarize, and semantically search news articles
using Generative AI (GenAI) tools. It automates the process of gathering news content, analyzing it with AI,
and enabling intelligent search functionality. The key features of the project include:

### News Extraction
Scrapes full-text content and headlines from provided URLs to collect news articles efficiently.

### GenAI-Powered Summarization and Topic Identification
Leverages Generative AI models (e.g., OpenAI's GPT) to generate concise summaries and identify the main topics of each article, ensuring key insights are captured.

### Semantic Search
Stores extracted articles, summaries, and topics in a vector database. Implements a semantic search feature that interprets user queries contextually and retrieves relevant articles.

# Summary
This project demonstrates the effective application of GenAI tools for real-world use cases, combining web scraping, natural language processing, and advanced search capabilities into a cohesive system.

# Quick start
1. Pull the repo
2. Create .env file with openai api key 
    - file content:
    ```shell
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
       pip install -r requirements.txt
    ```
6. Run the test file you're interested in (full functionality test is in test_search.py)
    - command:
    ```shell
       python3 test_search.py
    ```

# python cheat sheet
Deactivate venv:
```shell
  deactivate
```

Dump dependency versions:
```shell
  pip freeze > requirements.txt
```