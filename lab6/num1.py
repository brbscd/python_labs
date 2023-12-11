def scalar_composition(x, y):
    if len(x) != len(y):
        print('Размерность векторов не совпадает.')
        exit()
    else:
        rez = 0
        for i in range(len(x)):
            rez += x[i] * y[i]

        return rez


try:
    vec1 = input("Введите элементы первого вектора: ").split()
    vec1 = list(map(int, vec1))
    vec2 = input("Введите элементы второго вектора: ").split()
    vec2 = list(map(int, vec2))

    rez = scalar_composition(vec1, vec2)
    print(f"Скалярное произведение векторов {vec1} и {vec2} равно: {rez}")

except ValueError:
    print("Введен недопустимый элемент")
    exit()

