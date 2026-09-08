"""Visualize model metrics produced by the Alzheimer's ML demo pipeline."""

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def load_metrics(metrics_file):
    path = Path(metrics_file)
    if not path.exists():
        raise FileNotFoundError(f"Metrics file not found: {metrics_file}")

    with path.open("r", encoding="utf-8") as handle:
        metrics = json.load(handle)

    if not metrics:
        raise ValueError("Metrics file is empty.")
    return metrics


def metrics_to_dataframe(metrics):
    rows = []
    for model_name, values in metrics.items():
        rows.append(
            {
                "Model": model_name,
                "AUC": values.get("auc"),
                "Accuracy": values.get("accuracy"),
                "CV AUC": values.get("cv_auc_mean"),
                "CV AUC SD": values.get("cv_auc_std"),
                "CV Accuracy": values.get("cv_accuracy_mean"),
                "CV Accuracy SD": values.get("cv_accuracy_std"),
            }
        )
    return pd.DataFrame(rows)


def _save_bar_plot(results, value_column, output_file, ylabel, title, error_column=None):
    if results[value_column].isna().any():
        raise ValueError(f"One or more models are missing {value_column} values.")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    errors = None
    if error_column is not None:
        if results[error_column].isna().any():
            raise ValueError(f"One or more models are missing {error_column} values.")
        errors = results[error_column]

    plt.figure(figsize=(8, 5))
    plt.bar(results["Model"], results[value_column], yerr=errors, capsize=4 if errors is not None else 0)
    plt.ylim(0, 1.05)
    plt.xlabel("Machine Learning Model")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def plot_model_auc(results, output_file):
    _save_bar_plot(
        results,
        "AUC",
        output_file,
        "Hold-out AUC",
        "Hold-out Model Performance (Example Data)",
    )


def plot_model_accuracy(results, output_file):
    _save_bar_plot(
        results,
        "Accuracy",
        output_file,
        "Hold-out Accuracy",
        "Hold-out Model Accuracy (Example Data)",
    )


def plot_cv_auc(results, output_file):
    _save_bar_plot(
        results,
        "CV AUC",
        output_file,
        "Repeated CV ROC-AUC",
        "Repeated Stratified Cross-Validation AUC (Example Data)",
        error_column="CV AUC SD",
    )


def plot_cv_accuracy(results, output_file):
    _save_bar_plot(
        results,
        "CV Accuracy",
        output_file,
        "Repeated CV Accuracy",
        "Repeated Stratified Cross-Validation Accuracy (Example Data)",
        error_column="CV Accuracy SD",
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create figures from exported model metrics."
    )
    parser.add_argument(
        "--metrics", default="results/model_metrics.json", help="Metrics JSON file."
    )
    parser.add_argument(
        "--output-dir", default="figures", help="Directory for generated figures."
    )
    return parser.parse_args()


def main():
    args = parse_args()
    metrics = load_metrics(args.metrics)
    results = metrics_to_dataframe(metrics)

    output_dir = Path(args.output_dir)
    plot_model_auc(results, output_dir / "model_auc_comparison.png")
    plot_model_accuracy(results, output_dir / "model_accuracy_comparison.png")
    plot_cv_auc(results, output_dir / "model_cv_auc_comparison.svg")
    plot_cv_accuracy(results, output_dir / "model_cv_accuracy_comparison.svg")
    print(f"Figures saved in {output_dir}")


if __name__ == "__main__":
    main()
