# compare_tools_func_py
# Поиск сборок и обновление файлов АС ДКО

import pathlib
import os

REVISION_DIR = r"\\10.1.18.19\asdko\RELEASE\ASDCO_release_next\release_60"


def create_release_list_for_gui_drop_down_menu(path):  # создание списка релизов из release_next
    # для использования в интерфейсе
    list_dir = []
    for i in pathlib.Path(path).iterdir():
        if i.is_dir():
            list_dir.append(i.name)
    return list_dir


def get_latest_revision(path):
    """
    Определение каталога с последней сборкой
    :param path: путь (str) к каталогу со сборками
    :return:
    """
    list_dir = []
    for i in pathlib.Path(path).iterdir():
        if i.is_dir() and i.name.startswith('88'):
            list_dir.append(i.name)
            print(list_dir)
        elif i.is_file():
            print('is file')
            pass
    return max(list_dir), pathlib.Path(path).joinpath(max(list_dir))


def get_file_create_time(path):  # получение времени создания файлов в каталоге сборки
    dict_of_file = {'accord.jar': 0,
                    'client.jar.pack.gz': 0,
                    'patchC.jar': 0, 'patchS.jar': 0, 'server-accounts-service.jar': 0, 'server.jar.pack.gz': 0,
                    'serverM.jar.pack.gz': 0, 'signar.jar': 0, 'support.jar': 0, }
    for i in pathlib.Path(path).iterdir():
        if i.name in dict_of_file.keys():
            creating_time = i.stat().st_ctime
            dict_of_file[i.name] = creating_time
    print(dict_of_file)


def search_for_schemas(path):
    '''
    Проверка каталога на существование XMLSchemas
    :param path: имя каталога для поиска
    :return: True or False
    '''
    for i in path.glob('**'):
        if i.name == 'XMLSchemas':
            print(i.parts)
            return True
    return False


def get_size(path, dict_name):
    '''
    Создание словаря со списком файлов и размером файлов для последующего сравнения в каталоге сборки и каталоге АС ДКО
    :param path: путь к каталогу для анализа
    :param dict_name: имя создаваемого словаря
    :return: возвращает словарь
    '''
    dict_name = {}
    print('\n')
    for i in path.rglob('*'):  # get all files and directories from the path
        if i.is_file():
            if '001' in i.parts:  # поиск 001 в имени компонентов пути
                path_to_schemas = pathlib.Path.cwd()
                for j in i.parts[
                         i.parts.index(
                             '001') - 1::]:  # получение индекса элемента 001 (заменить на XMLSchemas) и добавление к пути
                    path_to_schemas = path_to_schemas.joinpath(j)
                print('path to schemas:', path_to_schemas)
                print(path_to_schemas.exists())
            elif '001' not in i.parts:
                pass
            dict_name[i.name] = i.stat().st_size
        elif not i.is_file():
            pass
    return dict_name


def dict_compare(*dicts):  # сравнение словарей со списками файлов в каталоге сборки и каталоге АС ДКО
    list_of_diff = []
    for i in dicts[0]:
        # print(dicts[0].get(i))
        # print(dicts[1].get(i))
        if dicts[0].get(i) != dicts[1].get(i):
            print(f'{i} key is not equal. {dicts[0].get(i)}. {dicts[1].get(i)}. ')
            list_of_diff.append(i)
        elif dicts[0].get(i) == dicts[1].get(i):
            print(f'{i} key is equal')
        elif dicts[0].get(i) not in dicts[1]:
            print(f'{i} key is not find')
        else:
            print('Something wrong!')
    print(list_of_diff)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # path_to_latest_revision = get_latest_revision(REVISION_DIR)[1]
    # get_file_create_time(path_to_latest_revision)
    # dict_compare(get_size(pathlib.Path.cwd().joinpath('test'), 'original_dict'),
    #              get_size(pathlib.Path.cwd().joinpath('test2'), 'asdco_dict'))
    # get_size(pathlib.Path.cwd().joinpath('test'), 'original_dict')
    # get_size(pathlib.Path.cwd().joinpath(r'C:\ASDCO\asdco_test_002\run\AppContext\XMLSchemas'), 'original_dict')
    # print(search_for_schemas(pathlib.Path.cwd().joinpath('test/003')))
    path = pathlib.Path.cwd().joinpath('releases')
    print(create_release_list_for_gui_drop_down_menu(path))

# TODO сравнивать размер каталога с каждым альбомом XML в сборке и каталоге АС ДКО
# TODO отсортироать список от create_release_list_for_gui
