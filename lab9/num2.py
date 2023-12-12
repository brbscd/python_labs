import re

try:
    f = open('text.txt', 'r').read()
except FileNotFoundError:
    print(f"Файл text.txt не найден")
    exit()

f = re.split("!|\\?|\\.", f)
#убираем последний пустой элемент
f.pop()
text_count = []

try:
    number = int(input("Введите количество слов в предложении: "))
except TypeError:
    print("Ошибка при вводе значения")
    exit()
except ValueError:
    print("Ошибка при вводе значения")
    exit()

for i in range(len(f)):
    strg = f[i].split()
    if len(strg) > number:
        text_count.append(f[i] + '.')

try:
    h = open('retext.txt', 'w')
except FileNotFoundError:
    print(f"Файл retext.txt не найден")
    exit()

h.write("".join(text_count))
h.close()