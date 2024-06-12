# CS Python Workshops

# Reminder

These are workshops for us as a department to develop a common understanding of the technology we will be teaching. Not everything in the workshops will be taught to science students.

# PyCharm


## PyCharm overview


- Get it from: <https://www.jetbrains.com/pycharm/>.
- Community edition is the free version.
- "Cousin" of IntelliJ IDEA (java), Android Studio and others.
- Platforms: Windows, macOS and Linux.
- Specific to python programming.


## Project structure overview:

- What is a PyCharm project?
- PyCharm has a flexible idea of a project.
- Opening a folder in pycharm automatically makes it a project.
- Hidden `.idea` folder indicates a project.
- Can't "double-click" it in file explorers


### Tip for console users

In bash/macOS: use an alias to open pycharm.

    > alias pycharm='open -a /Applications/PyCharm\ CE.app/'
    > pycharm path/to/project


## Python interpreter


- Setting the interpreter
- Switching interpreters
- Always check that an interpreter is set
  - Not indicated and can have some odd error messaging.

### System vs. local interpreter

-   **system:** installed on machine
-   **local:** installed as virtual environment


## Virtual Environment

-   Install python packages in the project folder instead of system folder.
-   Possibly the most relevant reason for us:
-   `venv` or `.venv` in project
-   Not considered movable. Not committed to repo. Recreated from scratch.


### References:

-   "Creation of virtual environments"  <https://docs.python.org/3/library/venv.html#venv-def>
-   "Python Virtual Environments: A Primer" <https://realpython.com/python-virtual-environments-a-primer/>


## Run configuration vs. Run current file


- Run [01<sub>hello</sub><sub>world.py</sub>](01_hello_world.py)
- "current file"
  - Just that: run current file.

### Run `▶`

-   In the left margin of the editor you will see a `▶`.
-   pycharm is detecting an execution point in the file.
-   Running this will add it to the drop-down at the top of the window. These are called "run configurations".
-   Run configurations configurable. Ex: you can pass arguments to your configurations.


### References

-<https://www.jetbrains.com/help/pycharm/run-debug-configuration.html>


### Dive deeper

-   Why `__name__ == "__main__"`? https://realpython.com/if-name-main-python/

-   Including run configurations in your repositories.
    -   By default configurations are not stored in version control.
    -   <https://www.jetbrains.com/help/pycharm/run-debug-configuration.html#share-configurations>

## REPL

- Read-Execute-Print-Loop
- Install `ipython` in terminal.
  1.  In pycharm, open "Terminal". Notice the `(venv)` if you are working in a virtual environment.
  2.  Use pip to install:  `> pip install ipython`
  3.  `> ipython`

- Why REPL?
  - Test units of code: expressions, functions, etc...
  - Discover what operations are available for an object: `dir(x)`.
  - Check the documentation of an operation: `? foo`

### Dive Deeper

-   Inspect objects using `
-   Code disassembly using the `dis` library. 


## Inspections

### Linting

-   Both compilers and linters: check syntax, type check
-   Compilers generate code.
-   Linters also check style errors, code smell / bad code.

### Inspection Severity

-   **Errors:** Syntax errors: showstoppers that will be runtime errors if executed.
-   **Warnings:** Might be an error. To fix!
-   **Weak Warnings:** Not an error, but code that could be improved.


### Errors don't prevent the running of code.

-   There are errors [03<sub>inspections.py</sub>](03_inspections.py)
-   We can still run the other code examples.
-   We can still run main in 03<sub>inspections.py</sub>!

### References

-   <https://www.jetbrains.com/help/pycharm/configuring-inspection-severities.html>

### Dive Deeper

-   Configuring inspections <https://www.jetbrains.com/help/pycharm/inspections-settings.html>

# Types

## Dynamic typing

This is allowed in python:

    x = 123
    x = "abc"
    x = [1, 2, 3]

But:

-   Just cause we can doesn't mean we should.
-   This does not mean python has no types.


## Python has types

Try this in the REPL

    >>> x = 123
    >>> type(x)
    >>> x = "abc"
    >>> type(x)
    >>> x = [1, 2, 3]
    >>> type(x)

The values have types, the variable (name) `x` does not.

            +-----------------------+
            | type: str             |
    [x] --> | value: "abc"          |
            | refcount: 1           |
            +-----------------------+

The function `isinstance` can check a type at runtime.

    def test_return_type_correct():
        assert isinstance(asg1_solution(), float)


### References:

-   <https://www.youtube.com/watch?v=_AEJHKGk9ns>


## Built-in types


### There are:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Type</th>
<th scope="col" class="org-left">What we might find different</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left"><code>int</code></td>
<td class="org-left">No overflow: like a big-int</td>
</tr>


<tr>
<td class="org-left"><code>float</code></td>
<td class="org-left">64-bit. There is no <code>double</code> type</td>
</tr>


<tr>
<td class="org-left"><code>str</code></td>
<td class="org-left">String data type</td>
</tr>


<tr>
<td class="org-left"><code>bool</code></td>
<td class="org-left">Values <code>True</code> and <code>False</code></td>
</tr>
</tbody>
</table>

Some other important types:

-   Collections: `range`, `list`, `set`, `tuple`, `dict`
-   Misc: `complex` for complex numbers, binary types, `None` (like `null`).
-   Callables: functions and methods


### Dive Deeper

-   Types, Modules and Code itself are objects in python. <https://docs.python.org/3/library/stdtypes.html#other-built-in-types>


## Duck typing

"If it looks like a duck, quacks like a duck, it's a duck"

    def many_pop(collection, amount):
        for i in range(amount):
            if len(collection) == 0:
                return
            collection.pop()

What kinds of collections can we `many_pop`? Those with operations `pop` and `len` (technically `__len__`).

A stack class would support these, but turns out built-in's `list`,  `set` and `dict` do too!

See <04_types.py> for full example.

## Type Hints

-   For variables:
    
        x: int = 123
        y: float = 3.14
        n: str = "ian"

-   For functions:
    
        def add(x: int, y: int) -> int:
            return x + y
        
        def debug(message: str) -> None:
            print(message, file=error_log)

-   Maybe we should drop `-> None`?


## Types and OOP

Classes, protocols (interfaces), enums are all types:

    class Stack:
        ...
    
    
    def combine(s1: Stack, s2: Stack) -> Stack:
        ...

More on objects in later workshops.


## Optionals

Optional types allow for `None` values.

    def index_of(data: list[str], value: str) -> Optional[int]:
        pass


## Why bother with types?

1.  Detecting errors when the linting.
2.  Additional information about our code.
3.  Reasoning about code.
4.  IDE drop-down lists for available operations.


## Dive Deeper:

-   Generics and type arguments, ex: `list[str]` or "list of strings": 
-   Protocols (interfaces).
-   Union types.

