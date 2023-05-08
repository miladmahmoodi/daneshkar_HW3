#! /usr/bin/python3
"""
This is simple module to applies the discount code to the price.
"""


def apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price.
    :param price: Price.
    :param discount: Discount.
    :return: Final price.
    """

    final_price = int(price * (1 - discount))

    # Syntax error
    assert (
        0 < final_price <= price, "Why this AssertionError never Raised!"
        )

    """
    assert doesn't work because it has a syntax error.
    The code is modified by removing the desired text from inside the parenthesis.
    assert are not a good way to validate data and are only used to debug and monitor possible errors, because by
    running this file with the command '-O' in terminal, all assert are ignored and we have no ability to validate data.
    As a result, assert is not suitable for data validation.
    To avoid this problem and to validate the data, we can use conditional commands.
    Pay attention to the following code:
    """

    # Valid syntax
    assert (
        0 < final_price <= price
        ), "Why this AssertionError never Raised!"

    # Data validation
    if not 0 < final_price <= price:
        raise ValueError('some error.')

    return final_price


def main():
    """
    This function is written to execute and use this module`s functions in itself.
    """
    return apply_discount(
        1000,
        .9,
    )


if __name__ == '__main__':
    print(main())
