#d) двоичное представление десятичного числа;
def bin_convert(n):
    if n < 0:
        return 'Для действия необходимо положительное число'
    elif n == 0:
        return '0'
    else:
        return bin_convert(n // 2) + str(n % 2)


try:
    n = int(input("Введите число для перевода из десятичной в двоичную систему: "))
except ValueError:
    print("Введено некорректное значение")
    exit()

#убираем ночь в начале, если он есть
if str(bin_convert(n))[0] == '0':
    r = str(bin_convert(n))[1:]
print(f'Введенное число в двоичной системе равно {r}')