#b) сумму n членов геометрической прогрессии;

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
    values = int(input("Введите количество элементов: "))
    begin = int(input("Введите первый член последовательности: "))
    znamenatel = int(input("Введите знаменатель последовательности: "))
    n = int(input(f"Введите сумму какого количества элементов прогрессии, не превышающее {values}, найти: "))
except ValueError:
    print("Введено некорректное решение")
    exit()

print(f'Сумма n-элементов последовательности равна {sum(geom_prog(begin, znamenatel, values)[:n + 1])}')