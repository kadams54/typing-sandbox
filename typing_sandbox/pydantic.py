from typing import Optional, Sequence

from pydantic import BaseModel, Field


class Cat(BaseModel):
    age: int = Field(ge=0, lt=50)
    name: Optional[str]


class StrictCat(Cat):
    name: str


def echo(cats: Sequence[Cat]) -> Sequence[Cat]:
    return cats


def name(cats: Sequence[Cat]) -> Sequence[str]:
    return [c.name or "" for c in cats]


def run() -> None:
    cats: Sequence[StrictCat] = [
        StrictCat(age=4, name="Daisy"),
        StrictCat(age=6, name="Superman"),
    ]
    other_cats = echo(cats)
    print(name(other_cats))
    print(Cat.model_json_schema())
