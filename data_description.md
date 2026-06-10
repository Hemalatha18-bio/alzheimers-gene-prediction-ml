# Data Description

## Project

Machine Learning Pipeline for Alzheimer’s Disease Gene Prediction

## Overview

This project uses public biological datasets to explore Alzheimer’s disease-associated genes through machine learning and bioinformatics analysis. The workflow integrates genomic, transcriptomic, and disease-association resources to create a unified feature set for model training and biological interpretation.

## Data Types Used

This project is based on three major types of biological data:

### 1. GWAS Data

Genome-wide association study data were used to represent genetic variants associated with Alzheimer’s disease. These data help identify SNPs and genomic regions that may be linked to disease risk.

Examples of information used from GWAS-style data:

* SNP identifiers
* Gene mappings
* Disease-associated loci
* Genomic features
* Variant-level association information

### 2. GEO Gene Expression Data

Gene Expression Omnibus datasets were used to represent transcriptomic changes associated with Alzheimer’s disease or related biological conditions. Gene expression data help identify genes that are differentially expressed or biologically relevant in disease contexts.

Examples of information used from GEO-style data:

* Gene expression values
* Sample metadata
* Disease/control grouping
* Normalized expression matrices
* Gene identifiers

### 3. DisGeNET Disease-Gene Association Data

DisGeNET disease-gene association information was used to connect genes with known disease relevance. These associations helped support biological interpretation and feature prioritization.

Examples of information used from DisGeNET-style data:

* Disease-associated genes
* Gene-disease scores
* Literature-supported disease associations
* Biological relevance annotations

## Additional Biological Resources

The project also used biological annotation and interpretation resources such as:

* Gene Ontology enrichment resources
* NCBI gene information
* Published literature
* Disease pathway references

## Data Availability

Raw data files are not included in this repository.

This repository is intended to demonstrate the project workflow, methodology, analysis structure, and reproducible documentation. Public datasets should be downloaded directly from their original sources when reproducing or extending this project.

## Why Raw Data Is Not Included

Raw data are not included because:

* Some public datasets are large.
* Dataset access and usage terms may vary by source.
* Repositories should avoid unnecessary storage of large biological datasets.
* The purpose of this repository is to document the analysis workflow and reproducible structure.

## Reproducibility Notes

To reproduce a similar workflow, users should:

1. Download Alzheimer’s-related GWAS data from a public GWAS resource.
2. Download Alzheimer’s-related gene expression datasets from GEO.
3. Retrieve disease-gene association data from DisGeNET or a similar public database.
4. Standardize gene identifiers across datasets.
5. Merge features into a unified analysis table.
6. Apply preprocessing, PCA, variance filtering, and batch correction.
7. Train machine learning models.
8. Use SHAP and GO enrichment for biological interpretation.

## Example Feature Categories

The final machine learning feature matrix may include:

* SNP-associated gene features
* Gene expression values
* Disease-gene association scores
* Normalized genomic features
* PCA-transformed features
* Filtered high-variance biological features

## Data Processing Summary

The data processing workflow included:

* Dataset cleaning
* Missing value handling
* Gene identifier standardization
* Feature harmonization
* Variance filtering
* PCA
* Batch correction
* Model-ready table generation

## Ethical and Privacy Considerations

This project uses public biological research datasets. No private patient records, protected health information, or confidential clinical data are included in this repository.

## Suggested Citation Statement

If using public datasets, cite the original data sources, including the relevant GWAS source, GEO accession numbers, DisGeNET database, and any enrichment resources used in the analysis.

## Author

Hemalatha Ponnam
M.S. Bioinformatics & Computational Biology
Saint Louis University
Email: [hema22000latha@gmail.com](mailto:hema22000latha@gmail.com)
