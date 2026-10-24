# Project: Retail Sales Forecasting and Business Intelligence

## Business context
Forecast retail sales over time to support inventory planning and operational decision-making.

## Data sources
Use the supplied files where available:
- `retail_data.csv`
- `Retail_Forecasting_Education_Text.csv`

Inspect the actual schema, date range, frequency, store/item identifiers, target units and missing-period meaning. Do not assume a missing date represents zero sales unless the source supports that interpretation.

## Milestone 1: Data foundations
Validate time-series data, perform trend/seasonality EDA, engineer calendar features, create naive or seasonal-naive baselines, and evaluate a baseline regression/forecasting model using chronological splits.

## Milestone 2: Machine learning
Build models using lag, rolling and calendar features derived only from past data; tune using time-aware validation; compare with simple baselines; inspect feature importance and residuals by store/item.

## Milestone 3: Deep learning
Build a feed-forward or sequence neural model, construct sequences chronologically, fit scaling on training data only, and compare against ML and naive baselines on the same future holdout.

## Milestone 4: Generative AI and agents
Use an LLM to summarize validated forecast results, implement grounded RAG over approved forecasting material, provide safe read-only Text-to-SQL, orchestrate data/retrieval/summary tools, and evaluate grounding and time-period correctness.

## Expected evidence
Date validation, time-series plots, leakage-aware feature engineering, baseline and model metrics (MAE/RMSE/sMAPE as appropriate), chronological validation, residual analysis, model comparisons and limitations.

## Constraints
Clearly distinguish historical actuals from forecasts and identify the forecast horizon. Do not invent forecast values or claim causal impact, savings or improved inventory performance without evidence. Do not claim code was executed.