№1
string = input("Введите 10 слов: ").split(';')
contr_string = input("Введите контрольную строку: ")

for i in range(len(string)):
    if string[i].isalpha():
        continue
    else:
        print("Введено что-то кроме букв")
        exit()

if len(string) == 10:
    for i in range(len(string)):
        if string[i].startswith(contr_string):
            print(string[i])
else:
    print("Введено несоответствующее количество слов")
    exit()







№2
a = []


def f(current):
    if len(a) == 0:
        a.append(current)
    if current > 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = current * 3 + 1
    if current == 1:
        a.append(1)
        return
    a.append(current)
    return f(current)


cnt = 0
try:
    x = int(input('Введите число: '))
except ValueError:
    print("Введено некорректное значение")
    exit()

if x <= 0:
    print("Введено некорректное значение, продолжить невозможно")
    exit()

f(x)


for i in a:
    cnt += 1
    if cnt == len(a):
        print(i)
        break
    print(i, '-> ', end='')  //что-то с join
print(f'Количество элементов: {len(a)}')
print(f'Пик последовательности: {max(a)}')


//изменить имена










№3
competition_list = {}

try:
    spisok = open('competition.txt', "r", encoding='utf-8').read().split()
    result = open('res.txt', 'w')
except FileNotFoundError:
    print("Файл не найден")
    exit()

for i in range(0, len(spisok) - 1, 2):
    competition_list[spisok[i]] = spisok[i + 1]

new_d = {}
for k,v in competition_list.items():
    new_d[k] = int(v)

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
    stroka = open('enter.txt', 'r', encoding='utf-8').readline()
    result = open('res1.txt', 'w', encoding='utf-8')
except FileNotFoundError:
    print("Файл не найден")
    exit()

stroka = stroka.lower()
a = Counter(stroka)

if len(a) == 0:
    print("Пустой файл")
    exit()

for key, value in a.items():
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
