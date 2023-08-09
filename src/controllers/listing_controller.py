from services.firestore_handler import FirestoreHandler
from services.scraper import Scraper
from models.sets import SetTranslastions, SetFsCollections
from googletrans import Translator
from typing import Dict


class ListingController:
    """Class exposing controller functions scraping and inserting data"""

    def __init__(self) -> None:
        self.fs_handler = FirestoreHandler()
        self.scraper = Scraper()

    def get_new_listings(self, set_name) -> Dict:
        """Get the listings for the first page of the mercacri research"""

        japanese_set_name = getattr(SetTranslastions, set_name).value
        listings, _ = self.scraper.get_page_listings(japanese_set_name)

        fs_collection_name = getattr(SetFsCollections, set_name).value

        fs_listings = self.fs_handler.get_listings(fs_collection_name)
        # Check if new listings scraped already exist in firestore
        new_listings = []
        translator = Translator()
        for listing in listings:
            if listing.listing_id not in fs_listings:
                translate_text = translator.translate(listing.title, dest="en")
                listing.title_translated = translate_text.text
                new_listings.append(listing)
        self.fs_handler.batch_insert_listings(fs_collection_name, new_listings)

        return {"listings": len(new_listings)}

    def get_every_listings(self, set_name) -> Dict:
        """Get every listings for the mercari research and insert them into firestore"""

        page_number = 1
        new_listings = []
        japanese_set_name = getattr(SetTranslastions, set_name).value
        fs_collection_name = getattr(SetFsCollections, set_name).value

        listings, next_page_exists = self.scraper.get_page_listings(japanese_set_name)
        new_listings.extend(listings)

        while next_page_exists:
            page_number += 1
            listings, next_page_exists = self.scraper.get_page_listings(
                japanese_set_name, page_number
            )
            new_listings.extend(listings)

        translator = Translator()
        for listing in new_listings:
            translate_text = translator.translate(listing.title, dest="en")
            listing.title_translated = translate_text.text

        self.fs_handler.batch_insert_listings(fs_collection_name, new_listings)

        return {"listings": len(new_listings)}
