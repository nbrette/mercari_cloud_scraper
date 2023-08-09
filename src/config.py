import os


class Config:
    """Class exposing config variables required for the service"""

    PROJECT_ID = os.environ["PROJECT_ID"]
    PUBSUB_TOPIC = os.environ["PUBSUB_TOPIC"]
    PORT = int(os.getenv("PORT", "8080"))
