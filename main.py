from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine
from models import Base
from routers.dashboard import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mutual Fund Dashboard API",
    description=(
        "REST API powering the Mutual Fund Transaction Dashboard. "
        "Provides investor and mutual fund summaries filterable by date range."))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "message": "Mutual Fund Dashboard API is running."}