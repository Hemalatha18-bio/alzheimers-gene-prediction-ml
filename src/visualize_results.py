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
            }
        )
    return pd.DataFrame(rows)


def plot_model_auc(results, output_file):
    if results["AUC"].isna().any():
        raise ValueError("One or more models are missing AUC values.")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.bar(results["Model"], results["AUC"])
    plt.ylim(0, 1)
    plt.xlabel("Machine Learning Model")
    plt.ylabel("AUC Score")
    plt.title("Model Performance Comparison")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


def plot_model_accuracy(results, output_file):
    if results["Accuracy"].isna().any():
        raise ValueError("One or more models are missing accuracy values.")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.bar(results["Model"], results["Accuracy"])
    plt.ylim(0, 1)
    plt.xlabel("Machine Learning Model")
    plt.ylabel("Accuracy")
    plt.title("Model Accuracy Comparison")
    plt.xticks(rotation=15, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


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
    print(f"Figures saved in {output_dir}")


if __name__ == "__main__":
    main()
