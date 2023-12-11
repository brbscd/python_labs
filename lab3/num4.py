from datetime import datetime, timedelta
try:
    print("Введите дату вашего рождения в формате ДД/ММ/ГГГГ: ")
    birth_date = datetime.strptime(input(), "%d/%m/%Y")
except ValueError:
    print('Дата в неверном формате')
    exit()
except TypeError:
    print("Введены не числовые значения")
    exit()

secs = timedelta(seconds = 1_000_000_000)
mins = timedelta(minutes = 1_000_000)
days = timedelta(days = 10_000)

print(f"Вам исполнится 10_000 дней {birth_date + days}")
print(f"Вам исполнится 10_000_000 минут {birth_date + mins}")
print(f"Вам исполнится 10_000_000_000 секунд {birth_date + secs}")