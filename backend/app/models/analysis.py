from datetime import datetime, timezone


class AnalysisSession:

    def __init__(
        self,
        analysis_id,
        company,
        status="created"
    ):
        self.analysis_id = analysis_id
        self.company = company
        self.status = status
        self.created_at = datetime.now(timezone.utc)
        self.news_result = None