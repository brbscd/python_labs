import math

print("Вычисление синуса, косинуса и тангенса угла.")

try:
    ugol = int(input("Введите величину угла на плоскоти в градусах: "))
    if ugol > 360 or ugol < 0:
        print("Введено некорректное значение")
        exit()
except ValueError:
    print("Введено некорректное значение")
    exit()
except TypeError:
    print("\nВведены не числовые значения")
    exit()

print(f"Синус такого угла равен {round(math.sin(math.radians(ugol)), 5)}")
print(f"Косинус такого угла равен {round(math.cos(math.radians(ugol)), 5)}")
print(f"Тангенс такого угла равен {round(math.tan(math.radians(ugol)), 5)}")
