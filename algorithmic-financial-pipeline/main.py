from fastapi import FastAPI
from app.api.v1.endpoints.company import router as company_router
from app.db.database import engine
from app.models.company_model import Base

app = FastAPI(
    title="Algorithmic Financial Processing Pipeline",
    version="1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(company_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Financial Processing API Running"}