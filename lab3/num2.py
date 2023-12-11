import math

print("Вычисление наибольшего общего делителя.")
x, y = 0, 0

def nod(x, y):
    delit = []
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0: delit.append(i)
    if len(delit) == 1 and delit[0] == 1: return ("\nИспользуя мою функцию, получим, что это взамино простые числа")
    if len(delit) != 1: return (f"\nИспользуя мою функцию, получим, что НОД этих двух чисел равен {max(delit)}")


try:
    x, y = map(int, input("Введите два натуральных числа: ").split())
    if x <= 0 or y <= 0:
        print("Введены не натуральные числа")
        exit()
except ValueError:
    print("Введены некорректные значения")
    exit()
except TypeError:
    print("Введены не числовые значения")
    exit()


print(nod(int(x), int(y)))

print(f"Используя встроенную функцию, получим результат: {math.gcd(x, y)}")
