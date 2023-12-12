import time
import random


def bubble_sort(spisok):
    start = time.time()
    random_lst = spisok
    counter, storage = 1, 0
    while counter != 0:
        counter = 0
        for i in range(1, len(random_lst)):
            if random_lst[i - 1] > random_lst[i]:
                #меняем соседние элементы местами
                storage = random_lst[i - 1]
                random_lst[i - 1] = random_lst[i]
                random_lst[i] = storage
                counter += 1
    end = time.time() - start

    return end


def time_func_sort(spisok):
    random_lst = spisok
    start = time.time()
    g = sorted(random_lst)
    end = time.time() - start
    return end


lst = [random.randint(0, 100) for _ in range(100)]
bubble = bubble_sort(lst)
func = time_func_sort(lst)

if bubble > func:
    print(f'Встроенная функция работает быстрее, чем моя, на {round(bubble - func, 8)} секунд')
    exit()
if bubble < func:
    print(f'Моя функция работает быстрее, чем встроенная, на {round(func - bubble, 8)} секунд')
    exit()
if bubble == func:
    print(f'Обе функции работают одинаково - {round(func, 8)} секунд')



