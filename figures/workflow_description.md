# Workflow Description

## Machine Learning Pipeline for Alzheimer’s Disease Gene Prediction

The project workflow follows these major steps:

```text
Public Data Sources
        |
        |-- GWAS SNP Profiles
        |-- GEO Gene Expression Data
        |-- DisGeNET Disease-Gene Associations
        |
        v
Data Cleaning and Standardization
        |
        |-- Missing value handling
        |-- Gene identifier formatting
        |-- Metadata organization
        |
        v
Feature Harmonization
        |
        |-- Merge genomic features
        |-- Create model-ready feature matrix
        |-- Harmonize 30,000+ features
        |
        v
Preprocessing
        |
        |-- Variance filtering
        |-- PCA
        |-- Batch correction
        |-- Feature scaling
        |
        v
Machine Learning
        |
        |-- Random Forest
        |-- SVM
        |-- XGBoost
        |-- Deep learning classifiers
        |
        v
Model Evaluation
        |
        |-- Cross-validation
        |-- AUC
        |-- Accuracy
        |-- Sensitivity / specificity
        |
        v
Explainable AI
        |
        |-- SHAP values
        |-- Feature importance
        |-- Top gene ranking
        |
        v
Biological Interpretation
        |
        |-- GO enrichment
        |-- Literature review
        |-- Disease pathway interpretation
