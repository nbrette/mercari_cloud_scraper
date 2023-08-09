from fastapi import APIRouter

health_router = APIRouter()


@health_router.get("/")
def handle_healt_check():
    """Healt check to know if the service is ready to run"""

    return {"message": "Mercari scraper ready to run"}
