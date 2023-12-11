f = open('vector.txt', 'r').read().split()
print(f)


def work_vector(file, number_count):
    for i in range(number_count):
        file.pop(-1)
    return " ".join(file)



i = int(input(f"Введите количество чисел, не превышающее {len(f)}, для удаления: "))
if i > len(f) or i < 0:
    print("Введено некорректное значение.")
    exit()

g = open('revector.txt', 'w')
g.write(work_vector(f, i))
g.close()

