from typing import Optional, TypedDict


class Content(TypedDict):
    name: str


class Table(TypedDict):
    contents: list[Content]


class Room(TypedDict):
    table: Optional[Table]


class House(TypedDict):
    rooms: list[Room]
    address: str


house: House = {
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
