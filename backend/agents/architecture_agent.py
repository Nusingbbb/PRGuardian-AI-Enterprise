
def architecture_scan(diff_report):
    risks = []
    for mod in diff_report["risk_modules"]:
        risks.append({"type":"Architecture Risk","file":mod,"line":1,"comment":"Cross-layer invocation detected, verify service boundary"})
    return risks
