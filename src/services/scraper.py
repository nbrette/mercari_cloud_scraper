from typing import List
from playwright.sync_api import sync_playwright, Page
from models.item import Item


class Scraper:
    """Scraper class for scraping mercari listings"""

    NEXT_BUTTON_SELECTOR = '[data-testid="pagination-next-button"]'
    LISTING_SELECTOR = '[data-testid="item-cell"]'
    MERCARI_BASE_URL = "https://jp.mercari.com/search?keyword="
    URL_SELECTOR = 'a[data-testid="thumbnail-link"]'
    PRICE_SELECTOR = 'span[class="number__6b270ca7"]'
    TITLE_SELECTOR = "div[class='imageContainer__f8ddf3a2']"

    def __init__(self):
        self.listings = []

    def get_page_listings(self, japanese_set_name: str, page_number=1) -> List[Item]:
        """make a research on mercari for the set in parameter and scrape the listings"""
        url = self._generate_mercari_url(japanese_set_name, page_number)
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_selector(self.LISTING_SELECTOR)
            listings = self._extract_items(page)
            next_page_exist = self._next_page_exist(page)

        return listings, next_page_exist

    def _next_page_exist(self, page: Page):
        """Check if the next page button exist"""
        next_button = page.query_selector(self.NEXT_BUTTON_SELECTOR)
        return bool(next_button)

    def _extract_items(self, page: Page) -> List[Item]:
        """Get the div containing every linstings and the extract data from those listings"""
        items = page.query_selector_all(self.LISTING_SELECTOR)
        extracted_items = []

        for item in items:
            link_element = item.query_selector(self.URL_SELECTOR)
            url_splitted = link_element.get_attribute("href").split("/")
            listing_id = url_splitted[-1]

            price_element = item.query_selector(self.PRICE_SELECTOR)
            price = price_element.text_content().replace(",", "")

            japanese_title_div = item.query_selector(self.TITLE_SELECTOR)
            japanese_title = japanese_title_div.query_selector("img").get_attribute(
                "alt"
            )

            extracted_item = Item(listing_id, price, japanese_title)
            extracted_items.append(extracted_item)

        return extracted_items

    def _generate_mercari_url(self, research: str, page_number: int) -> str:
        """Generate a URL for a mercari search with a keyword and a page number"""
        url = f"{self.MERCARI_BASE_URL}{research}&status=on_sale&sort=created_time&order=desc"
        if page_number > 1:
            url = f"{url}&page_token=v1%3A{page_number}"
        return url
