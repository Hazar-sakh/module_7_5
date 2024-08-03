import os
import time


_directory = '.'
_path = os.path.join(_directory)
_time = os.path.getmtime(_directory)
_size = os.path.getsize(_directory)
_dirname = os.path.dirname(_directory)

for root, dirs, files in os.walk(_directory):
    for file in files:
        filepath = _path
        filetime = _time
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = _size
        parent_dir = _dirname
        print(f'Обнаружен файл: {file}, Путь: {_path}, Размер: {filesize} байт,\n'
              f'Время изменения: {formatted_time}, Родительская директория: {_dirname}')
