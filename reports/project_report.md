# Project Report: Machine Learning Pipeline for Alzheimer's Disease Gene Prediction

## Author
Hemalatha Ponnam

## Background

Alzheimer's disease is a complex neurodegenerative disorder with genetic, transcriptomic, and pathway-level contributors. Public biological resources can support exploratory analysis of disease-associated genes, but integrating heterogeneous datasets requires careful preprocessing, clear assumptions, and reproducible computational workflows.

This repository presents a compact public demonstration of machine-learning and reproducibility practices relevant to that broader problem.

## Public Repository Objective

The objective of the public repository is to demonstrate a reproducible machine-learning workflow that can:

1. load and validate a tabular biological feature matrix;
2. split training and test data before fitting preprocessing steps;
3. apply standardization and PCA within scikit-learn pipelines;
4. train and compare Random Forest, Support Vector Machine, and XGBoost classifiers;
5. export model-evaluation metrics;
6. generate figures from exported results;
7. demonstrate SHAP-based model explainability on example data;
8. run automated tests with pytest and GitHub Actions;
9. orchestrate the demo with Snakemake; and
10. illustrate execution in a SLURM/HPC environment.

## Public Demonstration Methods

### Data

The executable public workflow uses `data/example_feature_matrix.csv`, a small example dataset intended for software demonstration. It is not a research-scale Alzheimer's cohort and is not intended for clinical or biological validation.

### Preprocessing

The model code performs a stratified train/test split before fitting preprocessing. Standardization and PCA are placed inside scikit-learn pipelines so these transformations are learned from training data rather than the held-out test partition.

### Machine Learning

The public implementation compares:

- Random Forest
- Support Vector Machine
- XGBoost

The pipeline exports ROC-AUC, accuracy, and classification-report metrics to a machine-readable JSON file.

### Explainability

A separate script demonstrates SHAP-based feature explanation with a Random Forest model trained on the example feature matrix. The resulting explanations illustrate methodology only and should not be interpreted as evidence for Alzheimer's disease biology.

### Reproducibility and Software Engineering

The repository includes:

- pytest-based automated tests;
- GitHub Actions continuous integration;
- a Snakemake workflow;
- command-line interfaces;
- documented output locations; and
- a generic SLURM submission example for HPC-oriented execution.

## Public Demonstration Results

The public code generates model metrics and visualizations from the included example data. These outputs demonstrate that the pipeline is executable and show how model comparison and explainability are organized.

No clinical-performance or disease-mechanism claims should be inferred from metrics generated on the example dataset. Quantitative results from broader project work are intentionally not presented as reproducible public results unless the underlying data and analysis are available in this repository.

## Broader Project Experience

The broader project context involved experience with public biological resources and concepts such as:

- genomic and transcriptomic data integration;
- disease-gene association resources;
- high-dimensional biological feature processing;
- dimensionality reduction and feature engineering;
- machine-learning model experimentation;
- biological interpretation and enrichment-analysis concepts;
- scientific literature review; and
- Linux/HPC execution.

These activities provide context for the portfolio project but are not all implemented by the current public scripts. The public repository is deliberately narrower so that the code, example data, tests, and workflow can be shared responsibly and reproduced by others.

## Skills Demonstrated

The repository demonstrates:

- Python scientific programming;
- pandas and NumPy data handling;
- scikit-learn pipeline construction;
- Random Forest, SVM, and XGBoost modeling;
- leakage-aware preprocessing;
- PCA and dimensionality reduction;
- ROC-AUC and classification evaluation;
- SHAP explainability concepts;
- automated testing;
- GitHub Actions CI;
- Snakemake workflow management;
- Linux/HPC and SLURM familiarity;
- Git/GitHub organization; and
- reproducible scientific documentation.

## Limitations

- The included dataset is a small example feature matrix, not a clinical or research validation cohort.
- The current public evaluation uses a held-out test split rather than a complete cross-validation benchmark.
- The public repository does not reproduce the full original data-integration workflow.
- Example-data SHAP results are methodological illustrations, not biological findings.
- A complete public GO-enrichment analysis is not currently included.
- External validation and appropriate biological study design would be required before drawing scientific conclusions.

## Future Improvements

Potential improvements include:

- adding stratified or repeated cross-validation;
- adding hyperparameter tuning within cross-validation;
- strengthening missing-value and numeric-input validation;
- expanding automated tests;
- committing generated example metrics and figures; and
- adding a fully reproducible enrichment-analysis implementation when an appropriate public input gene list and background universe are available.

## Conclusion

This repository demonstrates how a compact biological machine-learning project can be structured as reproducible software. Its main strengths are leakage-aware preprocessing, model comparison, explainability, testing, CI, workflow automation, and HPC-aware execution. Broader Alzheimer's bioinformatics experience is described separately from the public implementation so that readers can clearly distinguish reproducible repository functionality from wider project context.
