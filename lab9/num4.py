try:
    f = open('chapter.txt', 'r').readlines()

except FileNotFoundError:
    print(f"Файл chapter.txt не найден")
    exit()

text = "".join(f).split('\n')
string = ''
content = ["Оглавление"]
for i in range(len(text)):
    if "Chapter" in text[i] or "Глава" in text[i]:
        string = text[i] + ". " + text[i + 1]
        content.append(string)

w = open("rechapter.txt", 'w')
for i in content:
    w.write(i)
    w.write("\n")

w.close()