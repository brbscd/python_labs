#e) наименьшее общее кратное двух натуральных чисел
def nok(a, b):
    import math*
    return (a * b) / math.gcd(a, b)


try:
    num_x, num_y = map(int, input("Введите два числа через пробел: ").split())
except ValueError:
    print("Некорректные данные")
    exit()
print(f'Наибольшее общее кратное введеных чисел - {nok(num_x, num_y)}')
