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


def total_life_second(birth_date: datetime.datetime) -> float:
    """
    This function returns the total seconds of life.
    :param birth_date: Date and time.
    :return: Seconds of life.
    """

    datetime_now = datetime.datetime.now()

    total_second = (
            datetime_now
            - birth_date
    ).total_seconds()

    return total_second


def next_birthday(birth_date: datetime.datetime) -> datetime.timedelta:
    """
    This function returns the number of days until the next birthday.
    :param birth_date: Date and time.
    :return: Days until the next birthday.
    """

    datetime_now = datetime.datetime.now()

    this_year_bd = datetime.datetime(
        datetime_now.year,
        birth_date.month,
        birth_date.day,
        birth_date.hour,
        birth_date.minute,
        birth_date.second,
    )
    next_year_bd = datetime.datetime(
        datetime_now.year + 1,
        birth_date.month,
        birth_date.day,
        birth_date.hour,
        birth_date.minute,
        birth_date.second,
    )

    to_next_birthday = (this_year_bd if this_year_bd > datetime_now else next_year_bd) - datetime_now

    return to_next_birthday


def jalali_birth_date(birth_date: datetime.datetime) -> jdatetime.GregorianToJalali:
    """
    This function converts the Gregorian date to Jalali.
    :param birth_date: Date and time.
    :return: Jalali datetime.
    """

    jalali_birth_day = jdatetime.GregorianToJalali(
        gyear=birth_date.year,
        gmonth=birth_date.month,
        gday=birth_date.day,
    ).getJalaliList()

    return jalali_birth_day


def happy_birthday(
        year: int,
        month: int,
        day: int,
        hour: int = 0,
        minute: int = 0,
        second: int = 0,
):
    """
    This function takes the date of birth into Gregorian and then the number of seconds that have passed since the date
    of birth and the number of days remaining until the next birthday and the date of birth into Jalali.
    :param year: Year of birthday.
    :param month: Month of birthday.
    :param day: Day of birthday.
    :param hour: Hour of birthday.
    :param minute: Minute of birthday.
    :param second: Second of birthday.
    :return: Tuple of total life second, next birthday and jalali birth date.
    """

    birth_date = datetime.datetime(
        year,
        month,
        day,
        hour,
        minute,
        second,
    )

    total_second = total_life_second(birth_date)

    to_next_birthday = next_birthday(birth_date)

    jalali_birth_day = jalali_birth_date(birth_date)

    return total_second, to_next_birthday, jalali_birth_day


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

