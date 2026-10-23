import argparse, json, os, sys
from pathlib import Path
from evaluator.core import SUPPORTED, collect_submission, evaluate, load_problem
from evaluator.report_generator import write_reports

def choose_project_milestone(path, config):
    parts=[p.lower() for p in path.parts]
    projects=config.get("projects",{})
    project=next((p for p in projects if p.lower() in parts),config.get("default_project","Loan_Default"))
    rubrics=projects.get(project,{}).get("rubrics",{})
    milestone=next((m for m in rubrics if m.lower() in parts or m.lower() in path.name.lower()),config.get("default_milestone","Milestone_1"))
    return project,milestone

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--files-from",required=True)
    ap.add_argument("--output-dir",default="evaluation-reports")
    args=ap.parse_args()
    config=json.loads(Path("evaluator/config.json").read_text(encoding="utf-8"))
    paths=[Path(x.strip()) for x in Path(args.files_from).read_text(encoding="utf-8").splitlines() if x.strip()]
    candidates=[p for p in paths if p.exists() and p.is_file() and (p.suffix.lower() in SUPPORTED or p.suffix.lower()==".zip") and p.parts and p.parts[0]=="submission"]
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
