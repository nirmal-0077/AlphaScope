from app.services.news_service import fetch_company_news


class NewsAgent:

    def analyze(self, company_name: str):

        articles = fetch_company_news(company_name)

        result = {
            "agent": "news_agent",
            "company": company_name,
            "status": "completed",
            "articles": articles
        }

        return result