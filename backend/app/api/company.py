from fastapi import APIRouter

from app.schemas.company import CompanyRequest
from app.services.company_service import (
    analyze_company , 
    get_analysis
)
router = APIRouter()

@router.post("/analyze")
def analyze(request: CompanyRequest):
    return analyze_company(request.company)
@router.get("/analysis/{analysis_id}")
def get_analysis_by_id(analysis_id: str):
    return get_analysis(analysis_id)