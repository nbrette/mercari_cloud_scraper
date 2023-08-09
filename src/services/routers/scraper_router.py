from fastapi import APIRouter
from models.mercari_body_request import MercariBodyRequest
from controllers.listing_controller import ListingController

scraper_router = APIRouter()


@scraper_router.post("/mercari/new")
def handle_scraper_mercari_new(body: MercariBodyRequest):
    """Route to scrape mercari listings"""
    controller = ListingController()
    return controller.get_new_listings(body.set_name.upper())


@scraper_router.post("/mercari/all")
def handle_scraper_mercari_all(body: MercariBodyRequest):
    """Route to scrape mercari listings"""
    controller = ListingController()
    return controller.get_every_listings(body.set_name.upper())
