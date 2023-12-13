#e) наименьшее общее кратное двух натуральных чисел
def nok(a, b):
    c = a % b
    if c == 0:
        return a
    return a * nok(b, c) // c


try:
    num_x, num_y = map(int, input("Введите два числа через пробел: ").split())
except ValueError:
    print("Некорректные данные")
    exit()
print(f'Наибольшее общее кратное введеных чисел - {nok(num_x, num_y)}')
