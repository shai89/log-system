from fastapi import FastAPI
from routes.log_routes import router as log_router

app = FastAPI(title="Log Ingestion MVP")

app.include_router(log_router, prefix="/logs")
