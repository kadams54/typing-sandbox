from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass
class Cat:
    age: int
    name: Optional[str]


@dataclass
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
