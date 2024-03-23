"""Autograding script"""

import os

databases_dir = "datalake/databases/"
if not os.path.exists(databases_dir):
    os.makedirs(databases_dir)

downsampled_data = "datalake/downsampled_data/"
if not os.path.exists(downsampled_data):
    os.makedirs(downsampled_data)

logs = "datalake/logs/"
if not os.path.exists(logs):
    os.makedirs(logs)

models = "datalake/models/"
if not os.path.exists(models):
    os.makedirs(models)

stagging = "datalake/raw/stagging/"
if not os.path.exists(stagging):
    os.makedirs(stagging)

ingested = "datalake/raw/ingested/"
if not os.path.exists(ingested):
    os.makedirs(ingested)


# test code files
assert os.path.exists("src/1_datalake/create_datalake.py")
assert os.path.exists("src/1_datalake/datalake_structure.txt")

# test datalake structure
assert os.path.exists("datalake/databases/")
assert os.path.exists("datalake/downsampled_data/")
assert os.path.exists("datalake/logs/")
assert os.path.exists("datalake/models/")
assert os.path.exists("datalake/raw/stagging/")
assert os.path.exists("datalake/raw/ingested/")
