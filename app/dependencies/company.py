from fastapi import Header, HTTPException, status

#TODO: Later move to database
COMPANIES = {
    "pub_abc123": {"id": 1, "name": "Acme Corp"},
    "pub_xyz456": {"id": 2, "name": "Globex"},
}

def get_company(apiKey: str = Header(...)):
    company = COMPANIES.get(apiKey)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return company