# Gene Ontology Enrichment Reproducibility Template

## Purpose

This file is a documentation template for a future reproducible Gene Ontology enrichment analysis. It does **not** report Alzheimer's disease enrichment results and should not be interpreted as biological evidence.

A complete enrichment analysis should record the following information so that another researcher can reproduce and evaluate the result.

## Required Inputs

- Input gene list
- Gene identifier type (for example, HGNC symbol, Ensembl ID, Entrez ID)
- Source of the gene list
- Date the gene list was generated
- Background or reference gene universe
- Inclusion and exclusion criteria

## Analysis Details

Document:

- Enrichment tool or library
- Tool version
- Gene Ontology release or database version
- Ontology category or categories used
- Statistical test
- Multiple-testing correction method
- Significance threshold
- Minimum and maximum gene-set sizes, if applicable
- Any filtering performed before or after enrichment

## Reproducible Outputs

Save machine-readable output containing at least:

- GO term ID
- GO term name
- ontology category
- raw p-value
- adjusted p-value / q-value
- overlap count
- background count or gene-set size
- overlapping input genes

## Interpretation Notes

When interpreting enrichment results:

- distinguish exploratory findings from validated biological conclusions;
- report the background universe used;
- avoid selecting terms only because they fit an expected narrative;
- account for multiple testing;
- retain complete machine-readable results, not only selected significant terms; and
- record database and software versions because enrichment results can change as annotations are updated.

## Public Repository Status

The current public repository does not contain a completed Alzheimer's disease GO-enrichment analysis. This template documents the reproducibility requirements that should be followed if such an analysis is added later using an appropriate public input gene list and background universe.
