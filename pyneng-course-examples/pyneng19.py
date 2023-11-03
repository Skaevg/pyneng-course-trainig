import os

[file for file in os.listdir(".") if os.path.isfile(file)] # вывод всего ls и проверка на файл
[file for file in os.listdir(".") if os.path.isfile(file) and not file.startswitch('.')] # вывод файлов и отсев скрытых начинающихся с '.'

all_files = os.listdir(".")
files_only = []
for file in all_files:
    if os.path.isfile(file) and not file.startswith('.'):
        files_only.append(file)

