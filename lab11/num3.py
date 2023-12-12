try:
    f = open("bankstack.txt", 'r', encoding='utf-8').readlines()
except FileNotFoundError:
    print("Файл bankstack.txt не найден")
    exit()

string = "".join(f)
string = string.split("\n")

stek = []

for i in string:
    stek.append(i.split(","))

print(stek)

for i in range(len(stek) - 1):
    for j in range(len(stek[0]) + 1):
        if stek[j][i] != "*":
            print(stek[j][i])
