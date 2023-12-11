from collections import Counter


print("Введите массив: ")
mass = [int(s) for s in input().split()]
x = Counter(mass).most_common()[0][0]
if Counter(mass).most_common()[0][1] != Counter(mass).most_common()[1][1]:
    print("Мода массива:", x)
else:
    print("У данного массива нет моды")
