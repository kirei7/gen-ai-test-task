# Pre-requisites
Before you start, make sure you have installed the following software:
1. Git
2. python3

This guide assumes that you work in unix shell. For Windows users - consider installing git bash or using Linux subsystem. 
# Quick start
1. Pull the repo
2. Create .env file with openai api key 
    - file content:
    ```shell
       OPENAI_API_KEY=<YOUR_API_KEY>
    ``` 
3. Activate venv
    - command:
    ```shell
       source venv/bin/activate
    ```
4. Set up project dependencies
    - command:
    ```shell
       pip install -r requirements.txt
    ```
5. Run the test file you're interested in (full functionality test is in test_search.py)
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