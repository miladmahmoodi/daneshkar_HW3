#! /usr/bin/python3
"""
This is
"""

import datetime
import jdatetime


def happy_birthday(
        year: int,
        month: int,
        day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
):
    datetime_now = datetime.datetime.today()

    birth_date = datetime.datetime(
        year,
        month,
        day,
        hour,
        minute,
        second,
    )

    total_second = (
            datetime_now
            - birth_date
    ).total_seconds()

    this_year_bd = datetime.datetime(
        datetime_now.year,
        month,
        day,
    )
    next_year_bd = datetime.datetime(
        datetime_now.year + 1,
        month,
        day,
    )

    next_birthday = (this_year_bd if this_year_bd > datetime_now else next_year_bd) - datetime_now

    jalali_birth_day = jdatetime.GregorianToJalali(
        gyear=year,
        gmonth=month,
        gday=day,
    ).getJalaliList()

    return total_second, next_birthday, jalali_birth_day


def main():
    """
    This function is written to execute and use this module`s functions in itself.
    """
    result = happy_birthday(
        1997,
        5,
        12,
        10,
        0,
        0,
    )
    # return result
    print(
        f'Total elapsed seconds: {result[0]}',
        f'Happy birthday in advance... {result[1]}',
        f'Hijri: {result[2]}',
        sep='\n',
    )
# Happy birthday in advance


if __name__ == '__main__':
    main()

