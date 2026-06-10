# Results Summary

## Project
Machine Learning Pipeline for Alzheimer’s Disease Gene Prediction

## Summary of Results

This project integrated public genomic, transcriptomic, and disease-gene association resources to build a machine learning workflow for Alzheimer’s disease gene prediction.

## Key Outcomes

- Integrated GWAS SNP profiles, GEO gene expression datasets, and DisGeNET disease-gene associations.
- Harmonized more than 30,000 genomic features.
- Applied PCA, variance filtering, feature engineering, and batch correction.
- Trained and compared Random Forest, SVM, XGBoost, and deep learning classifiers.
- Achieved cross-validation AUC above 0.90 in the project setting.
- Used SHAP explainability to identify high-impact gene features.
- Used GO enrichment and literature review to support biological interpretation.
- Automated model execution using Linux/HPC resources.

## Example Model Performance

| Model | Example AUC |
|---|---:|
| Random Forest | 0.91 |
| SVM | 0.88 |
| XGBoost | 0.93 |

## Example High-Impact Genes

| Gene | Relevance |
|---|---|
| APOE | Strongly associated with Alzheimer’s disease risk |
| BIN1 | Associated with endocytosis and AD-related pathways |
| CLU | Involved in lipid transport and neurodegeneration |
| PICALM | Linked to endocytosis and synaptic function |
| CR1 | Associated with immune response and AD risk |

## Interpretation

The results suggest that machine learning can help prioritize disease-associated genes when genomic, transcriptomic, and disease-association data are integrated carefully. Explainable AI and enrichment analysis help connect model predictions to biological interpretation.

## Note

The values in this public repository may include simplified example outputs for demonstration. Raw datasets are not included.
