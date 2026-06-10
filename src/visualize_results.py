"""
Visualization script for Alzheimer's Disease Gene Prediction project.

This script creates simple example visualizations from demo model results.
Author: Hemalatha Ponnam
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_model_auc():
    """
    Create a bar plot comparing example AUC scores for ML models.
    """

    results = pd.DataFrame({
        "Model": ["Random Forest", "SVM", "XGBoost"],
        "AUC": [0.91, 0.88, 0.93]
    })

    plt.figure(figsize=(8, 5))
    plt.bar(results["Model"], results["AUC"])
    plt.ylim(0, 1)
    plt.xlabel("Machine Learning Model")
    plt.ylabel("AUC Score")
    plt.title("Example Model Performance Comparison")
    plt.tight_layout()
    plt.savefig("figures/model_auc_comparison.png", dpi=300)
    plt.show()


def plot_top_genes():
    """
    Create a bar plot showing example top-ranked genes.
    """

    genes = pd.DataFrame({
        "Gene": ["APOE", "BIN1", "CLU", "PICALM", "CR1"],
        "Importance": [0.24, 0.18, 0.15, 0.12, 0.09]
    })

    plt.figure(figsize=(8, 5))
    plt.bar(genes["Gene"], genes["Importance"])
    plt.xlabel("Gene")
    plt.ylabel("Example Feature Importance")
    plt.title("Example Top Gene Features")
    plt.tight_layout()
    plt.savefig("figures/top_gene_features.png", dpi=300)
    plt.show()


def main():
    print("Generating visualizations...")
    plot_model_auc()
    plot_top_genes()
    print("Figures saved in the figures/ folder.")


if __name__ == "__main__":
    main()
