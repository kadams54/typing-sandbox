from typing import Any, Optional

from pydantic import BaseModel, ValidationError
from result import Err, Ok, Result
from rich import print


class Content(BaseModel):
    name: str


class Table(BaseModel):
    contents: list[Content]


class Room(BaseModel):
    table: Optional[Table]


class House(BaseModel):
    rooms: list[Room]
    address: str


def fetch_house(data: Any) -> Result[House, ValidationError]:
    try:
        house = House(**data)
    except ValidationError as error:
        return Err(error)
    return Ok(house)


def run() -> None:
    data = {
        "address": "1 Sample boulevard",
        "rooms": [
            {
                "table": {
                    "contents": [
                        {
                            "name": "Fork",
                        }
                    ]
                }
            }
        ],
    }

    house_1 = House(**data)
    print(house_1)
    # House(rooms=[Room(table=Table(contents=[Content(name='Fork')]))], address='1 Sample boulevard')

    fork = Content(name="Fork")
    spoon = Content(name="Spoon")
    table = Table(contents=[fork, spoon])
    dining_room = Room(table=table)
    bedroom = Room(table=None)
    house_2 = House(address="123 Main Street", rooms=[dining_room, bedroom])
    print(house_2)
    # House(rooms=[Room(table=Table(contents=[Content(name='Fork'), Content(name='Spoon')])), Room(table=None)], address='123 Main Street')
