try:
    books_dict = {}
    while True:
        author = input("Введите фамилию автора для добавления его книг в список (для перехода к выводу напишите 'дальше'):\n").capitalize()
        if author.lower() == 'дальше':
            break
        book = input("Введите название книги, которое Вы хотите добавить: ").split(',')
        books_dict[author] = book

    while True:
        ans = input("Введите фамилию автора для просмотра его работ (для завершения работы введите 'выход':\n").capitalize()
        if ans.lower() == 'выход':
            break
        if ans in books_dict:
            print(f"Произведения данного автора - {ans}: {', '.join(books_dict[ans])}\n")
        else:
            print("\nДанного автора нет в списке")

except KeyError as err:
    print(f"Ошибка: {err}")



