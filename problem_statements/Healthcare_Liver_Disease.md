# Project: Healthcare Liver Disease Decision Support

## Business context
Build an educational analytics workflow using the provided liver-patient dataset and supporting lookup/education files. The work is for model development and learning, not clinical diagnosis or treatment.

## Data sources
Use the supplied files where available:
- `Liver Patient Dataset.csv`
- `Status.xlsx`
- `Cityname_statecode.xlsx`
- `Statecode_name.xlsx`
- `Healthcare_Education_Text.csv`

Inspect actual schemas and confirm join keys before joining. Verify the target encoding in the provided status file; do not assume undocumented mappings. Exclude identifiers from predictive features and check for leakage.

## Milestone 1: Data foundations
Profile data quality, analyze target balance and clinical-feature distributions, clean and engineer features, build a logistic-regression baseline, and evaluate with class-sensitive metrics.

## Milestone 2: Machine learning
Develop and compare classification models, tune them using stratified validation, analyze feature importance, and if requested produce clearly labelled illustrative risk scores or groups. Do not present unvalidated thresholds as clinical cut-offs.

## Milestone 3: Deep learning and text
Build and evaluate a neural-network classifier, compare it with a selected ML baseline on the same holdout, and complete a clearly defined NLP task using supplied healthcare education text.

## Milestone 4: Generative AI and agents
Provide cautious evidence-grounded explanations, RAG over approved education material, safe read-only SQL and tool orchestration. Evaluate privacy, fairness, grounding and unsafe clinical claims.

## Expected evidence
Data checks, documented target mapping, plots, leakage-aware preprocessing, confusion matrix, precision/recall/F1/ROC-AUC where appropriate, model comparison, text task evidence, source-grounded outputs and limitations.

## Safety constraints
This is not a medical device. Never claim a model diagnoses disease or recommend treatment. Protect patient information, discuss false negatives and bias, distinguish associations from causes, and require qualified clinical review for clinical decisions. Do not invent metrics or claim code was executed.