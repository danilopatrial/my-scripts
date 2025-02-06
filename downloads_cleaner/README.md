# Downloads Cleaner

## Description
Downloads Cleaner is a Python script that automatically organizes and cleans files in your downloads folder based on predefined categories. It moves files to their respective folders or permanently deletes unrecognized files.

## Features
- Parses and lists all files in the downloads folder with details (name, type, size).
- Moves files to predefined folders based on their extensions.
- Deletes unrecognized files permanently.
- Allows updating file paths through command-line arguments.
- Provides a help command to display available options.

## Installation
1. Clone this repository or download the script.
2. Ensure you have Python installed on your system.

## Usage
Run the script using Python:
```bash
python -m downloads_cleaner
```

### Command-line Options
- `--filepaths` : Prints the current folder paths stored in `folders_paths.json`.
- `--help` : Displays available commands and their descriptions.
- `--setpath <category> <new_path>` : Updates the path for a specific file category.

Example:
```bash
python downloads_cleaner --setpath images "C:\Users\User\Pictures"
```

## Supported File Types
| Extension | Folder |
|-----------|--------|
| pdf       | Documents |
| mp4       | Videos |
| iso       | ISOs |
| png, jpg, jpeg, gif | Images |
| mp3       | Audio |

## Deleting Files
The script permanently deletes any files that do not belong to the predefined categories. Before proceeding, it asks for confirmation.

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

## Autor
Danilo Patrial

