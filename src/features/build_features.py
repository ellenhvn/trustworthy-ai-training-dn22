"""
Script to create features from the raw data and do cleaning and preprocessing
"""
import os
import json
import numpy as np
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split

def load_data() -> pd.DataFrame:
    """
    Load csv file containing training data
    """
    return pd.read_csv(os.path.join(os.path.dirname(__file__), os.pardir, "data", "german_raw_data.csv"))


def replace_column_names(df: pd.DataFrame) -> pd.DataFrame:
    with open(os.path.join(os.path.dirname(__file__), "german_credit_config.json")) as file:
        config = json.load(file)
    df = df.rename(columns=config["Column Names"])
    # for more info about the mapping of the values refer to EDA notebook
    df = df.replace(config["Categorical Values Map"])
    df = df.replace(config["Ordinal Values Map"])
    return df


def create_dummy_columns(df:pd.DataFrame) -> pd.DataFrame:
    return pd.get_dummies(df)


def create_train_val_data(df:pd.DataFrame) -> pd.DataFrame:
    df.loc[:, "Risk"] = df.loc[:, "Risk"].replace({1: 0, 2: 1})

    X = df.drop("Risk", axis=1)
    y = df["Risk"]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.33, random_state=10)

    return X_train, X_val, y_train, y_val