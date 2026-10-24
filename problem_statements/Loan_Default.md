# Project: Loan Default Prediction and Enterprise Risk Intelligence

## Business context
Develop a reproducible analytics workflow to understand loan-default patterns and support risk analysis. Predictions are decision-support evidence, not automatic lending decisions.

## Milestone 1: Data understanding and baseline
Inspect the supplied loan/default dataset and target definition. Profile data quality, analyze class balance and relationships, clean data, engineer appropriate features, build a logistic-regression baseline, and report confusion matrix, precision, recall, F1 and ROC-AUC where appropriate.

## Milestone 2: Machine learning and borrower segmentation
Develop and compare suitable ML classifiers, tune hyperparameters using cross-validation on training data, analyze feature importance carefully, and create borrower segments with suitable clustering methods. Explain trade-offs under class imbalance and the cost of false positives/false negatives.

## Milestone 3: Deep learning and NLP
Build a neural-network model for the defined default prediction target, compare it with a selected ML model on the same held-out data, assess overfitting, and implement a clearly defined NLP task using relevant supplied text where available.

## Milestone 4: Generative AI and agentic risk intelligence
Use LLMs to explain validated findings; implement RAG over approved policy documents with source citations; provide safe read-only Text-to-SQL; coordinate specialist tools/agents; and test grounding, query safety, privacy, fairness, uncertainty and prompt injection.

## Expected evidence
Notebook/code, schema and quality checks, documented target mapping, plots, leakage-aware preprocessing, model metrics, comparison tables, interpretations, validation evidence, limitations and reproducibility notes.

## Responsible use
Do not invent results, claim code was executed when it was not, or treat correlations as causation. Avoid exposing personal data. Model scores must not be presented as the sole basis for credit decisions. Human review is required.
