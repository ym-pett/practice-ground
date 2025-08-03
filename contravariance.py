# from a tutorial by Marco Gorelli: https://labs.quansight.org/blog/escaping-contravariance-hell

from typing import Protocol
from typing import Callable

class Vegetable(Protocol): ...

class Carrot(Vegetable):
    ...

def carrot_func(vegetable: Carrot) -> None:
    return None

vegetable_func: Callable[[Vegetable], None] = carrot_func