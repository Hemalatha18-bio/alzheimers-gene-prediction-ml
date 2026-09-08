# Data Description

## Project
Machine Learning Pipeline for Alzheimer's Disease Gene Prediction

## Public Demo Data

The executable public demonstration in this repository uses:

`data/example_feature_matrix.csv`

This is a small example feature matrix intended to demonstrate code execution, testing, workflow structure, model evaluation, and explainability methods. It is not a research-scale Alzheimer's disease dataset and should not be used to draw biological or clinical conclusions.

The public model code expects a tabular feature matrix in which:

- rows represent observations;
- columns represent numeric input features; and
- the target column is named `label` by default.

The example file is included so that users can run the repository without downloading large external datasets.

## What the Public Repository Does With the Data

The current public implementation:

1. loads the example CSV file;
2. validates that the required label column is present and that the table is not empty;
3. separates input features from the label;
4. performs a stratified train/test split;
5. applies standardization and PCA inside scikit-learn model pipelines;
6. trains Random Forest, Support Vector Machine, and XGBoost classifiers;
7. exports ROC-AUC, accuracy, and classification-report metrics;
8. generates model-comparison figures from exported metrics; and
9. provides a separate SHAP explainability demonstration on the example feature matrix.

Because the example data are for software demonstration, generated metrics and feature explanations should be treated as example outputs rather than biological findings.

## Broader Project Data Context

The broader project experience that motivated this portfolio repository involved working with or considering public biological resources such as:

- genome-wide association study resources;
- GEO gene-expression datasets;
- disease-gene association resources such as DisGeNET;
- Gene Ontology and related annotation resources;
- NCBI gene information; and
- scientific literature used for biological interpretation.

That broader context included concepts such as gene-identifier harmonization, high-dimensional feature processing, dimensionality reduction, feature engineering, biological interpretation, and enrichment analysis.

However, those original datasets and the complete data-integration workflow are not included in this public repository. Readers should not assume that the compact example feature matrix reproduces the original research-scale workflow.

## Why Original Research-Scale Data Are Not Included

Research-scale biological datasets may be large, distributed across multiple public resources, governed by source-specific usage terms, or associated with project environments that are not appropriate to publish directly.

This repository therefore focuses on a small, shareable demonstration that makes the software structure and reproducibility practices visible without distributing large or restricted data.

## Reproducing the Public Demo

No external biological dataset is required to run the included demonstration.

After installing the dependencies, users can execute the model pipeline with:

```bash
python src/model_pipeline.py \
  --input data/example_feature_matrix.csv \
  --pca-components 2 \
  --output results/model_metrics.json
```

The SHAP demonstration can be run with:

```bash
python src/explain_model.py \
  --input data/example_feature_matrix.csv \
  --output figures/shap_summary.png
```

The full demonstration workflow can also be executed through Snakemake as documented in the main `README.md`.

## Extending the Repository With Public Biological Data

A future fully reproducible extension using real public biological datasets should document, at minimum:

1. exact dataset identifiers or accession numbers;
2. download sources and access dates;
3. sample inclusion and exclusion criteria;
4. gene or feature identifier mappings;
5. preprocessing and normalization procedures;
6. missing-value handling;
7. batch or cohort effects where relevant;
8. train/test or cross-validation strategy;
9. any feature-selection procedure;
10. enrichment-analysis inputs and background universe; and
11. software and database versions.

Any preprocessing or feature selection used for predictive modeling should be fitted within the appropriate training or cross-validation workflow to avoid information leakage.

## Privacy and Responsible Use

The public example data are intended only for portfolio and software-demonstration purposes. The repository does not contain private patient records, protected health information, confidential clinical data, or unpublished lab-owned datasets.

Users applying the code to their own biological datasets are responsible for following the relevant data-use, privacy, licensing, and institutional requirements.

## Interpretation

This repository demonstrates computational methods and reproducibility practices. It is not a clinical prediction tool and does not provide validated evidence for Alzheimer's disease-associated genes or mechanisms.

For the most accurate description of the current public scope, refer to the main `README.md`, source files under `src/`, automated tests under `tests/`, and workflow definitions under `workflow/`.
