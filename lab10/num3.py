from operator import itemgetter

f = open("peoplenames.txt", 'r', encoding='utf-8').readline().split(" ")
print(f)

g = []
for i in range(0, len(f), 2):
    slovar = {}
    slovar = {"Фамилия": f"{f[i]}", "Год рождения": f"{f[i + 1]}"}
    g.append(slovar)

print("Сортировка словаря по возрастанию возраста")
#print(sorted(g, key=itemgetter("Фамилия", "Год рождения")))
g_sorted1 = sorted(g.items(), key=lambda item: item[1], reverse=True)
print(g_sorted1)