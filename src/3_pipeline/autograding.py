"""Autograding script"""

import os

ingested = "datalake/raw/ingested/"
if not os.path.exists(ingested):
    os.makedirs(ingested)

# test code files
assert os.path.exists("src/3_pipeline/config.json")
assert os.path.exists("src/3_pipeline/pipeline.py")
assert os.path.exists("src/3_pipeline/simple_query.py")

# test run
assert os.path.exists("datalake/raw/ingested/house_data_1.csv.zip")
