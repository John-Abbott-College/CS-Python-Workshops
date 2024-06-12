# import main1
# import main2
#
# print(f"I am {__name__}")


class Foo:

    def __init__(self):
        self._x = 0

    def __str__(self):

        self._x += 1
        return str(self._x)


def main():
    f: Foo = Foo()
    for i in range(10):
        print(str(f))
        print()

if __name__ == "__main__":
    main()