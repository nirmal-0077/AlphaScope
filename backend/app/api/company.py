from fastapi import APIRouter

from app.schemas.company import CompanyRequest
from app.services.company_service import analyze_company

router = APIRouter()

@router.post("/analyze")
def analyze(request: CompanyRequest):
    return analyze_company(request.company)