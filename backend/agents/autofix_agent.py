def generate_patch(issues):
    return [{"file":i["file"],"patch":"# auto generated patch"} for i in issues[:2]]
