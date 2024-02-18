#1
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







#2 - обработка 0
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


f(x)


for i in a:
    cnt += 1
    if cnt == len(a):
        print(i)
        break
    print(i, '-> ', end='')
print(f'Количество элементов: {len(a)}')
print(f'Пик последовательности: {max(a)}')







#3
competition_list = {}

try:
    spisok = open('competition.txt', "r", encoding='utf-8').read().split()
    result = open('res.txt', 'w')
except FileNotFoundError:
    print("Файл не существует")
    exit()

for i in range(0, len(spisok) - 1, 2):
    competition_list[spisok[i]] = spisok[i + 1]

sorted_comp_grade = sorted(competition_list.items(), key=lambda item: item[1])
sorted_comp_name = sorted(competition_list.items())

print('Изначальный словарь: \n', competition_list)
print('Отсортированный по баллам: \n', sorted_comp_grade)
print('Отсортированный по имени: \n', sorted_comp_name)

n = int(input('Введите количество баллов: '))

for key, value in competition_list.items():
    if int(value) > n:
        result.write(f'{key}, {value}\n')

result.close()








#4
import re


stroka = open('enter.txt', 'r', encoding='utf-8').readline()
stroka = re.split(',', stroka)
print(stroka)
