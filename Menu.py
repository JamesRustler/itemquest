#!/usr/bin/env python3
"""
General Menu System
"""


def menu(options):
    """
    General text menu - returns number of option chosen.

    options is an array of strings for the menu options.

    Usage:
    >>> fight_menu = ("attack","magic","item","run")
    >>> selection = menu(fight_menu)
    >>> print(selection)
    1
    """

    error_invalid_option = 'Enter a value between 1 - '
    error_invalid_option += str(len(options))
    error_invalid_option += '.'
    acceptable_answer_range = range(1, (len(options) + 1))
    selection_chosen = False

    while not selection_chosen:
        option_number = 1
        for option in options:
            print(str(option_number) + ') ' + option)
            option_number += 1
        try:
            answer = int(input('> '))
        except ValueError:
            print(error_invalid_option)
            continue
        if answer not in acceptable_answer_range:
            print(error_invalid_option)
            continue
        if answer in acceptable_answer_range:
            selection_chosen = True
    return answer
