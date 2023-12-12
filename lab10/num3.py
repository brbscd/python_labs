try:
    f = open("peoplenames.txt", 'r', encoding='utf-8').readline().split(" ")

except FileNotFoundError:
    print(f"Файл peoplenames.txt не найден")
    exit()

g = []
for i in range(0, len(f), 2):
    slovar = {}
    slovar = {"Фамилия": f"{f[i]}", "Год рождения": f"{f[i + 1]}"}
    g.append(slovar)

print("Сортировка словаря по возрастанию возраста: ")
g_sorted1 = sorted(g, key=lambda x: x['Год рождения'], reverse=True)
print(g_sorted1)

print("\n")

print("Сортировка словаря в алфавитном порядке по фамиилии: ")
g_sorted2 = sorted(g, key=lambda x: x['Фамилия'])
print(g_sorted2)