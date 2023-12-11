f = open('chapter.txt', 'r').readlines()
text = "".join(f).split('\n')
print(text)
stroka = ''
oglavlenie = ["Оглавление"]
for i in range(len(text)):
    if "Chapter" in text[i] or "Глава" in text[i]:
        stroka = text[i] + ". " + text[i + 1]
        oglavlenie.append(stroka)

print(oglavlenie)
w = open("rechapter.txt", 'w')
for i in oglavlenie:
    w.write(i)
    w.write("\n")