# Поиск сборок и обновление файлов АС ДКО

import pathlib
import os

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
REVISION_DIR = r"\\10.1.18.19\asdko\RELEASE\ASDCO_release_next\release_60"


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
        elif i.is_file():
            pass
    return max(list_dir), pathlib.Path(path).joinpath(max(list_dir))


def get_file_create_time(path):  # получение времени создания файлов в каталоге сборки
    dict_of_file = {'accord.jar': 0,
                    'client.jar.pack.gz': 0,
                    'patchC.jar': 0, 'patchS.jar': 0, 'server-accounts-service.jar': 0, 'server.jar.pack.gz': 0, 'serverM.jar.pack.gz': 0, 'signar.jar': 0, 'support.jar': 0, }
    for i in pathlib.Path(path).iterdir():
        if i.name in dict_of_file.keys():
            creating_time = i.stat().st_ctime
            dict_of_file[i.name] = creating_time
    print(dict_of_file)


def get_size(path, dict_name):
    dict_name = {}
    # for i in pathlib.Path(path).iterdir():
    #     dict_name[i.name] = i.stat().st_size
    # print(sum(file.stat().st_size for file in path.glob('**\*')))
    print('\n')
    for i in path.rglob('*'):  # get all files and directories from the path
        if i.is_file():
            if '001' in i.parts:
                path_to_schemas = pathlib.Path.cwd()
                for j in i.parts[i.parts.index('001')-1::]:  # поиск элемента 001 (заменить на XMLSchemas) и добавление к пути
                    path_to_schemas = path_to_schemas.joinpath(j)
                print('path to schemas:', path_to_schemas)
                print(path_to_schemas.exists())
            elif '001' not in i.parts:
                pass
                # print(i.parts[len_parts-2::])
            dict_name[i.name] = i.stat().st_size
        elif not i.is_file():
            pass
        # print(i, i.stat().st_size)
        # dict_name[f'{i.parent}\{i.parent.name}'] = i.stat().st_size
        # dict_name[i.name] = i.stat().st_size
        # print(i.name, i.stat().st_size)
        # print(dict_name)
    return dict_name


def dict_compare(*dicts):
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
    dict_compare(get_size(pathlib.Path.cwd().joinpath('test'), 'original_dict'), get_size(pathlib.Path.cwd().joinpath('test2'), 'asdco_dict'))
    # get_size(pathlib.Path.cwd().joinpath('test'), 'original_dict')
    # get_size(pathlib.Path.cwd().joinpath(r'C:\ASDCO\asdco_test_002\run\AppContext\XMLSchemas'), 'original_dict')

    
# TODO сравнивать размер каталога с каждым альбомом XML в сборке и каталоге АС ДКО


    
# TODO сравнивать размер каталога с каждым альбомом XML в сборке и каталоге АС ДКО
