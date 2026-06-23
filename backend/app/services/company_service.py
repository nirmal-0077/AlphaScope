import uuid

from app.models.analysis import AnalysisSession
from app.database.session_store import analysis_sessions


def analyze_company(company_name: str):

    analysis = AnalysisSession(
        str(uuid.uuid4()),
        company_name,
        "analysis_started"
    )
    analysis_sessions[analysis.analysis_id]=analysis

    return {
        "analysis_id": analysis.analysis_id,
        "company": analysis.company,
        "status": analysis.status
    }

def get_analysis(analysis_id : str):
    analysis = analysis_sessions.get(analysis_id)
    if analysis is None:
        return{
             "error" : "Analysis not found"
        }
    
    return {
        "analysis_id":analysis.analysis_id,
        "company" : analysis.company,
        "status" : analysis.status
    }
