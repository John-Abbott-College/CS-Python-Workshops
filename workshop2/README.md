-   Iterator pattern is important, since iterators are standard way of
    looping in python.
-   Some techniques in iterators.
-   Iterable vs. Iterator:
-   Iterator vs. generator: a basic survival guide

# Why iterators?

-   Start looping early and keep looping simple (at first) with
    iterables.
-   Be ready for submissions that use iterators and generators that
    students find online/AI.
-   Be more pythonic in our coding, including starter code and grading
    code.

# From while to for-each

## Good ol\' while

``` python
def buy_groceries_v1(grocery_list: list):
    i: int = 0
    while i < len(grocery_list):
        item = grocery_list[i]
        print(f"Remember to buy {item}")
        i = i + 1
```

-   It\'s not direct, a lot of the code is \"plumbing\" to get us the
    next position in the list.
-   It\'s concept heavy: integers, conditions, booleans, comparisons,
    assignment and reassignment, array access, and state of execution.
-   It\'s what actually happens when you iterate over an array in
    imperative programming.

## For loops

Python doesn\'t have traditional for loops, so our version 2 will come
from Java:

``` java
void buy_groceries_v2(List grocery_list) {
    for(int i = 0; i < grocery_list.size(); i = i + 1)
        System.out.println("Remember to buy " + item)

```

-   This is just syntactic \"sugar\" for the while loop, so has the same
    features with a more compact notation.

## \"for\" loops in python

We can recreate the \"for\" loop in python with a `range`.

``` python
def buy_groceries_v3(grocery_list: list):
    for i in range(len(grocery_list)):
        item = grocery_list[i]
        print(f"Remember to buy {item}")
```

There is a lot of differences between this an traditional `for` loops,
but let\'s first discuss the pros and cons.

### Pros

-   The need to manage `i`\'s state is removed.
-   No more condition.

### Cons

-   There is the need to understand ranges.
-   The syntax for accessing list elements is still required.

## \"for-each\" loops

Since we\'re only interested in accessing the list sequentially, we can
just:

``` python
def buy_groceries_v4(grocery_list: list):
    for item in grocery_list:
        print(f"Remember to buy {item}")
```

Now there\'s no need for integers or even that a list is indexable.

Notes:

-   The `for` statement in python is just a for-each. The for loop
    behaviour is identical for both version 3 and version 4.
-   `range` and `list` are both examples of *iterables*.

## How to conceptually \"read\" for loops

``` python
for var_name in iterable_thing:
    code_statements    
```

`for var_name in`

:   the variable/name will be assigned to each element in the iterable.

`in iterable_thing`

:   the iterable produces a stream of values.

`code_statements`
:   the statement(s) that execute for each assignment of `var_name` to a
    value produced by `iterable_thing`

It is more intuitive to new programmers what\'s going on here:

``` python
for item in grocery_list:
    print(f"Remember to buy {item}")
```

compared to what where we started:

``` python
i: int = 0
while i < len(grocery_list):
    item = grocery_list[i]
    print(f"Remember to buy {item}")
    i = i + 1
```

## References

<https://www.youtube.com/watch?v=EnSu9hHGq5o>

# Many iterables

What the iterable *is* determines what stream of values will be produced
in the loop.

``` {.python results="output"}
l: list = [2, 3, 4, 5, 6]
for x in l:
    print(x)
```

``` {.python results="output"}
r: range = range(1, 11, 2) 
for x in r:
    print(x)
```

``` {.python results="output"}
s: str = "hello"
for x in s:
    print(x)
```

``` {.python results="output"}
t: tuple = (1, 2)
for x in t:
    print(x)
```

``` {.python results="output"}
with open("students.txt", "r") as f:
    for x in f:
        print(x.strip())
```

``` {.python results="output"}
from enum import Enum

class Directions(Enum):
    UP, RIGHT, DOWN, LEFT = range(4)

for x in Directions:
    print(x)

```

``` {.python results="output"}
d: dict = {'a': 1, 'b': 2, 'c': 3}
for x in d:
    print(x)

for x in d.keys():
    print(x)

for x in d.values():
    print(x)

for x in d.items():
    print(x)
```

