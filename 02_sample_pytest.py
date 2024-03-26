# The next line is flagged as an error until you install the dependency
# Follow the "fix" suggested by the red lightbulb
import pytest

# Alternate way: use terminal to install
import numpy


def test_math_is_math():
    assert 4 == 2 + 2
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0


def test_numpy_math():
    assert 4 == numpy.add(2, 2)
