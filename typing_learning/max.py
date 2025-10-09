# adapted from https://jellis18.github.io/post/2022-01-11-abc-vs-protocol/

from typing import TypeVar, Protocol, Any


class ProtocolWithGreaterThan(Protocol):
    def __gt__(self, other: Any) -> bool:
        ...

T = TypeVar("T", bound=ProtocolWithGreaterThan)

class ClassWithCustomMax:
    def max(self, x: T, y: T) -> T:
        if x > y:
            return x
        return y

maxer = ClassWithCustomMax()
max_int = maxer.max(4, 5)
max_str = maxer.max("hello", "world!")

print(max_int)
print(max_str)