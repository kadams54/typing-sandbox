from typing import Sequence, TypedDict


class Cat(TypedDict, total=False):
    age: int
    name: str


class StrictCat(Cat, total=True):
    pass


def echo(cats: Sequence[Cat]) -> Sequence[Cat]:
    return cats


def name(cats: Sequence[StrictCat]) -> Sequence[str]:
    return [c.get("name", "") for c in cats]


def run():
    cats: Sequence[StrictCat] = [
        {"age": 4, "name": "Daisy"},
        {"age": 6, "name": "Superman"},
    ]
    other_cats = echo(cats)
    print(name(other_cats))
