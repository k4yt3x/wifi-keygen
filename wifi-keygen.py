#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WiFi Secure Password Generator

Dev: K4YT3X
Date Created: Mar 2, 2018
Last Modified: Mar 3, 2018

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2016 - 2017 K4YT3X
"""
from string import *
import avalon_framework as av
import argparse
import random

VERSION = "0.1 alpha"


def proces_arguments():
    """Parses arguments from the command line

    Character Selection: Options relevant to characters
    that shall be included for generating the password

    Extra: Other options

    Returns:
        argparse.Namespace -- parsed arguments
    """
    parser = argparse.ArgumentParser()
    char = parser.add_argument_group('Character Selection')
    char.add_argument("--uppercase", help="Include uppercase ASCII characters", action="store_true", default=False)
    char.add_argument("--lowercase", help="Include lowercase ASCII characters", action="store_true", default=False)
    char.add_argument("--digits", help="Include digits", action="store_true", default=False)
    char.add_argument("--symbols", help="Include symbols", action="store_true", default=False)
    char.add_argument("-a", "--all", help="Include all possible characters (Default)", action="store_true", default=False)
    etc = parser.add_argument_group('Extra')
    etc.add_argument("-q", "--quiet", help="Quiet Mode", action="store_true", default=False)
    etc.add_argument("--version", help="Show WiFi-Keygen version and exit", action="store_true", default=False)
    return parser.parse_args()


def create_char_pool(args):
    """Create a pool of characters

    This function creates a pool of characters which the
    random password generator will choose characters from.

    Arguments:
        args {argparse.Namespace} -- parsed arguments

    Returns:
        string -- string of characters
    """
    symbols = ''.join([chr(i) for i in range(33, 48)])
    char_pool = ""

    if args.uppercase:
        if not args.quiet:
            av.subLevelTimeInfo("Including Uppercase characters")
        char_pool += ascii_uppercase
    if args.lowercase:
        if not args.quiet:
            av.subLevelTimeInfo("Including lowercase characters")
        char_pool += ascii_lowercase
    if args.digits:
        if not args.quiet:
            av.subLevelTimeInfo("Including digits")
        char_pool += digits
    if args.symbols:
        if not args.quiet:
            av.subLevelTimeInfo("Including symbols")
        char_pool += symbols
    if args.all or not (args.uppercase or args.lowercase or args.digits or args.symbols):
        if not args.quiet:
            av.subLevelTimeInfo("Including all characters")
        if args.uppercase or args.lowercase or args.digits or args.symbols:
            if not args.quiet:
                av.warning("Ignoring other switches since including all characters")
        char_pool = ascii_letters + digits + symbols
    return char_pool


def get_psk_length():
    """Asks the user for desired password length

    Returns:
        int -- length of PSK
    """
    while 1:
        try:
            psk_length = int(av.gets("Desired PSK Length: "))
            if psk_length < 8 or psk_length > 63:
                av.error("PSK length should be between 8 and 63")
                continue
            break
        except ValueError:
            av.error("Invalid Input")
    return psk_length


args = proces_arguments()
char_pool = create_char_pool(args)
psk_length = get_psk_length()

password = (''.join(random.SystemRandom().choice(char_pool) for _ in range(psk_length)))
print(password)
