# Project Report: Machine Learning Pipeline for Alzheimer’s Disease Gene Prediction

## Author
Hemalatha Ponnam

## Background

Alzheimer’s disease is a complex neurodegenerative disorder with genetic, transcriptomic, and pathway-level contributors. Public biological datasets such as GWAS, GEO, and DisGeNET can be used to explore disease-associated genes, but these datasets require careful preprocessing and integration.

## Objective

The objective of this project was to build a reproducible machine learning pipeline to predict Alzheimer’s disease-associated genes and interpret important biological features.

## Methods

The workflow included:

1. Collection of public GWAS, GEO, and DisGeNET datasets.
2. Cleaning and harmonization of gene-level features.
3. Preprocessing using PCA, variance filtering, and batch correction.
4. Training machine learning models including Random Forest, SVM, XGBoost, and deep learning classifiers.
5. Evaluating model performance using cross-validation.
6. Interpreting important features using SHAP.
7. Validating biological relevance using GO enrichment and literature review.

## Results

The project harmonized more than 30,000 genomic features and achieved cross-validation AUC above 0.90 across multiple machine learning models in the project setting. SHAP explainability helped identify high-impact gene features, and GO enrichment supported biological interpretation.

## Skills Demonstrated

- Bioinformatics pipeline development
- GWAS and gene expression data integration
- Machine learning model development
- High-dimensional data preprocessing
- Python/R analysis
- Linux/HPC workflow execution
- SHAP explainability
- GO enrichment
- Scientific reporting

## Conclusion

This project demonstrates the use of machine learning and bioinformatics methods to integrate public disease-related datasets and identify biologically meaningful gene features associated with Alzheimer’s disease.
