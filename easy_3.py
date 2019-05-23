# coding=utf-8

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def about_user (name, age, city):
    result = '{}, {} год(а), проживает в городе {}'.format(name, age, city)
    return result

name = input('Укакжите имя: ')
age = input('Укажите возраст: ')
city = input('Укажите город проживания: ')

result = about_user(name, age, city)
print(result)

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_number(a, b, c):
    num_list = [a,b,c]
    max_num = (max(num_list))
    return max_num

num_1 = int (input('Введите значение первого числа: '))
num_2 = int (input('Введите значение второго числа: '))
num_3 = int (input('Введите значение третьего числа: '))

result = max_number(num_1, num_2, num_3)
print('Максимальное число: {}'.format(result))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def max_str (* arg):
    max_len = max (arg, key = len)
    return max_len

arg_1 = input('Введите первыю строку: ')
arg_2 = input('Введите вторую строку: ')
arg_3 = input('Введите трутью строку: ')

result = max_str(arg_1, arg_2, arg_3)
print('Самая длинная строка из полученных аргументов: : {}'.format(result))