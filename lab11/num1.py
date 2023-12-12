string  = input("Введите строку: ")
mas = list(string)

if len(mas) < 3:
    print("Длина слова должна быть не менее трех")
    exit()

ln_ms = len(mas) // 2
if len(mas) % 2 == 0:
    stek = mas[:ln_ms]
    mas = mas[ln_ms:]

else:
    stek = mas[:ln_ms]
    mas = mas[ln_ms:]
    mas.pop(0)

for i in range(len(stek) - 1):
    elem_stek = stek.pop()
    if elem_stek != mas[i]:
        print("Слово не является полиндромом")
        exit()

print("Слово является полиндромом")