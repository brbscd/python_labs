string = input("Введите строку: ")
stack = list(string)
print(''.join(stack.pop() for a in range (len(string))))