def cnt_a(f):
    return f.count('а') + f.count('А')


try:
    f = list(map(str.strip, open("strings.txt", 'r', encoding='utf-8').readlines()))

except FileNotFoundError:
    print(f"Файл strings.txt не найден")
    exit()

f2 = sorted(f, key=lambda x:cnt_a(x), reverse=True)
print(f2)