from enum import Enum


class SetTranslastions(Enum):
    """Enums representing the pokemon set names in english and japanese"""

    JUNGLE = "ポケモンジャングル"
    FOSSIL = ""
    TEAM_ROCKET = ""


class SetFsCollections(Enum):
    """Enum representing the pokemon sets names and the correspondind firestore collection name"""

    JUNGLE = "JUNGLE_LISTINGS"
    FOSSIL = "FOSSIL_LISTINGS"
    TEAM_ROCKET = "TEAM_ROCKET_LISTINGS"
