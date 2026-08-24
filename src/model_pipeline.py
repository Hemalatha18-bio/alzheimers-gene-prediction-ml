"""Machine-learning demo pipeline for Alzheimer's disease gene prediction.

The public repository uses an example feature matrix. Preprocessing is fitted only
on training data to avoid test-set leakage.
"""

import argparse
import json
from pathlib import Path

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from xgboost import XGBClassifier


def load_data(file_path, label_column="label"):
    data = pd.read_csv(file_path)
    if label_column not in data.columns:
        raise ValueError(f"Required label column '{label_column}' was not found.")
    if data.empty:
        raise ValueError("Input dataset is empty.")
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


def train_models(data, label_column="label", n_components=2, test_size=0.2):
    X = data.drop(columns=[label_column])
    y = data[label_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42, stratify=y
    )

    max_components = min(X_train.shape[0], X_train.shape[1])
    if n_components < 1 or n_components > max_components:
        raise ValueError(
            f"n_components must be between 1 and {max_components} for this dataset."
        )

    results = {}
    for model_name, model in build_models(n_components).items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        probabilities = model.predict_proba(X_test)[:, 1]

        results[model_name] = {
            "auc": float(roc_auc_score(y_test, probabilities)),
            "accuracy": float(accuracy_score(y_test, predictions)),
            "classification_report": classification_report(
                y_test, predictions, output_dict=True, zero_division=0
            ),
        }

        print(f"{model_name}: AUC={results[model_name]['auc']:.3f}, "
              f"accuracy={results[model_name]['accuracy']:.3f}")

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
    parser.add_argument(
        "--output", default="results/model_metrics.json", help="Metrics JSON output."
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print("Loading data...")
    data = load_data(args.input, args.label_column)
    print("Training leakage-safe pipelines...")
    results = train_models(
        data,
        label_column=args.label_column,
        n_components=args.pca_components,
        test_size=args.test_size,
    )
    save_results(results, args.output)
    print(f"Metrics saved to {args.output}")


if __name__ == "__main__":
    main()
