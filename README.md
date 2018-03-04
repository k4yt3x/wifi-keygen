# WiFi-Keygen

A utility that generates a long, complex and secure wifi password.


## Usages

First get WiFi-Keygen from github
~~~~
$ git clone https://github.com/K4YT3X/wifi-keygen.git
$ cd wifi-keygen/
~~~~

Then run it with python3
~~~~
$ python3 wifi-keygen.py
~~~~
OR
~~~~
$ ./wifi-keygen.py
~~~~

## Arguments
~~~~
usage: wifi-keygen.py [-h] [--uppercase] [--lowercase] [--digits] [--symbols]
                      [-a] [-q] [--version]

optional arguments:
  -h, --help   show this help message and exit

Character Selection:
  --uppercase  Include uppercase ASCII characters
  --lowercase  Include lowercase ASCII characters
  --digits     Include digits
  --symbols    Include symbols
  -a, --all    Include all possible characters (Default)

Extra:
  -q, --quiet  Quiet Mode
  --version    Show WiFi-Keygen version and exit
~~~~