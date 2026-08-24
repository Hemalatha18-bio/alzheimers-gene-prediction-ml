# Machine Learning Pipeline for Alzheimer's Disease Gene Prediction

## Overview

This portfolio project documents a machine-learning workflow for exploring Alzheimer's disease-associated genomic patterns using public biological data sources. The broader project methodology includes genomic/transcriptomic integration, dimensionality reduction, model comparison, explainability, biological interpretation, and Linux/HPC execution.

The **public repository is a reproducible demonstration of selected workflow components**. Raw research datasets are not distributed here, and the included example feature matrix is intended for code demonstration rather than clinical or research validation.

## Public Repository Scope

The public demo includes:

- CSV data loading and validation;
- leakage-safe train/test preprocessing with scikit-learn pipelines;
- Random Forest, SVM, and XGBoost classification;
- AUC, accuracy, and classification-report export to JSON;
- figures generated directly from exported metrics;
- pytest-based automated tests;
- GitHub Actions continuous integration;
- a generic SLURM submission example;
- a Snakemake workflow for model training and visualization;
- a SHAP explainability demonstration using the example feature matrix; and
- a documented GO-enrichment reproducibility template.

The public examples are portfolio demonstrations. They should not be interpreted as clinical validation or as evidence for Alzheimer's disease mechanisms.

## Data Sources and Privacy

The broader project methodology drew on publicly available biological resources such as GWAS studies, GEO expression datasets, disease-gene association resources, Gene Ontology resources, and scientific literature.

Raw research datasets are not included. Small example or synthetic files may be included solely to demonstrate code execution. See `data_description.md` for additional notes.

## Technologies

- Python
- pandas / NumPy
- scikit-learn
- XGBoost
- matplotlib
- SHAP
- pytest
- Snakemake
- GitHub Actions
- Linux/HPC
- SLURM
- Git/GitHub

## Repository Structure

```text
alzheimers-gene-prediction-ml/
├── .github/workflows/ci.yml
├── README.md
├── data_description.md
├── requirements.txt
├── data/
│   └── example_feature_matrix.csv
├── src/
│   ├── model_pipeline.py
│   ├── visualize_results.py
│   └── explain_model.py
├── tests/
│   └── test_model_pipeline.py
├── hpc/
│   └── run_model.slurm
├── workflow/
│   ├── Snakefile
│   └── config.yaml
├── examples/
│   └── go_enrichment_template.md
├── figures/
├── results/
├── reports/
├── notebooks/
└── LICENSE
```

## How to Run

### Environment

```bash
git clone https://github.com/Hemalatha18-bio/alzheimers-gene-prediction-ml.git
cd alzheimers-gene-prediction-ml
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate with `.venv\\Scripts\\activate`.

### Model pipeline

```bash
python src/model_pipeline.py \
  --input data/example_feature_matrix.csv \
  --pca-components 2 \
  --output results/model_metrics.json
```

Scaling and PCA are fitted only on training data through model pipelines to reduce preprocessing leakage into the held-out test set.

### Visualize exported metrics

```bash
python src/visualize_results.py \
  --metrics results/model_metrics.json \
  --output-dir figures
```

### Run tests

```bash
pytest -q
```

### SHAP demonstration

```bash
python src/explain_model.py \
  --input data/example_feature_matrix.csv \
  --output figures/shap_summary.png
```

This is an explainability demonstration on example data, not a biological interpretation of Alzheimer's disease.

### Snakemake workflow

```bash
snakemake --snakefile workflow/Snakefile --cores 1
```

The workflow connects the example feature matrix to model training and metric visualization. Configuration is stored in `workflow/config.yaml`.

### HPC / SLURM example

A generic submission script is provided at `hpc/run_model.slurm`. Cluster-specific modules, environments, resource requests, paths, and policies must be adapted to the target system.

## Continuous Integration

`.github/workflows/ci.yml` runs the test suite on pushes and pull requests targeting `main`. This provides an automated check that the public code remains testable as the repository changes.

## Gene Ontology Enrichment

`examples/go_enrichment_template.md` documents what a reproducible GO-enrichment extension should record, including the input gene list, identifier type, background universe, multiple-testing correction, database/tool versions, and complete machine-readable outputs.

It intentionally does **not** contain fabricated Alzheimer's enrichment results.

## Outputs

Model metrics are written to `results/model_metrics.json`. Model-comparison and SHAP demonstration figures are written under `figures/` when the corresponding scripts are run.

## Broader Project Context

The broader project work included multi-source biological data integration, high-dimensional feature processing, model experimentation, biological interpretation, and use of Linux/HPC resources. Quantitative claims are not presented as reproducible public-demo results unless the corresponding data and analysis are available in this repository.

## Limitations

- The public demo is not a clinical prediction system.
- Example/synthetic data cannot establish biological validity or clinical performance.
- SHAP explanations from demonstration data are methodological examples, not biological findings.
- The GO-enrichment file is a reproducibility template, not an Alzheimer's enrichment result.
- External validation would be required before drawing scientific conclusions.

## Possible Future Extensions

- Add cross-validation and hyperparameter tuning.
- Add richer logging and additional input validation.
- Add a fully reproducible GO-enrichment implementation when an appropriate public gene list and background universe are available.
- Expand workflow orchestration if the public demo grows beyond the current compact pipeline.

## Skills Demonstrated

Python scientific programming, machine-learning pipeline construction, leakage-aware preprocessing, model evaluation, explainability, automated testing, CI, workflow management, reproducibility practices, result visualization, Git/GitHub organization, and familiarity with Linux/HPC and SLURM concepts.

## Author

Hemalatha Ponnam  
M.S. Bioinformatics & Computational Biology  
Saint Louis University
