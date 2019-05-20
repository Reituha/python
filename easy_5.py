# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

print('Текущая директория {}'.format(os.getcwd()))


def makedir(i):
    os.mkdir('{}'.format(i))


def removedir(i):
    os.rmdir('{}'.format(i))


def chdir(i):
    os.chdir(i)


for r in range(9):
    makedir('dir_{}'.format(r + 1))
print(os.listdir())
for r in range(9):
    removedir('dir_{}'.format(r + 1))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def nowdir():
    print('Содержимое текущей папки: {}'.format(os.listdir()))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file(first_file, backup_file):
    shutil.copy(first_file, backup_file)

def delete_dir(dir_path):
    dir_path = os.path.join(os.getcwd(), dir_path)
    try:
        0
        os.rmdir(dir_path)
    except:
        print(dir_path + ' - директория отсуствует')


def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')

# dir_path = 'C:\Users\Ekaterina\PycharmProjects\untitled\dir_9'
# change_dir(dir_path)
