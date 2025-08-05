# from a tutorial by Marco Gorelli: https://labs.quansight.org/blog/escaping-contravariance-hell

# from typing import Protocol, TypeVar
# from typing import Callable

# class Vegetable(Protocol): ...

# VegetableT = TypeVar('VegetableT', bound=Vegetable)

# class VegetablePeeler(Protocol[VegetableT]):
#     def peel(self, vegetable: VegetableT) -> VegetableT:
#         ...

# class Carrot(Vegetable):
#     ...

# # def carrot_func(vegetable: Carrot) -> None:
# #     return None

# # #vegetable: Vegetable = Carrot()

# # vegetable_func: Callable[[Vegetable], None] = carrot_func

# class CarrotPeeler(VegetablePeeler[Carrot]):
#     def peel(self, vegetable: Carrot) -> Carrot:
#         return vegetable

###########################

from typing import Protocol

class Vegetable(Protocol):
    ...

class VegetablePeeler[T: Vegetable](Protocol):
    def peel(self, vegetable: T) -> T: ...

class Carrot(Vegetable): ...

class CarrotPeeler(VegetablePeeler[Carrot]):
    def peel(self, vegetable: Carrot) -> Carrot:
        return vegetable