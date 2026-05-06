def build_summary(diff_report, issues, patches, ci_result):
    return {"risk_level":"HIGH","issues_found":len(issues),"patches_generated":len(patches),"ci_result":ci_result,"issues":issues,"patches":patches,"message":"PRGuardian AI Pro review completed"}
