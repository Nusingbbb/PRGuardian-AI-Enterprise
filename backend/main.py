
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from services.gitlab_service import parse_gitlab_webhook, post_review_comments
from agents.langgraph_orchestrator import run_graph_pipeline
from db.storage import save_review_record, list_reviews

app = FastAPI(title="PRGuardian AI Pro")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status":"pro_ok"}

@app.get("/reviews")
def reviews():
    return list_reviews()

@app.post("/webhook/gitlab")
async def gitlab_webhook(req: Request):
    payload = await req.json()
    pr_data = parse_gitlab_webhook(payload)
    result = run_graph_pipeline(pr_data)
    post_review_comments(result["issues"])
    save_review_record(result)
    return result
