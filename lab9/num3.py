try:
    f = open('matrix.txt', 'r').readlines()
except FileNotFoundError:
    print(f"Файл matrix.txt не найден")
    exit()

try:
    w = open('rematrix.txt', 'w')
except FileNotFoundError:
    print(f"Файл rematrix.txt не найден")
    exit()

g, h, m = [], [], []

#добавляем каждую строку как элемент в массив
for i in range(len(f)):
    g.append(list(map(int, f[i].split())))

#вывод исходника
for i in range(len(g)):
    for j in range(len(g[i])):
        print(g[i][j], end=' ')
    print()

print()

#создаем массив столбцов
for j in range(len(g)):
    for i in range(len(g[j])):
        m.append(g[i][j])
    h.append(m)
    m = []

#теперь создаем файл и вписываем туда все стобцы как строки
for i in range(len(h)):
    for j in range(len(h[i])):
        w.write(" " + str(h[i][j]))
        print(h[i][j], end=' ')
    print()
    w.write("\n")

w.close()