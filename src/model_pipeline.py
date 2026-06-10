"""
Machine Learning Pipeline for Alzheimer's Disease Gene Prediction

This script provides a simple template for preprocessing high-dimensional
genomic features, training machine learning models, and evaluating performance.

Author: Hemalatha Ponnam
"""

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, roc_auc_score

from xgboost import XGBClassifier


def load_data(file_path):
    """
    Load a feature matrix from a CSV file.

    Expected format:
    - Rows = samples or genes
    - Columns = genomic features
    - One column named 'label' for disease/control or class status
    """
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data, label_column="label", n_components=50):
    """
    Preprocess genomic feature data using scaling and PCA.
    """
    X = data.drop(columns=[label_column])
    y = data[label_column]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)

    return X_pca, y, pca


def train_models(X, y):
    """
    Train and evaluate multiple machine learning models.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    models = {
        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42
        ),
        "Support Vector Machine": SVC(
            kernel="rbf",
            probability=True,
            random_state=42
        ),
        "XGBoost": XGBClassifier(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=4,
            eval_metric="logloss",
            random_state=42
        )
    }

    results = {}

    for model_name, model in models.items():
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]

        auc = roc_auc_score(y_test, y_prob)
        report = classification_report(y_test, y_pred)

        results[model_name] = {
            "auc": auc,
            "classification_report": report
        }

        print(f"\nModel: {model_name}")
        print(f"AUC: {auc:.3f}")
        print(report)

    return results


def main():
    """
    Example workflow.

    Replace 'example_feature_matrix.csv' with the actual processed dataset path.
    """
    file_path = "example_feature_matrix.csv"

    print("Loading data...")
    data = load_data(file_path)

    print("Preprocessing data...")
    X, y, pca_model = preprocess_data(data)

    print("Training models...")
    results = train_models(X, y)

    print("Pipeline completed.")


if __name__ == "__main__":
    main()
