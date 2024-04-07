"""Autograding script"""

import os


logs = "datalake/logs/"
if not os.path.exists(logs):
    os.makedirs(logs)
    

# test code files
assert os.path.exists("src/6b_api_server/config.json")
assert os.path.exists("src/6b_api_server/server.py")


# test run
assert os.path.exists("datalake/logs/api_server.log")
