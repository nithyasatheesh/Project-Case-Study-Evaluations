# Project: Retail Customer Purchase Intelligence

## Business context
A retailer wants to understand customer purchase behaviour and improve data-informed marketing and merchandising decisions using customer demographics, product-purchase records and customer reviews.

## Data sources
Use the project-provided data files where available:
- `user_demographics.csv`
- `User_product_purchase_details.csv`
- `Customer_Reviews.csv`

Verify the actual column names, identifiers, key uniqueness and relationships before joining. Do not assume keys or column types without inspecting the files.

## Milestone 1: Data foundations
Profile data quality, conduct exploratory analysis, clean and engineer features, build a regression baseline for the purchase amount, and evaluate it with suitable regression metrics.

## Milestone 2: Machine learning
Develop and compare multiple regression models, tune hyperparameters with appropriate validation, analyze feature importance cautiously, and create customer segments from aggregated purchase behaviour.

## Milestone 3: Deep learning and text
Develop a neural-network regression model, compare it with the best machine-learning baseline on the same holdout, and perform a clearly defined NLP task on customer reviews. If labels are absent, do not fabricate supervised metrics.

## Milestone 4: Generative AI and agents
Use an LLM to explain validated findings; implement grounded RAG over approved retail reference material; provide safe read-only Text-to-SQL; orchestrate tools/agents; evaluate grounding, privacy, fairness and prompt-injection resistance.

## Expected evidence
Notebook/code, data-quality findings, plots, documented preprocessing, model metrics, comparison tables, interpretations, reproducibility notes and limitations. The evaluator must score only evidence actually present and must not claim code was executed.

## Constraints
Do not expose personal customer records unnecessarily. Correlation is not causation. Do not invent metrics, dataset fields, source documents or results. Human review is required.