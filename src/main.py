from fastapi import FastAPI

from src.report.api.router import report

app = FastAPI()
app.include_router(report)