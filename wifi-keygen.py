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
import random

while 1:
    try:
        length = int(av.gets("Desired PSK Length: "))
        if length < 8 or length > 63:
            av.error("PSK length should be between 8 and 63")
            continue
        break
    except ValueError:
        av.error("Invalid Input")

symbols = ''.join([chr(i) for i in range(33, 48)])
char_pool = ascii_letters + digits + symbols
password = (''.join(random.SystemRandom().choice(char_pool) for _ in range(length)))
print(password)
