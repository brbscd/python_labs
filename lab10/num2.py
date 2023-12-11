f = list(map(str.strip, open("strings.txt", 'r', encoding='utf-8').readlines()))

print(sorted(f, key=lambda x:x.count('a'), reverse=True))