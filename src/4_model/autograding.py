"""Autograding script"""

import os

models = "datalake/models/"
if not os.path.exists(models):
    os.makedirs(models)


# test code files
assert os.path.exists("src/4_model/config.json")
assert os.path.exists("src/4_model/train.py")

# test run
assert os.path.exists("datalake/models/house_prices_model.pkl")
