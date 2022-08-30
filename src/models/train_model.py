"""
Script to train a model from the preprocessed data
"""
import os
import pickle
import typing as th
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline


def load_data() -> th.Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Load the preprocessed data from pickle files
    :return: Tuple contain dataframes for train and validation X and y
    """
    X_train = pd.read_pickle(os.path.join(
        Path(__file__).parents[2], "data", "processed", "german_credit_X_train" + ".pickle"))
    X_val = pd.read_pickle(os.path.join(
        Path(__file__).parents[2], "data", "processed", "german_credit_X_val" + ".pickle"))
    y_train = pd.read_pickle(os.path.join(
        Path(__file__).parents[2], "data", "processed", "german_credit_y_train" + ".pickle"))
    y_val = pd.read_pickle(os.path.join(
        Path(__file__).parents[2], "data", "processed", "german_credit_y_val" + ".pickle"))
    return X_train, X_val, y_train, y_val


def train_model(clf: BaseEstimator, X_train: pd.DataFrame, X_val: pd.DataFrame,
                y_train: pd.DataFrame, y_val: pd.DataFrame) -> th.Tuple[BaseEstimator, float]:
    """
    Train a scikit learn model
    :param clf:
    :param X_train:
    :param X_val:
    :param y_train:
    :param y_val:
    :return:
    """
    model = Pipeline([
        ("scaler", MinMaxScaler()),
        ("model", clf)])
    model.fit(X_train, y_train)
    y_pred = model.predict_proba(X_val)[:, 1]
    metric = roc_auc_score(y_val, y_pred)
    return model, metric


def save_model(model: BaseEstimator, filename: str) -> None:
    """
    :param model:
    :param filename:
    :return:
    """
    pickle.dump(model, open(os.path.join(
        Path(__file__).parents[2], "models", "german_credit_" + filename + ".pickle"), "wb"))


if __name__ == "__main__":
    train_features, val_features, train_targets, val_targets = load_data()
    rf_clf = RandomForestClassifier(n_estimators = 100, random_state = 50, verbose = 1, n_jobs=-1)
    rf_model, rf_metric = train_model(rf_clf, train_features, val_features,
                                      train_targets, val_targets)
    print("ROC AUC score for model " + str(type(rf_model).__name__) +
          ": " + str(np.round(rf_metric, 3)))
    save_model(rf_model, "pipeline_randomForest")
