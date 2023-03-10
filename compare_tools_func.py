# Поиск сборок и обновление файлов АС ДКО

import pathlib
import os

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
            if birth_dir_time > max_birth_dir_time:  # сравниваем дату создания каталога с максимальной датой создания
                max_birth_dir_time = birth_dir_time
                print(f'Birth: {i} {birth_dir_time}')
                print(max_birth_dir_time)
                print(type(i))
    return i

def get_size(path, dict_name):
    dict_name = {}
    for i in pathlib.Path(path).iterdir():
        dict_name[i.name] = i.stat().st_size
    return dict_name


def dict_compare(*dicts):
    for i in dicts[0]:
        # print(dicts[0].get(i))
        # print(dicts[1].get(i))
        if dicts[0].get(i) != dicts[1].get(i):
            print(f'{i} key is not equal. {dicts[0].get(i)}. {dicts[1].get(i)}. ')
        elif dicts[0].get(i) == dicts[1].get(i):
            print(f'{i} key is equal')
        elif dicts[0].get(i) not in dicts[1]:
            print(f'{i} key is not find')
        else:
            print('Something wrong!')




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(get_latest_revision(pathlib.Path().cwd()))
    # print(get_latest_revision(pathlib.Path('/Users/steelhawk/Documents/Godot_projects')))
    # get_size(pathlib.Path.cwd().joinpath('test'), 'original_dict')
    dict_compare(get_size(pathlib.Path.cwd().joinpath('test'), 'original_dict'), get_size(pathlib.Path.cwd().joinpath('test2'), 'asdco_dict'))
