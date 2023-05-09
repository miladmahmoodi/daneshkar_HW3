#! /usr/bin/python3
"""
This module get a file contain of 'The Zen of Python' and in start lines replace number with spelling number.
"""
import typing
from os.path import isfile


def line_generator(file: str) -> typing.Generator:
    """
    This generator yield the input file line by line.
    :param file: txt file.
    :return: Generator.
    """

    with open(file, 'r') as f:
        for line in f:
            yield line


def line_replacement_generator(file: str) -> typing.Generator:
    """
    This generator replaces the spelling of the number at the beginning of the line with its number.
    :param file: txt file.
    :return: Generator.
    """

    # Numbers of used in file.
    REPLACE_DICT = {
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

    line_gen = line_generator(file)

    for line in line_gen:
        for key, value in REPLACE_DICT.items():
            # Finding spelling number.
            if key + ' )' in line or ' ' + key + ' ' in line:
                # Replacing spelling number with it`s number.
                line = line.replace(
                    key,
                    value
                )
        yield line


def zen_of_python(file: str, new_file_name: str = 'zen.txt') -> str:
    """
    The Zen of Python, by Tim Peters
    :param file: txt file
    :param new_file_name: New txt file name to save changes.
    :return: Prompt.
    """

    # Checking if the file is exists.
    if not isfile(file):
        raise FileNotFoundError(f"No such file: '{file}'")

    # Use the replacement generator for replacing spelling number with it`s number.
    replacement_lines = line_replacement_generator(file)

    # Opening the file then writing all lines on it.
    with open(new_file_name, 'w') as new_file:
        for line in replacement_lines:
            new_file.write(line)

    return f"End process...\nFile '{new_file_name}' created successfully."


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
