import argparse, json, os, sys
from pathlib import Path
from evaluator.core import SUPPORTED, collect_submission, evaluate, load_problem
from evaluator.report_generator import write_reports

def choose_project_milestone(path, config):
    path_text = path.as_posix().lower().replace('-', '_')
    filename = path.stem.lower().replace('-', '_')
    project_configs = config.get('projects', {})
    aliases = [
        (('retail_purchase', 'retail_customer_purchase', 'customer purchase intelligence', 'user_product_purchase_details'), 'Retail_Customer_Purchase'),
        (('healthcare', 'liver_disease', 'liver disease', 'liver patient dataset'), 'Healthcare_Liver_Disease'),
        (('forecasting', 'sales_forecasting', 'retail sales forecasting', 'retail_data.csv'), 'Retail_Sales_Forecasting'),
        (('loan_default', 'loandefault'), 'Loan_Default'),
    ]
    project = None
    for keywords, configured_name in aliases:
        if configured_name in project_configs and any(k in filename or k in path_text for k in keywords):
            project = configured_name
            break
    if project is None and path.suffix.lower() in {'.ipynb', '.py', '.md', '.txt', '.json', '.html'}:
        try:
            sample = path.read_text(encoding='utf-8', errors='replace')[:12000].lower()
            for keywords, configured_name in aliases:
                if configured_name in project_configs and any(k in sample for k in keywords):
                    project = configured_name
                    break
        except OSError:
            pass
    if project is None:
        raise ValueError(f"Cannot identify project for '{path}'. Add a project keyword to the filename or include the project title in the notebook; refusing to default silently to Loan_Default.")
    milestone = None
    for i in range(1, 5):
        if f'milestone_{i}' in path_text or f'milestone{i}' in path_text or f'_m{i}_' in filename:
            milestone = f'Milestone_{i}'
            break
    if milestone is None:
        milestone = config.get('default_milestone', 'Milestone_1')
    if milestone not in project_configs[project].get('rubrics', {}):
        raise ValueError(f'No rubric configured for {project}/{milestone}')
    return project, milestone

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--files-from",required=True)
    ap.add_argument("--output-dir",default="evaluation-reports")
    args=ap.parse_args()
    config=json.loads(Path("evaluator/config.json").read_text(encoding="utf-8"))
    paths=[Path(x.strip()) for x in Path(args.files_from).read_text(encoding="utf-8").splitlines() if x.strip()]
    candidates=[p for p in paths if p.exists() and p.is_file() and (p.suffix.lower() in SUPPORTED or p.suffix.lower()==".zip") and p.parts and p.parts[0].lower() in {"submission", "submission-milestone1", "submission-milestone2", "submission-milestone3", "submission-milestone4"}]
    if not candidates:
        print("No supported changed submission files."); return 0
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY secret is missing.",file=sys.stderr); return 2
    for p in candidates:
        project,milestone=choose_project_milestone(p,config)
        pc=config.get("projects",{}).get(project,{})
        rubric_path=pc.get("rubrics",{}).get(milestone)
        if not rubric_path or not Path(rubric_path).exists():
            print(f"Skipping {p}: rubric not configured for {project}/{milestone}."); continue
        rubric=json.loads(Path(rubric_path).read_text(encoding="utf-8"))
        problem=load_problem(pc.get("problem_statement"))
        evidence,included=collect_submission([p],int(config.get("max_file_chars",18000)),int(config.get("max_total_chars",45000)))
        if not evidence.strip(): print(f"Skipping {p}: no text extracted."); continue
        result=evaluate(evidence,rubric,problem,config.get("model","gpt-4.1-mini"))
        xlsx,js=write_reports(result,p.as_posix(),args.output_dir)
        print(f"{p}: {result['total_marks']}/{result['maximum_marks']} | {xlsx} | {js}")
    return 0

if __name__=="__main__": raise SystemExit(main())
