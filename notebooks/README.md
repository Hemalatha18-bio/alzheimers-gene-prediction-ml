# Notebooks

This folder contains exploratory analysis notebooks for the Alzheimer’s disease gene prediction project.

## Planned Notebooks

### 1. data_preprocessing.ipynb
This notebook will include:
- Loading GWAS, GEO, and DisGeNET datasets
- Cleaning missing values
- Standardizing gene identifiers
- Merging feature tables
- Preparing model-ready datasets

### 2. feature_engineering.ipynb
This notebook will include:
- Variance filtering
- PCA
- Batch correction
- Feature scaling
- Model-ready feature matrix creation

### 3. model_training.ipynb
This notebook will include:
- Random Forest model training
- SVM model training
- XGBoost model training
- Cross-validation
- Model performance comparison

### 4. shap_interpretation.ipynb
This notebook will include:
- SHAP value calculation
- Top gene feature ranking
- Feature importance visualization
- Biological interpretation of important genes

### 5. go_enrichment_analysis.ipynb
This notebook will include:
- Gene list preparation
- GO enrichment analysis
- Pathway-level interpretation
- Literature-supported biological validation

## Note

Raw datasets are not included in this repository. Notebooks should be run using public datasets downloaded from their original sources or synthetic/demo data provided for portfolio demonstration.
