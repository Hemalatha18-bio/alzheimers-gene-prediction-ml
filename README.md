# Machine Learning Pipeline for Alzheimer's Disease Gene Prediction

## Overview

This portfolio project documents a machine-learning workflow for exploring Alzheimer's disease-associated genomic patterns using public biological data sources. The broader project methodology includes genomic/transcriptomic integration, dimensionality reduction, model comparison, explainability, biological interpretation, and Linux/HPC execution.

The **public repository is a reproducible demonstration of selected workflow components**. Raw research datasets are not distributed here, and the included example feature matrix is intended for code demonstration rather than clinical or research validation.

## Objectives

The broader project explored how to:

- integrate GWAS, GEO, and disease-gene association information;
- harmonize high-dimensional genomic features;
- apply preprocessing and dimensionality reduction;
- compare machine-learning classifiers;
- evaluate predictive performance;
- connect computational outputs with biological interpretation; and
- organize computational work for reproducible Linux/HPC execution.

## Public Repository Scope

The code published here focuses on a compact ML demonstration using a tabular feature matrix. It currently demonstrates:

- CSV data loading and validation;
- train/test splitting;
- leakage-safe scaling and PCA using scikit-learn pipelines;
- Random Forest, SVM, and XGBoost classification;
- AUC and accuracy calculation;
- classification reports;
- machine-readable JSON result export;
- plotting of AUC and accuracy directly from exported metrics;
- basic automated tests; and
- a generic SLURM example for HPC execution.

Other components discussed in the broader project context—such as full GWAS/GEO ingestion, batch correction, SHAP analysis, GO enrichment, deep-learning experiments, and production HPC orchestration—are not fully reproduced by the current public code and should not be inferred from the demo scripts alone.

## Data Sources and Privacy

The broader analysis drew on publicly available biological resources such as GWAS studies, GEO expression datasets, disease-gene association resources, Gene Ontology resources, and scientific literature.

Raw research datasets are not included in this repository. Small example or synthetic files may be included solely to demonstrate code execution. See `data_description.md` for additional data notes.

## Technologies

- Python
- pandas / NumPy
- scikit-learn
- XGBoost
- matplotlib
- pytest
- SHAP (broader project methodology)
- Linux/HPC
- SLURM
- Git/GitHub

## Repository Structure

```text
alzheimers-gene-prediction-ml/
├── README.md
├── data_description.md
├── requirements.txt
├── data/
│   └── example_feature_matrix.csv
├── src/
│   ├── model_pipeline.py
│   └── visualize_results.py
├── tests/
│   └── test_model_pipeline.py
├── hpc/
│   └── run_model.slurm
├── figures/
├── results/
├── reports/
├── notebooks/
└── LICENSE
```

## How to Run the Public Demo

### 1. Clone the repository

```bash
git clone https://github.com/Hemalatha18-bio/alzheimers-gene-prediction-ml.git
cd alzheimers-gene-prediction-ml
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with `.venv\\Scripts\\activate`.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the model pipeline

```bash
python src/model_pipeline.py \
  --input data/example_feature_matrix.csv \
  --pca-components 2 \
  --output results/model_metrics.json
```

The script splits the data before model-specific preprocessing. Scaling and PCA are fitted only using the training partition through a scikit-learn `Pipeline`, reducing preprocessing leakage into the held-out test data.

### 5. Generate figures from the exported metrics

```bash
python src/visualize_results.py \
  --metrics results/model_metrics.json \
  --output-dir figures
```

This generates model-comparison figures from the **actual metrics exported by the pipeline**, rather than hard-coded example performance values.

### 6. Run the tests

```bash
pytest -q
```

### 7. HPC / SLURM example

A generic SLURM submission example is included at:

```text
hpc/run_model.slurm
```

It is intended as a portable example of how the public demo could be submitted in a SLURM-based environment. Cluster-specific resource requests, modules, environments, paths, and policies should be adjusted for the system where it is used.

## Outputs

Model metrics are written to:

```text
results/model_metrics.json
```

Generated figures are written to the selected output directory, typically:

```text
figures/
```

## Broader Project Outcomes

The original project work included multi-source biological data integration, high-dimensional feature processing, model experimentation, biological interpretation, and use of Linux/HPC resources. Quantitative claims from the broader project are intentionally not presented here as reproducible public-demo results unless the corresponding data and analysis are available in this repository.

## Limitations

- The public demo is not a clinical prediction system.
- Example/synthetic data cannot establish biological validity or clinical performance.
- The public code represents selected components rather than the complete original research workflow.
- External validation and additional reproducibility work would be required before drawing scientific conclusions.

## Optional Future Enhancements

- Add cross-validation to the public demo.
- Add GitHub Actions CI for automated testing.
- Add richer logging and additional input validation.
- Add safe, reproducible examples for SHAP explainability and biological interpretation.
- Add example GO-enrichment outputs where data licensing and reproducibility allow.
- Consider workflow management with Snakemake or Nextflow.

## Skills Demonstrated

This repository demonstrates Python-based scientific programming, machine-learning pipeline construction, high-dimensional data preprocessing, model evaluation, reproducibility practices, automated testing, result visualization, Git/GitHub organization, and familiarity with Linux/HPC and SLURM workflow concepts.

## Author

Hemalatha Ponnam  
M.S. Bioinformatics & Computational Biology  
Saint Louis University
