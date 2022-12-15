from datetime import datetime
from pydantic import BaseModel


class Request(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: datetime
