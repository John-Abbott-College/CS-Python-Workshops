
def foo(x, y):
    return x + y


def bar(x: int, y: int) -> int:
    return x + y


def demo_hinting():
    print(foo(1, 3))
    print(foo("a", "b"))
    print(bar(3, 1.2))
    print(bar(3, "a"))


if __name__ == "__main__":
    demo_hinting()
