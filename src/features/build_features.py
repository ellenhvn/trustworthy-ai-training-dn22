"""
Script to create features from the raw data and do cleaning and preprocessing
"""
import os
import json
import pickle
import typing as th
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data() -> pd.DataFrame:
    """
    :return: Dataframe containing the raw German credit data
    """
    return pd.read_csv(os.path.join(Path(__file__).parents[2],
                                    "data", "raw", "german_raw_data.csv"))


def replace_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace
    :param df: Dataframe with raw data
    :return: Dataframe with new column names
    """
    with open(os.path.join(Path(__file__).parents[2],
                           "config", "german_credit_config.json")) as config_file:
        config = json.load(config_file)
    df = df.rename(columns=config["Column Names"])
    # for more info about the mapping of the values refer to EDA notebook
    df = df.replace(config["Categorical Values Map"])
    df = df.replace(config["Ordinal Values Map"])
    return df


def create_dummy_columns(df:pd.DataFrame) -> pd.DataFrame:
    """
    :param df:
    :return: Dataframe with OHE columns
    """
    return pd.get_dummies(df)


def create_train_val_data(df:pd.DataFrame) -> \
        th.Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Replace target values with 0 & 1
    In the inital data set, 1 is considered
    Split data into features and targets
    Split data int train and validation set
    :param df: Dataframe with OHE and preprocessed data
    :return:
    """
    df.loc[:, "Risk"] = df.loc[:, "Risk"].replace({1: 0, 2: 1})
    X = df.drop("Risk", axis=1)
    y = df["Risk"]
    train_features, train_targets, \
    val_features, val_targets = train_test_split(X, y, test_size=0.3, random_state=0)
    return train_features, train_targets, val_features, val_targets

def save_data(train_features: pd.DataFrame, val_features: pd.DataFrame,
              train_targets: pd.DataFrame, val_targets: pd.DataFrame) -> None:
    """
    Save data used for training and validation
    """
    pickle.dump(train_features, open(os.path.join(
        Path(__file__).parents[2], "data", "processed",
        "german_credit_X_train" + ".pickle"), "wb"))
    pickle.dump(val_features, open(os.path.join(
        Path(__file__).parents[2], "data", "processed",
        "german_credit_X_val" + ".pickle"), "wb"))
    pickle.dump(train_targets, open(os.path.join(
        Path(__file__).parents[2], "data", "processed",
        "german_credit_y_train" +  ".pickle"), "wb"))
    pickle.dump(val_targets, open(os.path.join(
        Path(__file__).parents[2], "data", "processed",
        "german_credit_y_val" + ".pickle"), "wb"))


if __name__ == "__main__":
    preprocessed_data = create_dummy_columns(replace_column_names(load_data()))
    X_train, X_val, y_train, y_val = create_train_val_data(preprocessed_data)
    save_data(X_train, X_val, y_train, y_val)
