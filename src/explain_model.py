"""Train a leakage-safe Random Forest pipeline and create a SHAP summary plot.

This is a portfolio demonstration using the repository's example feature matrix.
It is not a biological or clinical interpretation of Alzheimer's disease.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import shap
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def parse_args():
    parser = argparse.ArgumentParser(description="Create a SHAP explanation demo.")
    parser.add_argument("--input", default="data/example_feature_matrix.csv")
    parser.add_argument("--label-column", default="label")
    parser.add_argument("--output", default="figures/shap_summary.png")
    return parser.parse_args()


def main():
    args = parse_args()
    data = pd.read_csv(args.input)
    if args.label_column not in data.columns:
        raise ValueError(f"Missing label column: {args.label_column}")

    X = data.drop(columns=[args.label_column])
    y = data[args.label_column]
    X_train, X_test, y_train, _ = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("classifier", RandomForestClassifier(n_estimators=200, random_state=42)),
        ]
    )
    pipeline.fit(X_train, y_train)

    scaler = pipeline.named_steps["scaler"]
    classifier = pipeline.named_steps["classifier"]
    X_test_scaled = scaler.transform(X_test)

    explainer = shap.TreeExplainer(classifier)
    shap_values = explainer.shap_values(X_test_scaled)
    values = shap_values[1] if isinstance(shap_values, list) else shap_values

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    shap.summary_plot(values, X_test_scaled, feature_names=X.columns, show=False)
    plt.tight_layout()
    plt.savefig(output, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"SHAP demonstration figure saved to {output}")


if __name__ == "__main__":
    main()
