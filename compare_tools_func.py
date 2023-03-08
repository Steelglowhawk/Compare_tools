# Поиск сборок и обновление файлов АС ДКО

import pathlib

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_latest_revision(path):
    """
    Определение каталога с последней сборкой
    :param path: путь к каталогу со сборками
    :return:
    """
    max_birth_dir_time = 0

    for i in pathlib.Path(path).iterdir():

        if i.is_dir():
            birth_dir_time = i.stat().st_ctime
            if birth_dir_time > max_birth_dir_time:
                max_birth_dir_time = birth_dir_time
                print(f'Birth: {i} {birth_dir_time}')
                print(max_birth_dir_time)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_latest_revision(pathlib.Path().cwd())
