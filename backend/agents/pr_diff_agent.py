def analyze_diff(pr_data):
    return {"changed_files_count":len(pr_data["changed_files"]),"risk_modules":pr_data["changed_files"],"raw_diff":pr_data["diff"]}
