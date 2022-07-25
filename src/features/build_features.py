"""
Script to create features from the raw data and do cleaning and preprocessing
"""
import os
import json
import numpy as np
import pandas as pd
import pickle

class FeatureBuilder():
    def __init__(self):
        self.csv_file = ""
        self.settings_file = ""

    def replace_values(self) -> pd.DataFrame:
        """
        Read the column names, categorical and ordinal values from a config file and replace in the raw data
        """
        with open(os.path.join(os.path.dirname(__file__), "german_credit_config.json")) as file:
            config = json.load(file)
        df = df.rename(columns=config["Column Names"])
        # for more info about the mapping of the values refer to EDA notebook
        df = df.replace(config["Categorical Values Map"])
        df = df.replace(config["Ordinal Values Map"])