The library `itertools` has many useful functions that create iterables.

``` {.python results="output"}
from itertools import count, repeat, cycle

for x in repeat("python"):
    print(x)

for x in count():
    print(x)

for x in cycle("abc"):
    print(x)
```

# Abstraction with iterable

Iterables are objects and can be assigned, passed to and returned from
functions.

## The printer to rule them all

``` {.python results="output"}
def print_all(xs: Iterable):
    for x in xs:
        print(x)
```

## Stringify

``` python
def stringify(xs: Iterator[Any]) -> Iterator[str]:
    return map(str, xs)
```

The function `map` will call the function provided as the first argument
on each value in the iterable of the second argument.

# Some important built-in functions that work with iterables

## `list()` creates a list from an iterable

``` {.python results="output"}
l = list(range(10))
print(l)
l = list("abc")
print(l)
```

## `sum()`, `min()`, `max()`, `any()`, `all()` and `sorted()`

``` {.python results="output"}
print(sum(range(10)))
print(max(["foobar", "quux", "garply"]))
print(sorted([(2, 1), (2, 2), (0, 3), (5, 6)]))
```

Note: `min` and `max` require that the values of the iterable are
comparable, that is have defined `<` and `==` operators.

# Combining tuples and iteration

Tuple *unpacking* and foreach loops combine with an elegant syntax.

## Tuple unpacking

A tuple of names/variables can appear on the left-hand side of an
assignment statement.

``` {.python results="output"}
t = (123, 456)
(x, y) = t
```

The parentheses are optional:

``` {.python results="output"}
x, y = 123, 456
```

What does this do?

``` {.python results="output"}
x, y = y, x
```

## Iterating over a stream of tuples

With tuple unpacking we can go from:

``` {.python results="output"}
d: dict = {'a': 1, 'b': 2, 'c': 3}
for kv in d.items():
    print(f"{kv[0]} has value {kv[1]}")
```

to:

``` {.python results="output"}
d: dict = {'a': 1, 'b': 2, 'c': 3})
for key, value in d.items():
    print(f"{key} has value {value}")
```

## (Aside) List unpacking

What\'s the output of this?

``` {.python results="output"}
l = list(range(3))
[a, b, c] = l
print(a)
print(b)
print(c)
```

and this?

``` {.python results="output"}
l = list(range(4))
[a, b, *c] = l
print(a)
print(b)
print(c)
```

# \"But wait, what if we want to...\"

## Use the position of the items in the list?

What if we need to know the indices?

``` {.python results="output"}
def eval_poly(x: int, coeffs: list[int]):
    total: int = 0
    for i in range(len(coeffs)):
        total += coeffs[i] * x**i
    return total
```

There is a handy function
`enumerate(Iterator[T]) -> Iterator[tuple[int, T]]` that will Use the
function

``` {.python results="output"}
def eval_poly(x: int, coeffs: iterable[int]):
    total: int = 0
    for i, c in enumerate(coeffs):
        total += c * x**i
    return total
```

Advantage of `enumerate` over the first version: lists are iterable and
indexable, but very few collections of data are, so the second version
is more robust. Notice the change in the signature.

## Convert two parallel arrays to a dictionary?

What if we want to construct a dictionary/map from two lists: keys and
values?

``` {.python results="output"}
def make_dict(keys: list, values: list) -> dict:
    result: dict = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result
```

There is a handy function
`zip(Iterator[T], Iterator[S]) -> Iterator[tuple[T, S]]` that pairs the
values returned by two iterators:

``` {.python results="output"}
def make_dict(keys: list, values: list) -> dict:
    result: dict = {}
    for k, v in zip(keys, values):
        result[k] = v
    return result
```

The function `dict()` takes an `Iterator[tuple]` as its argument so we
could even shorten this to:

``` {.python results="output"}
def make_dict(keys: list, values: list) -> dict:
    return dict(zip(keys, values))
```

# Abstraction and Iterator Composition

Consider this for loop:

``` {.python results="output"}
hot_days: int = 0
for temp in recorded_temperature:
    if temp >= 20:
        hot_days += 1
print(f"There were {hot_days} hot days")       
```

