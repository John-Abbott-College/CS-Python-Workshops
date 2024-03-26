from typing import TypeVar, Protocol

from our_array import Array
from our_stack import Stack


# who can many pop?
def many_pop(collection, amount):
    """Remove (pop) and discard a specific number of items from the collection."""
    for i in range(amount):
        if len(collection) == 0:
            return
        collection.pop()


def demo_protocol_hinting():
    s: Stack[int] = Stack(10)
    a: Array[int] = Array(10)
    l: list[int] = []

    for i in range(10):
        l.append(i)
        a[i] = i
        s.push(i)

    print(many_pop(s, 15))
    print(many_pop(l, 15))
    print(many_pop(a, 15))


# Ian is still stuck on generics and protocols/interfaces...
# T = TypeVar("T")
#
#
# class Popable(Protocol[T]):
#     def pop(self) -> T:
#         pass
#
#     def __len__(self) -> int:
#         pass
#

if __name__ == "__main__":
    demo_protocol_hinting()
