# coding=utf-8
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
first_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []
for numbers in first_list:
    if numbers > 0 and math.sqrt(numbers) % 1 == 0:
        new_list.append(int(math.sqrt(numbers)))
print(new_list)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input('Введите дату в формате dd.mm.yyyy: ')
date_list = date.split('.')
name_months = {
'01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая', '06': 'июня', '07': 'июля',
'08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря',
}
name_days = {
'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
'06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
'11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
'16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
'21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
'25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
'29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое',
}
for key in name_days:
    if date_list[0] == key:
        date_list[0] = name_days[key]

for key in name_months:
    if date_list[1] == key:
        date_list[1] = name_months[key]

date_name = date_list[0] + ' ' + date_list[1] + ' ' + date_list[2] + ' ' "года"
print(date_name)


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

n =  int(input('Введите количество элементов массива: '))
from random import randint
print([randint(-100, 100) for _ in range(n)])

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
new_lst = set(lst)
print(new_lst)

# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
sec_lst = []
for item in lst:
    if lst.count(item) == 1:
        sec_lst.append(item)
print(sec_lst)