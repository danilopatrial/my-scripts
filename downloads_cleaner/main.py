from json import load
from shutil import move, rmtree
import stat, os

with open('downloads_cleaner/folders_paths.json', 'r') as json_file:
    data: dict = load(json_file)

DOWNLOADS: str = data.get('downloads', None)

def organize_files() -> None:
    file_map: dict = {
        'pdf': data['pdf'],
        'mp4': data['videos'],
        'iso': data['isos'],
        'png': data['images'],
        'jpg': data['images'],
        'mp3': data['audios'],
        'gif': data['gifs'],
        'jpeg': data['images']
    }
    print()
    for file in os.listdir(DOWNLOADS):
        try:
            file_type: str = file.split('.')[-1]
            destination_folder: str = file_map[file_type]
            move(os.path.join(DOWNLOADS, file), os.path.join(destination_folder, file))
            print(f'\033[1;33m{file} moved to {destination_folder}\033[0m')
        except:
            force_delete(os.path.join(DOWNLOADS, file))
            print(f'\033[1;31m{file} deleted.\033[0m')

def force_delete(file_path: str) -> None:
    if os.path.isfile(file_path):
        os.chmod(file_path, stat.S_IWRITE)
        os.remove(file_path)
        return
    for root, dirs, files in os.walk(file_path, topdown=False):
        for file in files:
            path = os.path.join(root, file)
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))

def downloads_parsing() -> None:
    os.system('cls')
    files: list = os.listdir(DOWNLOADS)
    number_files: int = len(files)
    total_size: float = 0.0

    print(f'\033[1;37m{number_files} files found at {DOWNLOADS}:\033[0m\n')
    for i, file in enumerate(files):
        file_path: str = os.path.join(DOWNLOADS, file)

        file_type = file.split('.')[-1] if '.' in file else ''

        file = file.removesuffix('.' + file_type)
        file_name = file if len(file) < 20 else file[:20] + '...'

        file_size = os.path.getsize(file_path) if file_type else ''
        total_size += file_size if file_size else 0
        print(f'{str(i + 1).zfill(3)}| {file_name:<33} {file_type:<15} {(file_size/1024 if file_size else 0).__round__(2)} KB')
    print(f'\nTotal size {''.ljust(43, '.')} {(total_size/1024).__round__(2)} KB')

    message: str = f"\nAre you sure you want to proceed? This action will \033[1;31mPERMANENTLY DELETE\033[0m all files except those with the following extensions: .pdf, .mp4, .mp3, .iso, .png, .jpg, .gif.\nY/N: "
    want_to_proced: bool = input(message).lower() in ('y', 'yes')
    if want_to_proced:
        organize_files()
    else:
        os.system('cls'), print('Application closed.')


def main():
    downloads_parsing()