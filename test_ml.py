import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

from ml.data import process_data
from ml.model import train_model, compute_model_metrics

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


def test_process_data():
    data = pd.read_csv("data/census.csv")

    X, y, encoder, lb = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )
    assert X.shape[0] > 0
    assert len(y) > 0


def test_train_model():
    data = pd.read_csv("data/census.csv")
    select_data = data.head(100)

    X, y, encoder, lb = process_data(
        select_data,
        categorical_features=cat_features,
        label="salary",
        training=True,
    )

    model = train_model(X, y)

    assert isinstance(model, RandomForestClassifier)


def test_compute_model_metrics():
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision >= 0
    assert recall >= 0
    assert fbeta >= 0
