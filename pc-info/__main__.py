from .main import stdout_main_data, get_internet_speed
from sys import argv, exit

try:

    if len(argv) == 1:
        stdout_main_data()

    elif argv[1] == '--speedtest':
        get_internet_speed()

    elif argv[1] == '--help':
        print(f'| --speedtest ... get the current internet speed.')

except KeyboardInterrupt:
    exit()