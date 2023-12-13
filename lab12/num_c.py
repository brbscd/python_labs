#c) n-й член арифметической прогрессии;

h = []


def arif_prog(nul, razn, amount):
    h.append(nul)
    nul += razn
    amount -= 1
    if amount != 0:
        return arif_prog(nul, razn, amount)
    else:
        return h


try:
    amount = int(input("Введите количество элементов арифметической прогрессии: "))
    begin = int(input("Введите первый элемент арифметической прогрессии: "))
    razn = int(input("Введите разность арифметической прогрессии: "))
    n = int(input(f"Введите искомый элемент последовательности, не превышающий {amount}: "))
except ValueError:
    print("Введено некорректное решение")
    exit()

print(f'\nИскомый элемент - {arif_prog(begin, razn, amount + 1)[n]}')