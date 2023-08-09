from google.cloud import pubsub_v1
from typing import List
from models.item import Item
from config import Config


def publish_listings(data: bytes) -> str:
    """publish message in pubsub and return the ID of the message"""

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(Config.PROJECT_ID, Config.PUBSUB_TOPIC)
    print(topic_path)
    future = publisher.publish(topic_path, data)
    return future.result()


def format_data(listings: List[Item], set_name: str) -> bytes:
    """Format the new listings into a publishables pubsub message format"""

    # Convert the list of object into a list of dict
    list_item_dict = []
    for listing in listings:
        list_item_dict.append(vars(listing))

    dict_data = {"listings": list_item_dict, "set": set_name}

    # Convert data to bytes
    str_data = str(dict_data).replace("'", '"')
    return str_data.encode("utf-8")
