import uuid

from app.models.analysis import AnalysisSession
from app.database.session_store import analysis_sessions
from app.agents.news_agent import NewsAgent

def analyze_company(company_name: str):

    analysis = AnalysisSession(
        str(uuid.uuid4()),
        company_name,
        "analysis_started"
    )
    news_agent = NewsAgent()

    news_result = news_agent.analyze(company_name)

    analysis.news_result = news_result
    analysis_sessions[analysis.analysis_id]=analysis

    return {
        "analysis_id": analysis.analysis_id,
        "company": analysis.company,
        "status": analysis.status,
        "created_at": analysis.created_at,
        "news_result": analysis.news_result
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
        "status" : analysis.status,
        "created_at": analysis.created_at,
        "news_result": analysis.news_result
    }