The `for-if` logic can be decomposed:

``` {.python results="output"}
def above(threshold: int, data: Iterable[int]) -> list[int]:
    results = []
    for x in data:
        if x >= threshold:
            results.append(x)
    return results
```

and now:

``` {.python results="output"}
hot_days: int = 0
for temp in above(20, recorded_temperature):
    hot_days += 1
print(f"There were {hot_days} hot days")       
```

or better:

``` {.python results="output"}
hot_days: int = len(above(20, recorded_temperature))
print(f"There were {hot_days} hot days")
```

A better `above()`

The function `above()` can me more succinctly written:

``` {.python results="output"}
def above(threshold: int, data: Iterator[int]) -> Iterator[int]:
    return filter(lambda x: x >= threshold, data)
```

Another option is an *generator* discussed below.

# List Comprehension

There is a syntactic shorthand for this:

``` python
result = []
for name in iterable:
    if condition:
        result.append(expression)
```

it\'s:

``` python
result = [expression for name in iterable if condition]
```

For example,

``` {.python results="output"}
def above(threshold: int, data: Iterator[int]) -> list[int]:
    results = []
    for x in data:
        if x >= threshold:
            results.append(x)
    return results
```

can be written as

``` python
def above(threshold: int, data: Iterator[int]) -> list[int]:
    return [x for x in data if x >= threshold]
```

# Iterator vs Iterable

You might have noticed the type `Iterator` in some of the sample code
above.

The simple story:

1.  An iterator is an object that will produce a stream of values. It\'s
    primary operation is called `next` (see below).
2.  An iterable is an object that is capable of producing an iterator.
    It\'s primary operation is called `iter` (see below). Iterables are
    usually collections like `list` or `dict`.

``` {.python results="output"}
l: list = [1, 2, 3]
it = iter(l)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
```

When you `for` loop over an iterable, the first thing that happens is
that an iterator is created to produce values.

Analogy: an book is iterable. Reading a book is an iteration. An
iterator is like a bookmark.

## (Aside) `__iter__()` and `__next__()`

The functions `iter(object)` and `next(object)` call that object\'s
`__iter__()` and `__next__()` methods respectively.

``` {.python results="output"}
from our_array import Array

class Stack:
    def __init__(self):
        self.elements: Array[int] = Array(10)

    def __iter__() -> Iterator[int]:
        return StackIter(self)

    # push, pop, etc...


class StackIter:
    def __init__(self, stack: Stack):
        self.stack: Stack = stack
        self.cursor: int = 0

    def __next__() -> int:
        if self.cursor >= len(self.stack.elements):
            raise StopIteration
        tmp = self.stack.elements[self.cursor]
        self.cursor += 1
        return tmp

    def __iter__() -> Iterator[int]:
        return self    # if the iterator is used as an iterable in a for loop
```

# Iterations are lazy

What if we wanted to \"tag\" recorded temperatures in a list with the
dates they were collected?

``` {.python results="output"}
from datetime import date, timedelta  # the first argument to timedelta is days

def tag_temps(start_iso: str, temps: list[float]) -> list[tuple[date, float]]:
    start: date = date.fromisoformat(start_iso)
    results = []
    for i in range(len(temps)):
        results.append((start + timedelta(i), temps[i]))
    return results
```

We can use `count` to enumerate the days!

``` {.python results="output"}
from datetime import date, timedelta
from itertools import count

def tag_temps(start_iso: str, temps: list[float]) -> list[tuple[date, float]]:
    start: date = date.fromisoformat(start_iso)
    deltas = map(timedelta, count())  # an infinite steam of date offsets
    results = []
    for d, temp in zip(deltas, temps):
        results.append((start + d, temp))
    return results
```

Note that since `count` produces an infinite sequence of numbers, the
iterable `deltas` is also infinite! Creating an infinite iterable does
not cause an infinite loop since there is no immediate evaluation of
this stream. This \"laziness\" is a useful feature of iterables: we can
carefully combine them with finite streams of values to ensure that our
program terminates. For example, `zip` will stop pairing values once one
of the iterables stops producing them.

