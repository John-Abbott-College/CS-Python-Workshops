def foo(x, y):
    if (x == y):   # this is a style warning
        print(f"{x} and {y} are equal.")

def bar(x, y):
    if x == y:

    # a common
    # mistake
    # with indented
    # blocks
    # is when
    # there's comments between
    # the beginning of the block
    # and
    # the body
    print(f"{x} and {y} are equal.")

def garply(x, y):   # "garply" the forgotten meta-syntactic variable
    ultimate_equality_checker(x, y)  # ... too awesome for us!

def baz(x, y):
    if x == y:
        eq = True
    if eq:
        print(f"{x} and {y} are equal.")

if __name__ == "__main__":
    for f in [foo, bar, garply, baz]:
        f(1, 1)
