# coding=utf-8

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

numbers = [1, 2, 4, 0]
numbers_sqr = [a ** 2 for a in numbers]
print(numbers_sqr)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits = ['яблоко', 'банан', 'киви', 'груша']
fruits_sec = ['нектарин', 'мандарин', 'персик', 'апельсин']
fruit_list = list (set (fruits) & set (fruits_sec))
print(fruit_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

numbers = [5, 10, 47, -9, 8, -84, 33]
new_list = [a for a in numbers if a % 3 == 0 and a >=0 and a % 4 !=0]
print(new_list)