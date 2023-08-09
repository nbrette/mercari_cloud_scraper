import uvicorn
from services.routers.scraper_router import scraper_router
from services.routers.health_router import health_router

from fastapi import FastAPI
from config import Config

app = FastAPI()

app.include_router(scraper_router)
app.include_router(health_router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=Config.PORT, log_level="info")
