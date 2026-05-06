
import json, os
DB_FILE = "review_records.json"

def save_review_record(record):
    data = []
    if os.path.exists(DB_FILE):
        with open(DB_FILE,"r") as f:
            data = json.load(f)
    data.append(record)
    with open(DB_FILE,"w") as f:
        json.dump(data,f)

def list_reviews():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE,"r") as f:
        return json.load(f)
