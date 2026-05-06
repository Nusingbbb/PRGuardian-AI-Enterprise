
from agents.pr_diff_agent import analyze_diff
from agents.rulecheck_agent import run_rulecheck
from agents.architecture_agent import architecture_scan
from agents.llm_review_agent import llm_semantic_review
from agents.autofix_agent import generate_patch
from agents.ci_agent import run_ci_tests
from agents.summary_agent import build_summary

def run_graph_pipeline(pr_data):
    diff_report = analyze_diff(pr_data)
    issues = run_rulecheck(diff_report)
    arch = architecture_scan(diff_report)
    llm_issues = llm_semantic_review(diff_report)
    all_issues = issues + arch + llm_issues
    patches = generate_patch(all_issues)
    ci = run_ci_tests(patches)
    return build_summary(diff_report, all_issues, patches, ci)
