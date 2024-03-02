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



with open ("animals.json", "r") as read_file:
    data_animals = json.load(read_file)

for bird in data_animals['animals']:
    if bird['animal_type'] == 'Bird':
        print(bird)

cnt = 0
for diurnal in data_animals['animals']:
    if diurnal['active_time'] == 'Diurnal':
        cnt += 1

print(f'Количество дневных животных равно {cnt}')

data_animals = sorted(data_animals, key=lambda data: data['weight_min'])
print(data_animals)
