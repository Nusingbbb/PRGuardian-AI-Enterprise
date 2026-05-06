
def parse_gitlab_webhook(payload):
    attrs = payload.get("object_attributes", {})
    return {
        "title": attrs.get("title","Demo PR"),
        "author": "demo_user",
        "changed_files": ["OrderService.java","PaymentDAO.java","InventoryService.java"],
        "insertions": 510,
        "deletions": 61,
        "diff": 'paymentResult.getCode().equals("S");\nselect * from orders;\nprintStackTrace();'
    }

def post_review_comments(issues):
    return True
