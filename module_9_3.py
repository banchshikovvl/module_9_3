"""
    ***Генераторные сборки***
"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

zp = zip(first, second)
first_result = (len(x) - len(y) for x, y in zp if len(x) != len(y))
print(f'Результат работы первой генераторной сборки: ', list(first_result))

second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))
print(f'Результат работы второй генераторной сборки: ', list(second_result))
