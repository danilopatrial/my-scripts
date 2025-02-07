from .main import main
from sys import argv
from os import system, path
from json import load, dump

def argv_parser(argv: list) -> None:

    keyNotFoundMessage: function = lambda key:\
        print(f"\033[1;31mKeyNotFoundError: Ignoring '{key}'\n'--help' for more info.\033[0m")
    fileNotFoundMessage: function = lambda file:\
        print(f'\033[1;31mFileNotFoundError: {file} does NOT exist.\033[0m')

    def print_json_config() -> None:
        system('type "C:\\Users\\Danilo Patrial\\Python\\Scripts\\downloads_cleaner\\folders_paths.json"')

    def print_stdout_commands() -> None:
        for key, value in stdout_commands.items():
            key += ' '
            print(f"| {key.ljust(15, '.')} {value.__name__.replace('_', ' ')}", end=' ')
            print(f"{value.__annotations__["return"] if value.__annotations__["return"] != None else ''}")

    def change_file_path() -> None:

        if len(argv) != 4:
            return keyNotFoundMessage(argv[1])

        if not path.exists(argv[3]):
            return fileNotFoundMessage(argv[3])

        with open('downloads_cleaner/folders_paths.json', 'r') as json_file:
            data: dict = load(json_file)

        if argv[2] not in data.keys():
            return keyNotFoundMessage(argv[2])

        data[argv[2]] = argv[3]

        with open('downloads_cleaner/folders_paths.json', 'w') as json_file:
            dump(data, json_file, indent=4)

        print(f'\033[1;33mJSON file successfully updated!\033[0m')

    stdout_commands: dict = {
        '--filepaths': print_json_config,
        '--help': print_stdout_commands,
        '--setpath': change_file_path,
    }

    change_file_path.__annotations__ = {"return": ".i.e '--setpaht images my/images/folder/path'"}

    try:
        stdout_commands[argv[1]]()
    except:
        return keyNotFoundMessage(argv[1])

if len(argv) != 1:
    argv_parser(argv)

elif __name__ == '__main__':
    main()