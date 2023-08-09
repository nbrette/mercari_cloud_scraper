import firebase_admin
from firebase_admin import firestore
from typing import Dict, List
from models.item import Item


class FirestoreHandler:
    """Class exposing the functions to interact with firestore"""

    # pylint: disable=invalid-name
    def __init__(self) -> None:
        firebase_admin.initialize_app()
        self.db = firestore.client()

    def get_listings(self, collection_name) -> Dict:
        """Get every listings for the collection in parameter and convert it to a dict"""
        listings = {}
        collection_ref = self.db.collection(collection_name)
        collection = collection_ref.get()
        for doc in collection:
            listings[doc.id] = doc.to_dict()

        return listings

    def batch_insert_listings(self, collection_name: str, listings: List[Item]):
        """Insert multiple listings into a firestore collection"""
        collection_ref = self.db.collection(collection_name)
        batch = self.db.batch()
        for listing in listings:
            doc_ref = collection_ref.document(listing.listing_id)
            batch.set(
                doc_ref,
                {
                    "id": listing.listing_id,
                    "price": listing.price,
                    "description": listing.listing,
                },
            )
        batch.commit()