Here\'s a simpler example in a python REPL:

``` {.python results="output"}
In [1]: c = count()

In [2]: type(c)
Out[2]: itertools.count
```

So our iterable is a `count` object. Calling `next` on an iterable will
get the next thing out of it:

``` {.python results="output"}
In [3]: next(c)
Out[3]: 0

In [4]: next(c)
Out[4]: 1

In [5]: next(c)
Out[5]: 2
```

Finally we can force it to make infinite values by asking for them, for
example in a `for` loop:

``` {.python results="output"}
In [6]: for i in c:
           print(i)

3
4
5
...
^C
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
Cell In[51], line 2
      1 for i in c:
----> 2     print(i)
```

# Generators

The date sequence above is a good example of how we can apply
abstraction in our programs. Here is a better way to make an infinite
date sequence:

``` {.python results="output"}
from datetime import date, timedelta

def days_from(start_iso: str) -> Iterator[date]:
    current: date = date.fromisoformat(start_iso)
    delta = timedelta(1)
    while True:
        yield current
        current = current + delta
```

It\'s called a generator. The `yield` statement produces a value and
then proceeds to the next statement, however it follows \"lazy\"
principle of iteration. It will not continue past the `yield` until the
yielded value is retrieved by the code that is using the generator.

Now we can write the `tag_temps` function in a very elengant way:

``` {.python results="output"}
from datetime import date, timedelta

def tag_temps(start_iso: str, temps: list[float]) -> list[tuple[date, float]]:
    results = []
    for date, temp in zip(days_from(start_iso), temps):
        results.append((date, temp))
    return results
```

or the more pythonic:

``` {.python results="output"}
from datetime import date, timedelta

def tag_temps(start_iso: str, temps: list[float]) -> list[tuple[date, float]]:
    return list(zip(days_from(start_iso), temps))
```

### Advanced example

``` python
def clockwise_directions_generator(start: Direction) -> Iterator[Direction]:
    """Just keep looping over directions, as needed"""
    forever_clockwise = cycle((Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT))
    for d in forever_clockwise:
        if d == start:
            yield d
            break
    yield from forever_clockwise
```

## Generators do not need to be infinite streams

``` {.python results="output"}
def circular_indices(start: int, size: int):
    for i in range(size):
        yield (start + i) % size
```

``` python
def clockwise_directions(start: Direction) -> Iterator[Direction]:
    forever_clockwise = cycle([Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT])
    for d in forever_clockwise:
        if d == start:
            break
    yield start
    for i in range(3):
        yield next(forever_clockwise)
```

# Generator expression

Using the same inline `for` statement as list comprehensions, but with
`()` instead of `[]`! So be careful!

``` python
def circular_indices(start: int, size: int):
    return ( (start + i) % size for i in range(size) )
```

# Generators are Iterators

A generator is an iterator. Once consumed it needs to be recreated to be
used again.

``` {.python results="output"}
indices = circular_indices(3, 7)
for i in indices:
    if i == 5:
        break
for i in indices:
    print(i)
```

# Python vs. \"Language XYZ\"

Yes, other imperative languages have iterators/streams/yields/itertools,
etc...

Some python advantages:

-   Relying on functions as opposed to methods reduce the learning
    overhead and also simplify the syntax
-   Duck typing can make this approachable for newer programmers
    (although the types can be helpful and are not too bad).

(Ian won\'t talk about how Haskell takes iterator/generator to a new
level...)

# Generator Pipelines

``` {.python results="output"}
def in_range(data: Iterator[int], r: range) -> Iterator[int]:
    return (x for x in data if x in r)

def project(f: Callable, data: Iterator) -> Iterator:
    return (f(x) for x in data)

def to_str_with_precision(data: Iterator[float]) -> Iterator[str]:
    return (f"{x:.3}" for x in data)

if __name__ == "__main__":
    def f(x):
        return float(x**2 + 2*x + 1)

    data: list[int] = [1, 35, 3,12, 432,34,22,213,123,123,4,433,5,435,6,7,66,3,5]
    data.sort()
    print(list(to_str_with_precision(project(f, in_range(data, range(100))))))
```
