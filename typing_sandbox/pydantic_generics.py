from typing import Literal, Optional, TypeVar, Generic

from pydantic import BaseModel

T = TypeVar("T")


class Content(BaseModel, Generic[T]):
    value: T


class Room(BaseModel, Generic[T]):
    content: Optional[T]


class House(BaseModel):
    rooms: list[Room[Content[list[Content[Literal["fork", "spoon", "spork"]]]]]]
    address: str


data = {
    "address": "an-address",
    "rooms": [
        {
            "content": {
                "value": [
                    {
                        "value": "fork",
                    },
                    {
                        "value": "spork",
                    },
                ]
            }
        }
    ],
}

parsed_data = House(**data)
"""
House(
    rooms=[
        Room[Content[list[Content[Literal['fork', 'spoon', 'spork']]]]](
            content=Content[list[Content[Literal['fork', 'spoon', 'spork']]]](
                value=[Content[Literal['fork', 'spoon', 'spork']](value='fork'), Content[Literal['fork', 'spoon', 'spork']](value='spork')]
            )
        )
    ],
    address='an-address'
)
"""
