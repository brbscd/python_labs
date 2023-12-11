import re

f = open('text.txt', 'r').read()
f = re.split("!|\\?|\\.", f)
#убираем последний пустой элемент
f.pop()
text_count = []
number = int(input("Введите количество слов в предложении: "))

for i in range(len(f)):
    strg = f[i].split()
    if len(strg) > number:
        text_count.append(f[i] + '.')

h = open('retext.txt', 'w')
h.write("".join(text_count))