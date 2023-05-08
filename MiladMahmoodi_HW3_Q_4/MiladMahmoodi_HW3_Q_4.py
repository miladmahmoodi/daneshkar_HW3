#! /usr/bin/python3
"""
This module takes the date and time of birth in Gregorian language and calculates the total number of seconds that have
passed since the date of birth in terms of minutes and seconds, and finally calculates the number of days and minutes
remaining until the next birthday celebration.
with a clap sound.
"""

import datetime
import jdatetime

from playsound import playsound


def happy_birthday(
        year: int,
        month: int,
        day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
):
    datetime_now = datetime.datetime.now()

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
        hour,
        minute,
        second,
    )
    next_year_bd = datetime.datetime(
        datetime_now.year + 1,
        month,
        day,
        hour,
        minute,
        second,
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
        10,
        0,
    )

    print(
        f'Total elapsed seconds: {result[0]}',
        f'Happy birthday in advance... {result[1]}',
        f'Hijri: {result[2][0]}/{result[2][1]}/{result[2][2]}',
        sep='\n',
    )
    playsound('clap.mp3')


if __name__ == '__main__':
    main()

