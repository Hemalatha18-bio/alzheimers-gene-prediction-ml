#!/bin/bash
#SBATCH --job-name=alzheimers-ml-demo
#SBATCH --output=logs/alzheimers-ml-%j.out
#SBATCH --error=logs/alzheimers-ml-%j.err
#SBATCH --time=00:30:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G

# Generic demonstration only.
# Adjust modules, environment paths, partitions, and resource requests
# for the HPC system where this job is executed.

set -euo pipefail

mkdir -p logs results

# Example environment activation. Replace with the environment setup
# appropriate for the target cluster.
# source .venv/bin/activate

python src/model_pipeline.py \
  --input data/example_feature_matrix.csv \
  --pca-components 2 \
  --output results/model_metrics.json

python src/visualize_results.py \
  --metrics results/model_metrics.json \
  --output-dir figures
