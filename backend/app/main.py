from fastapi import FastAPI

# Uvicorn looks for this exact module-level name: app.main:app
app = FastAPI(title="Learning Tracker API")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Learning Tracker API is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}