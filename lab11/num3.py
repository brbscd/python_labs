try:
    f = open("bankstack.txt", 'r', encoding='utf-8').readlines()
except FileNotFoundError:
    print("Файл bankstack.txt не найден")
    exit()

lines = ''.join(f)
lines = lines.split("\n")

stek = []
for i in lines:
    stek.append(i.split(", "))

#print(stek)
for i in range(len(stek)):
    while len(stek[i]) != len(max(stek, key=len)):
        stek[i].append("*")

#print(stek)

for i in range(len(stek)):
    for j in range(len(stek[0])):
        if stek[j][i] != '*':
            print(stek[j][i])