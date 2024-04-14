№1
def checking_the_string(string):
    if len(string) != 10:
        print("Введено несоответствующее количество слов")
        exit()

    for i in range(len(string)):
        if string[i].isalpha():
            continue
        if len(string) == 1 and not (string[i].isalpha()):
            print("Введена пустая строка")
            exit()
        else:
            print("Введено что-то кроме букв")
            exit()


string = input("Введите 10 слов: ").split(';')
contr_string = input("Введите контрольную строку: ")

if len(string) == 0:
    print("Введена пустая строка")
    exit()

checking_the_string(string)
checking_the_string(contr_string)

for i in range(len(string)):
    if string[i].startswith(contr_string):
        print(string[i])






№2
mas_of_nums = []


def turning_into_1(current):
    if len(mas_of_nums) == 0:
        mas_of_nums.append(current)
    if current > 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = current * 3 + 1
    if current == 1:
        mas_of_nums.append(1)
        return
    mas_of_nums.append(current)
    return turning_into_1(current)


cnt = 0
try:
    x = int(input('Введите число: '))
except ValueError:
    print("Введено некорректное значение, продолжить невозможно")
    exit()

if x <= 0:
    print("Введено некорректное значение, продолжить невозможно")
    exit()

turning_into_1(x)


print(' -> '.join(map(str, mas_of_nums)))
print(f'Количество элементов: {len(mas_of_nums)}')
print(f'Пик последовательности: {max(mas_of_nums)}')










№3
def convert_to_int_dict(input_dict):
    return {key: int(value) for key, value in input_dict.items()}


competition_list = {}
try:
    spisok = open('competition.txt', encoding='utf-8').read().split()
except FileNotFoundError:
    print("Файл не найден")
    exit()

result = open('res.txt', 'w')

for i in range(0, len(spisok) - 1, 2):
    competition_list[spisok[i]] = spisok[i + 1]

competition_list = convert_to_int_dict(competition_list)

sorted_comp_grade = sorted(competition_list.items(), key=lambda item: item[1])
sorted_comp_name = sorted(competition_list.items())

print('Изначальный словарь: \n', competition_list)
print('Отсортированный по баллам: \n', sorted_comp_grade)
print('Отсортированный по имени: \n', sorted_comp_name)

try:
    bal = int(input('Введите количество баллов: '))
except ValueError:
    print("Введено не числовое значение")
    exit()

for key, value in competition_list.items():
    if int(value) > bal:
        result.write(f'{key}, {value}\n')

result.close()








№4
from collections import Counter

try:
    stroka = open('enter.txt', encoding='utf-8').readline()
    result = open('res1.txt', 'w', encoding='utf-8')
except FileNotFoundError:
    print("Файл не найден")
    exit()

stroka = stroka.lower()
stroka = Counter(stroka)

if len(stroka) == 0:
    print("Пустой файл")
    exit()

for key, value in stroka.items():
    result.write(f'<{key}>: {value}\n')

result.close()






2 laba
#1
import json
import os
from pprint import pprint


ppath = "./animals.json"
if not os.path.exists(ppath):
    exit('не существует')
if os.path.splitext(ppath)[-1] != '.json':
    exit("неверное расширение")


with open("animals.json", "r") as read_file:
    data_animals = json.load(read_file)


print("Данные о всех птицах: ")
data_about_birds = list(filter(lambda x: x['animal_type'] == 'Bird', data_animals['animals']))
pprint(data_about_birds)



cnt = 0
for diurnal in data_animals['animals']:
    if diurnal['active_time'] == 'Diurnal':
        cnt += 1

print(f'Количество дневных животных равно {cnt}')

min_weight = 10000
animal_name = ''
for weight in data_animals['animals']:
    if float(weight['weight_min']) <= min_weight:
        min_weight = float(weight['weight_min'])
        animal_name = weight['name']

print(f'\nМинимальный вес имеет {animal_name}, весит {min_weight} кг')






#2
import csv
import os


ppath = "./countries.csv"
if not os.path.exists(ppath):
    exit("не существует")

if os.path.splitext(ppath)[-1] != '.csv': 
    exit("неверное расширение")

try:  
    min_income = float(input("Enter min income indicator: "))
    max_income = float(input("Enter max income indicator: "))
except Exception:
        exit('ничего не введено')

if (min_income < 0 or max_income < 0) or (min_income > max_income):
    print('entered number/s < 0 or min income > max income')
    exit()

csvfile = open(ppath)
try:
    countries = csv.reader(csvfile, delimiter=",") #quoting=csv.QUOTE_NONNUMERIC атоматическое преобразование типов данных
    titles = next(countries)
    sort_by_inflation = sorted(countries, key=lambda x: float(x[3]), reverse=False)
    sort_by_income = list(filter(lambda x: min_income <= float(x[2]) <= max_income, sort_by_inflation))
    if not(sort_by_income):
        print("There are no countries with this level of income")
except ValueError:
    print("empty file or noncorrect value/s")
    exit()

csvfile.close()

with open("NAMEFILE1.csv", "w") as csvfile: #создашь свои файлики в одной папке с этим файлом сюда введёшь названия
    file = csv.writer(csvfile, delimiter=",")
    file.writerow(titles)
    for line in sort_by_income:
        file.writerow(line)
        print(line)

with open("NAMEFILE2.csv", "w") as csvfile:
    file = csv.writer(csvfile, delimiter=",")
    file.writerow(titles)
    for line in sort_by_inflation:
        file.writerow(line)



3 laba
#1
import pytest


def factorial(n):
    if type(n) != int:
        raise TypeError()

    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def test_factorial():
    assert factorial(3) == 6


def test_exception_factorial():
    with pytest.raises(TypeError):
        factorial('3')


def test_exception_list():
    with pytest.raises(TypeError):
        factorial([2, 3])






#2
import pytest


def palindrom(string):
    if type(string) != str:
        raise TypeError()
    if len(string) < 3:
        return 'no'

    len_of_str = len(string) // 2
    if string[:len_of_str] == (string[-len_of_str:])[::-1]:
        return 'yes'
    else:
        return 'no'


def test_palindrom():
    assert palindrom('askksa') == 'yes'


def test_exception_palindrom():
    with pytest.raises(TypeError):
        palindrom(12321)


def test_exception_list():
    with pytest.raises(TypeError):
        palindrom(['a', 's', 'k', 'k', 's', 'a'])







#3
import pytest


def count_elem(string):
    if type(string) != str:
        raise TypeError()

    cnt = set()
    for i in range(len(string)):
        if string.count(string[i]) > 1:
            cnt.add(string[i])

    return len(cnt)


def test_count_elem():
    assert count_elem('tralalio') == 2


def test_exception_count_elem():
    with pytest.raises(TypeError):
        count_elem(12321)


def test_exception_list():
    with pytest.raises(TypeError):
        count_elem(['a', 's', 'u', 'k', 't', 'a'])

