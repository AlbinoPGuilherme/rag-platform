from fastapi import FastAPI

app = FastAPI(title="RAG Platform API")

@app.get("/health")
def health():
    return {"status": "ok"}