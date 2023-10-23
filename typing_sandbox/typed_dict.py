from typing import TypedDict


class Cat(TypedDict, total=False):
    age: int
    name: str


class StrictCat(Cat, total=True):
    pass


def echo(cats: list[Cat]) -> list[Cat]:
    return cats


def name(cats: list[StrictCat]) -> list[str]:
    return [c["name"] for c in cats]


cats: list[StrictCat] = [
    {"age": 4, "name": "Daisy"},
    {"age": 6, "name": "Superman"},
]
other_cats = echo(cats)
print(name(other_cats))
