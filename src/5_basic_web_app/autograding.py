"""Autograding script"""

import os

logs = "datalake/logs/"
if not os.path.exists(logs):
    os.makedirs(logs)
    
# test code files
assert os.path.exists("src/5_basic_web_app/config.json")
assert os.path.exists("src/5_basic_web_app/app.py")
assert os.path.exists("src/5_basic_web_app/templates/index.html")

# test run
assert os.path.exists("datalake/logs/basic_web_app.log")
