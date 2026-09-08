"""Machine-learning demo pipeline for Alzheimer's disease gene prediction.

The public repository uses an example feature matrix. Preprocessing is fitted inside
scikit-learn pipelines so both hold-out and cross-validation estimates avoid
preprocessing leakage.
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import (
    RepeatedStratifiedKFold,
    cross_validate,
    train_test_split,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from xgboost import XGBClassifier


def validate_data(data, label_column="label"):
    """Validate the public-demo feature matrix and return feature names."""
    if data.empty:
        raise ValueError("Input dataset is empty.")
    if label_column not in data.columns:
        raise ValueError(f"Required label column '{label_column}' was not found.")

    feature_columns = [column for column in data.columns if column != label_column]
    if not feature_columns:
        raise ValueError("At least one feature column is required.")

    if data[label_column].isna().any():
        raise ValueError("Label column contains missing values.")

    classes = set(pd.unique(data[label_column]))
    if classes != {0, 1}:
        raise ValueError("The public demo expects binary labels encoded as 0 and 1.")

    class_counts = data[label_column].value_counts()
    if int(class_counts.min()) < 2:
        raise ValueError("Each label class must contain at least two samples.")

    non_numeric = [
        column
        for column in feature_columns
        if not pd.api.types.is_numeric_dtype(data[column])
    ]
    if non_numeric:
        raise ValueError(
            "Feature columns must be numeric. Non-numeric columns: "
            + ", ".join(non_numeric)
        )

    if data[feature_columns].isna().any().any():
        raise ValueError("Feature matrix contains missing values.")

    if not np.isfinite(data[feature_columns].to_numpy(dtype=float)).all():
        raise ValueError("Feature matrix contains non-finite values.")

    return feature_columns


def load_data(file_path, label_column="label"):
    data = pd.read_csv(file_path)
    validate_data(data, label_column)
    return data


def build_models(n_components):
    classifiers = {
        "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
        "Support Vector Machine": SVC(kernel="rbf", probability=True, random_state=42),
        "XGBoost": XGBClassifier(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=4,
            eval_metric="logloss",
            random_state=42,
        ),
    }

    return {
        name: Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("pca", PCA(n_components=n_components)),
                ("classifier", classifier),
            ]
        )
        for name, classifier in classifiers.items()
    }


def _validate_evaluation_settings(data, feature_columns, test_size, cv_splits, cv_repeats, n_components):
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1.")
    if cv_splits < 2:
        raise ValueError("cv_splits must be at least 2.")
    if cv_repeats < 1:
        raise ValueError("cv_repeats must be at least 1.")

    min_class_count = int(data["label"].value_counts().min())
    if cv_splits > min_class_count:
        raise ValueError(
            f"cv_splits cannot exceed the smallest class size ({min_class_count})."
        )

    test_count = math.ceil(len(data) * test_size)
    train_count = len(data) - test_count
    if test_count < 2 or train_count < 2:
        raise ValueError("test_size leaves too few samples for a stratified split.")

    smallest_cv_train_size = len(data) - math.ceil(len(data) / cv_splits)
    max_components = min(len(feature_columns), train_count, smallest_cv_train_size)
    if n_components < 1 or n_components > max_components:
        raise ValueError(
            f"n_components must be between 1 and {max_components} for the selected evaluation settings."
        )


def train_models(
    data,
    label_column="label",
    n_components=2,
    test_size=0.2,
    cv_splits=3,
    cv_repeats=2,
):
    """Evaluate models with one hold-out split plus repeated stratified CV."""
    feature_columns = validate_data(data, label_column)
    if label_column != "label":
        eval_data = data.rename(columns={label_column: "label"})
    else:
        eval_data = data

    _validate_evaluation_settings(
        eval_data,
        feature_columns,
        test_size,
        cv_splits,
        cv_repeats,
        n_components,
    )

    X = data[feature_columns]
    y = data[label_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42,
        stratify=y,
    )

    cv = RepeatedStratifiedKFold(
        n_splits=cv_splits,
        n_repeats=cv_repeats,
        random_state=42,
    )

    results = {}
    for model_name, model in build_models(n_components).items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        probabilities = model.predict_proba(X_test)[:, 1]

        cv_scores = cross_validate(
            model,
            X,
            y,
            cv=cv,
            scoring={"auc": "roc_auc", "accuracy": "accuracy"},
            return_train_score=False,
        )

        results[model_name] = {
            "auc": float(roc_auc_score(y_test, probabilities)),
            "accuracy": float(accuracy_score(y_test, predictions)),
            "classification_report": classification_report(
                y_test, predictions, output_dict=True, zero_division=0
            ),
            "cv_auc_mean": float(np.mean(cv_scores["test_auc"])),
            "cv_auc_std": float(np.std(cv_scores["test_auc"])),
            "cv_accuracy_mean": float(np.mean(cv_scores["test_accuracy"])),
            "cv_accuracy_std": float(np.std(cv_scores["test_accuracy"])),
            "cv_folds": int(len(cv_scores["test_auc"])),
        }

        print(
            f"{model_name}: hold-out AUC={results[model_name]['auc']:.3f}, "
            f"CV AUC={results[model_name]['cv_auc_mean']:.3f} "
            f"+/- {results[model_name]['cv_auc_std']:.3f}"
        )

    return results


def save_results(results, output_file):
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run the Alzheimer's gene-prediction ML demonstration pipeline."
    )
    parser.add_argument(
        "--input", default="data/example_feature_matrix.csv", help="Input CSV file."
    )
    parser.add_argument("--label-column", default="label")
    parser.add_argument("--pca-components", type=int, default=2)
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--cv-splits", type=int, default=3)
    parser.add_argument("--cv-repeats", type=int, default=2)
    parser.add_argument(
        "--output", default="results/model_metrics.json", help="Metrics JSON output."
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print("Loading and validating data...")
    data = load_data(args.input, args.label_column)
    print("Evaluating leakage-safe pipelines with hold-out and repeated stratified CV...")
    results = train_models(
        data,
        label_column=args.label_column,
        n_components=args.pca_components,
        test_size=args.test_size,
        cv_splits=args.cv_splits,
        cv_repeats=args.cv_repeats,
    )
    save_results(results, args.output)
    print(f"Metrics saved to {args.output}")


if __name__ == "__main__":
    main()
