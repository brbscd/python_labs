try:
    f = open('vector.txt', 'r').read().split()
except FileNotFoundError:
    print(f"Файл vector.txt не найден")
    exit()


def work_vector(file, number_count):
    for i in range(number_count):
        file.pop()
    return " ".join(file)

try:
    i = int(input(f"Введите количество чисел, не превышающее {len(f)}, для удаления: "))
except TypeError:
    print("Ошибка при вводе значения")
    exit()
except ValueError:
    print("Ошибка при вводе значения")
    exit()

if i > len(f) or i < 0:
    print("Введено некорректное значение.")
    exit()

try:
    g = open('revector.txt', 'w')
except FileNotFoundError:
    print(f"Файл revector.txt не найден")
    exit()

g.write(work_vector(f, i))
g.close()

