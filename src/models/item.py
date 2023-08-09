class Item:
    """Class representing an item listed"""

    def __init__(
        self, listing_id, price, title, title_translated=None, url=None
    ) -> None:

        self.listing_id = listing_id
        self.price = price
        self.title = title
        self.title_translated = title_translated
        self.url = url

    def __repr__(self) -> str:
        return self.listing_id
