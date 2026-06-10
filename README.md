# Machine Learning Pipeline for Alzheimer’s Disease Gene Prediction

## Overview

This project focuses on building a machine learning pipeline to identify Alzheimer’s disease-associated genes by integrating public genomic, gene expression, and disease-association datasets. The workflow combines GWAS SNP profiles, GEO gene expression data, and DisGeNET disease-gene associations to create a unified feature set for disease gene prediction and biological interpretation.

The project demonstrates skills in bioinformatics, machine learning, genomic data integration, feature engineering, model evaluation, explainable AI, and biological validation.

## Objective

The goal of this project was to develop a reproducible machine learning workflow that could:

* Integrate GWAS, GEO, and DisGeNET datasets
* Harmonize high-dimensional genomic features
* Apply preprocessing, PCA, variance filtering, and batch correction
* Train and compare machine learning models
* Evaluate model performance using cross-validation
* Use SHAP explainability to identify high-impact features
* Interpret top genes using GO enrichment and literature review

## Background

Alzheimer’s disease is a complex neurodegenerative disorder influenced by genetic, transcriptomic, and biological pathway-level factors. Public genomic datasets can help identify genes that may contribute to disease risk or progression, but these datasets are often high-dimensional and require careful preprocessing before machine learning can be applied.

This project uses machine learning to explore disease-associated genomic patterns and connect model outputs to biological interpretation.

## Data Sources

This project used publicly available biological datasets and resources, including:

* GWAS SNP profiles related to Alzheimer’s disease
* GEO gene expression datasets
* DisGeNET disease-gene association data
* Gene Ontology resources for enrichment analysis
* Literature-based validation for biological interpretation

Note: Raw data files are not included in this repository. This repository focuses on the workflow, code structure, methodology, and reproducible project documentation.

## Tools and Technologies

### Programming and Workflow

* Python
* R
* SQL
* Linux/HPC
* Git/GitHub

### Machine Learning

* scikit-learn
* XGBoost
* Random Forest
* Support Vector Machine
* Deep learning classifiers
* SHAP

### Bioinformatics and Statistics

* GWAS data processing
* GEO gene expression analysis
* DisGeNET
* GO enrichment
* PCA
* Variance filtering
* Batch correction
* Feature engineering
* Cross-validation

## Workflow

### 1. Data Collection

Collected Alzheimer’s disease-related genomic and transcriptomic datasets from public databases. GWAS SNP profiles, GEO expression data, and DisGeNET disease associations were selected to represent different layers of disease-related biological information.

### 2. Data Cleaning and Preprocessing

Cleaned and standardized datasets before integration. This included checking missing values, formatting gene identifiers, removing incomplete records, and preparing feature tables for downstream analysis.

### 3. Feature Harmonization

Integrated multiple datasets into a unified machine learning-ready feature matrix. More than 30,000 genomic features were harmonized across the workflow.

### 4. Dimensionality Reduction

Applied PCA and variance filtering to reduce noise and improve computational efficiency. This step helped retain informative biological signals while reducing high-dimensional complexity.

### 5. Batch Correction

Applied batch correction strategies to reduce technical variation across datasets and improve reliability of downstream model training.

### 6. Model Development

Trained and compared multiple machine learning models, including:

* Random Forest
* XGBoost
* Support Vector Machine
* Deep learning classifiers

### 7. Model Evaluation

Used cross-validation to evaluate model performance. Models were compared using classification metrics including AUC, accuracy, sensitivity, specificity, and feature importance.

### 8. Explainable AI

Used SHAP explainability to identify high-impact features contributing to model predictions. This helped connect machine learning outputs to biologically meaningful genes.

### 9. Biological Interpretation

Performed Gene Ontology enrichment analysis and literature review to evaluate whether top-ranked genes were associated with Alzheimer’s disease mechanisms, neurodegeneration, immune response, inflammation, or related biological pathways.

### 10. HPC Execution

Automated data processing and model execution on Linux/HPC resources, reducing runtime from days to hours.

## Results

Key outcomes of the project included:

* Integrated GWAS, GEO, and DisGeNET datasets into a unified pipeline
* Harmonized 30,000+ genomic features
* Achieved cross-validation AUC above 0.90 across Random Forest, XGBoost, and deep learning models
* Used SHAP to identify high-impact genes
* Used GO enrichment and literature review for biological validation
* Reduced runtime from days to hours using HPC resources

## Key Skills Demonstrated

* Bioinformatics pipeline development
* Genomic data integration
* GWAS and gene expression analysis
* Machine learning for biological datasets
* Feature engineering and dimensionality reduction
* Model evaluation and cross-validation
* Explainable AI using SHAP
* GO enrichment and biological interpretation
* Linux/HPC workflow execution
* Reproducible research documentation

## Repository Structure

```text
alzheimers-gene-prediction-ml/
│
├── README.md
├── data_description.md
├── notebooks/
├── src/
├── figures/
├── results/
├── reports/
├── requirements.txt
└── LICENSE
```

## Suggested Folder Details

### notebooks/

Exploratory notebooks for preprocessing, modeling, and interpretation.

### src/

Reusable Python or R scripts for data cleaning, feature engineering, model training, and evaluation.

### figures/

Plots such as ROC curves, PCA plots, SHAP summary plots, and GO enrichment figures.

### results/

Model performance summaries, feature importance outputs, and enrichment results.

### reports/

Final project report or project summary PDF.

## Limitations

This project was based on public datasets, which may include technical noise, batch effects, population-specific biases, and incomplete metadata. The results should be interpreted as research-level findings and not as clinical predictions.

## Future Improvements

Future improvements could include:

* Adding more Alzheimer’s disease datasets
* Testing external validation cohorts
* Incorporating more omics layers such as proteomics or epigenomics
* Improving deep learning architectures
* Packaging the full workflow with Snakemake or Nextflow
* Creating an interactive dashboard for gene-level interpretation

## Portfolio Summary

This project demonstrates my ability to combine biological knowledge, public genomic data, machine learning, and explainable AI to analyze complex disease-related datasets. It reflects my interest in applying bioinformatics and computational biology to precision medicine, neurodegenerative disease research, and translational data science.

## Author

Hemalatha Ponnam
M.S. Bioinformatics & Computational Biology
Saint Louis University
Email: [hema22000latha@gmail.com](mailto:hema22000latha@gmail.com)
