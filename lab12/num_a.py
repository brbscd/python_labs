#a) n-й член геометрической прогрессии;

g = []


def geom_prog(nul, znam, amount):
    g.append(nul)
    nul *= znam
    amount -= 1
    if amount != 0:
        return geom_prog(nul, znam, amount)
    else:
        return g


try:
    amount = int(input("Введите количество элементов: "))
    begin = int(input("Введите первый член последовательности: "))
    znamenatel = int(input("Введите знаменатель последовательности: "))
    n = int(input("Введите необходимый элемент геометрической прогрессии: "))
except ValueError:
    print("Введено некорректное решение")
    exit()

print(f'Необходимый элемент - {geom_prog(begin, znamenatel, amount + 1)[n]}')