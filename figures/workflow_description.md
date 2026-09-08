# Workflow Description

## Public Demonstration

The public workflow in this repository is a compact, reproducible example that starts from `data/example_feature_matrix.csv` and produces model metrics and visualizations.

### Modeling path

```text
example feature matrix
        ↓
train/test split
        ↓
scikit-learn pipeline
(StandardScaler → PCA → classifier)
        ↓
Random Forest / SVM / XGBoost
        ↓
ROC-AUC, accuracy, classification report
        ↓
results/model_metrics.json
        ↓
model-comparison figures
```

Preprocessing is fitted within each model pipeline after the train/test split so that the held-out test data are not used to fit scaling or PCA transformations.

### Explainability path

```text
example feature matrix
        ↓
train/test split
        ↓
Random Forest demonstration
        ↓
SHAP explanation
        ↓
figures/shap_summary.png
```

The SHAP figure is a methodological example generated from demonstration data. It is not evidence for Alzheimer's disease-associated genes or mechanisms.

## Reproducibility Components

The repository also includes:

- pytest automated tests;
- GitHub Actions continuous integration;
- a Snakemake workflow connecting model training and visualization; and
- a generic SLURM example for HPC-oriented execution.

## Broader Context

Broader Alzheimer's bioinformatics experience that motivated this repository included genomic and transcriptomic data integration, disease-gene association resources, high-dimensional feature analysis, biological interpretation, enrichment-analysis concepts, and Linux/HPC work.

Those broader activities are project context rather than fully reproduced components of the current public workflow.
