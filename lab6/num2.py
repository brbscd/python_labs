def matrix_composition(a, b):
    rows_a = len(a)
    cols_b = len(b[0])
    rows_b = len(b)  # строки второй матрицы и столбцы первой
    result = [[0 for i in range(cols2)] for j in range(rows1)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(rows_b):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


mat1 = []
mat2 = []
try:
    rows1 = int(input("Введите кол-во строк первой матрицы: "))
    cols1 = int(input("Введите кол-во столбцов первой матрицы: "))
    rows2 = int(input("Введите кол-во строк второй матрицы: "))  # кол-во столбцов первой матрицы
    cols2 = int(input("Введите кол-во столбцов второй матрицы: "))

except ValueError:
    print("Введен недопустимый элемент")
    exit()

if cols1 != rows2:
    print('Количество столбцов первой матрицы не совпадает с кол-во строк второй')
    exit()

try:
    print('Введите элементы первой матрицы:')
    mat1 = [[int(input()) for i in range(cols1)] for j in range(rows1)]
    print('Введите элементы второй матрицы:')
    mat2 = [[int(input()) for i in range(cols2)] for j in range(rows2)]

except ValueError:
    print("Введен недопустимый элемент")
    exit()

rez = matrix_composition(mat1, mat2)
print(f"Произведение матриц {mat1} и {mat2} равно:")
for i in rez:
    print(i)

