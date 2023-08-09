from pydantic import BaseModel, validator
from .sets import SetTranslastions


class MercariBodyRequest(BaseModel):
    """Body for the /mercari/* routes"""

    set_name: str

    @validator("set_name")
    # pylint: disable=missing-function-docstring,no-self-argument
    def validate_set_name_exists(cls, value):
        if not any(value.upper() == item.name for item in SetTranslastions):
            raise ValueError(f"{value} is not a valid set name")
        return value
