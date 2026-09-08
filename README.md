# Machine Learning Pipeline for Alzheimer's Disease Gene Prediction

## Overview

This portfolio repository presents a reproducible machine-learning demonstration for biological feature data, motivated by broader Alzheimer's disease bioinformatics work involving genomic, transcriptomic, and disease-gene association resources.

The **public repository intentionally focuses on a compact, executable demonstration** using an included example feature matrix. It is designed to show leakage-aware preprocessing, model comparison, explainability, testing, continuous integration, workflow management, and HPC-oriented execution practices.

The public example data and generated outputs are for software demonstration only. They should not be interpreted as clinical validation, biological findings, or evidence for Alzheimer's disease mechanisms.

## What the Public Repository Implements

The current public demo includes:

- CSV data loading and validation;
- stratified train/test splitting;
- leakage-aware preprocessing with scikit-learn pipelines;
- standardization and PCA fitted only on training data;
- Random Forest, Support Vector Machine, and XGBoost classification;
- ROC-AUC, accuracy, and classification-report export to JSON;
- figures generated from exported model metrics;
- a SHAP explainability demonstration on the example feature matrix;
- pytest-based automated tests;
- GitHub Actions continuous integration;
- a Snakemake workflow; and
- a generic SLURM submission example.

## Public Data Scope

The executable demo uses:

```text
data/example_feature_matrix.csv
```

This is a small example dataset intended to make the repository runnable without distributing research-scale biological data. See `data_description.md` for details about the public dataset and the distinction between the executable demo and broader project context.

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

### 1. Create an environment

```bash
git clone https://github.com/Hemalatha18-bio/alzheimers-gene-prediction-ml.git
cd alzheimers-gene-prediction-ml
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\activate`.

### 2. Run the model pipeline

```bash
python src/model_pipeline.py \
  --input data/example_feature_matrix.csv \
  --pca-components 2 \
  --output results/model_metrics.json
```

Scaling and PCA are fitted inside the model pipelines after the train/test split so preprocessing is learned from training data rather than the held-out test set.

### 3. Generate model-comparison figures

```bash
python src/visualize_results.py \
  --metrics results/model_metrics.json \
  --output-dir figures
```

The visualization script reads the exported model metrics rather than relying on hard-coded performance values.

### 4. Run the SHAP demonstration

```bash
python src/explain_model.py \
  --input data/example_feature_matrix.csv \
  --output figures/shap_summary.png
```

The SHAP output is a methodological demonstration using example data and should not be interpreted as biological evidence.

### 5. Run tests

```bash
pytest -q
```

GitHub Actions runs the test suite automatically on pushes and pull requests targeting `main`.

### 6. Run with Snakemake

```bash
snakemake --snakefile workflow/Snakefile --cores 1
```

The workflow connects the example feature matrix to model training and visualization. Configuration is stored in `workflow/config.yaml`.

### 7. HPC / SLURM example

A generic submission script is provided at:

```text
hpc/run_model.slurm
```

Cluster-specific modules, environments, paths, account/partition settings, and resource requests should be adapted to the target HPC system.

## Outputs

The public demonstration writes model metrics to:

```text
results/model_metrics.json
```

Model-comparison and SHAP demonstration figures are written under:

```text
figures/
```

Outputs generated from the included example data are demonstration results only.

## Broader Project Experience

The broader project work that motivated this repository involved experience with public biological resources and concepts such as genomic and transcriptomic data integration, disease-gene association resources, high-dimensional feature processing, dimensionality reduction, machine-learning experimentation, biological interpretation, enrichment-analysis concepts, and Linux/HPC execution.

Those broader activities are **project context and experience, not all reproducible components of this public repository**. Quantitative claims from broader work are intentionally not presented here unless the supporting data and analysis are available in the repository.

## Gene Ontology Enrichment Template

`examples/go_enrichment_template.md` documents the information a reproducible enrichment analysis should record, including the input gene list, identifier type, background universe, multiple-testing correction, database/tool versions, and machine-readable outputs.

It is a documentation template rather than an Alzheimer's enrichment result.

## Limitations

- The public demo uses a small example feature matrix rather than a research-scale cohort.
- The current model evaluation uses a held-out test split rather than a full cross-validation benchmark.
- The repository does not reproduce the complete original biological data-integration workflow.
- Example-data SHAP outputs are methodological illustrations, not biological findings.
- A fully reproducible enrichment analysis is not currently implemented.
- External validation would be required before drawing scientific or clinical conclusions.

## Future Improvements

- Add stratified or repeated cross-validation.
- Add hyperparameter tuning within cross-validation.
- Strengthen numeric and missing-value validation.
- Expand automated tests.
- Commit clearly labeled generated example metrics and figures.
- Add a fully reproducible enrichment implementation when an appropriate public gene list and background universe are available.

## Skills Demonstrated

Python scientific programming, machine-learning pipeline construction, leakage-aware preprocessing, model evaluation, explainability, automated testing, CI, workflow management, reproducibility practices, result visualization, Git/GitHub organization, and familiarity with Linux/HPC and SLURM concepts.

## Author

Hemalatha Ponnam  
M.S. Bioinformatics & Computational Biology  
Saint Louis University
