# coding=utf-8

# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

user_name = input('Введите Ваше имя: ')
user_surname = input('Введите Ваш фамилию: ')
user_mail = input('Введите Ваш email: ')

NAME = '^[A-Z,А-Я]{1}[a-z,а-я]+$'
SURNAME = NAME
EMAIL = '^\w+\@\w+\.\w+$'

test_name = re.match(NAME, user_name) is None
test_surname = re.match(SURNAME, user_surname) is None
test_email = re.fullmatch(EMAIL, user_mail) is None

if test_name:
    test_name = 'Некорректно введено имя'
else:
    test_name = 'Имя корректно'

if test_surname:
    test_surname = 'Некорректно введена фамилия'
else:
    test_surname = 'Фамилия корректна'
if test_mail:
    test_mail = 'Некорректно введен email'
else:
    test_mail = 'email корректен'

print('{} {} has {} and {}, email {} is {}'.format(user_name, user_surnamee, test_name, test_surname, user_mail, test_mail))



# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

poem = len(re.findall('\.{2,}', some_str))
print(poem)
if poem > 0:
    print('В тексте встречается подряд более одной точки')
else:
    print('В тексте отсутствуют подряд более одной точки')