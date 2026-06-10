from fastapi import FastAPI

app = FastAPI(
    title="AlphaScope API",
    description="AI-Powered Market Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to AlphaScope"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "AlphaScope"
    }