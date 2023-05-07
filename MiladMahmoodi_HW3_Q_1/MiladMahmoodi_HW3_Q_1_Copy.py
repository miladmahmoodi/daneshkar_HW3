#! /usr/bin/python3
"""
This module get a file contain of 'The Zen of Python' and in start lines replace number with spelling number.
"""
import re

from os.path import isfile


def replacement(data) -> list[str]:
    """
    This function replaces the spelling number inside the text with its number.
    :param lines: List of string values.
    :return: List of string values.
    """

    # Numbers of used in file.
    TRANSLATE_DICT = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'ten': '10',
        'eleven': '11',
        'twelve': '12',
        'thirteen': '13',
        'fourteen': '14',
        'fifteen': '15',
        'sixteen': '16',
        'seventeen': '17',
        'eighteen': '18',
        'nineteen': '19',
        'twenty': '20',
    }

    for key, value in TRANSLATE_DICT.items():
        if key in data.split():
            print(key)
















def zen_of_python(file: str, new_file_name: str = 'zen.txt') -> str:
    """
    The Zen of Python, by Tim Peters

    :param file: txt file
    :param new_file_name: New txt file name to save changes.
    :return: Prompt
    """

    # Checking if the file is exists.
    if not isfile(file):
        raise FileNotFoundError(f"No such file: '{file}'")

    # Opening the file then reading all lines.
    with open(file, 'r', encoding='utf-8') as file:
        data = file.read()

    data = replacement(data)

    # Use the convertor function for replacing spelling number with it`s number.
    # lines = replacement(chars)

    # Opening the file then writing all lines on it.
    # with open(new_file_name, 'w') as new_file:
    #     new_file.write(data)
    #
    # return f"End process...\nFile '{new_file_name}' created successfully."


def main():
    """
    This function is written to execute and use this module`s functions in itself.
    """
    return zen_of_python(
        'Zen.txt',
        'zen.txt'
    )


if __name__ == '__main__':
    print(main())

