"""Autograding script"""

import os
logs = "datalake/logs/"
if not os.path.exists(logs):
    os.makedirs(logs)

# test code files
assert os.path.exists("config.json")
assert os.path.exists("src/6a_api_client/app.py")


# test run
assert os.path.exists("datalake/logs/api_client.log")
