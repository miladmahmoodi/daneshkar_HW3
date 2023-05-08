#! /usr/bin/python3
"""
This module is about LBYL and EAFP styles and then handles them according to the errors in the problem.
LBYL: Look Before You Leap.
EAFP: Easier to Ask for Forgiveness than Permission.

As a rule of thumb, EAFP is considered more Pythonic and should be preferred in most scenarios.
Some reasons why EAFP is preferred over LBYL:
    1. Better performance
    2. Explicit and more readable
    3. Prevents race conditions

But there are some scenarios where using LBYL does make more sense:
    1. Too many exceptions
    2. Complex side effects

However, we use the EAFP scenario in this module.

"""

from math import inf


def eafp(number_1: int | float, number_2: int | float) -> float:
    """
    Divides two numbers according to the EAFP style.
    :param number_1: Integer or float number.
    :param number_2: Integer or float number.
    :return: float number.
    """
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return inf
    except TypeError as err:
        raise err
    except MemoryError as err:
        raise err
    except OverflowError as err:
        raise err
    except Exception as err:
        raise err


def main():
    """
    This function is written to execute and use this module`s functions in itself.
    """
    return eafp(
        10,
        0.0
    )


if __name__ == '__main__':
    print(main())
