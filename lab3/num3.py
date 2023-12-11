from datetime import datetime, timedelta

print("Вычисление времени поездки в пути.")

try:
    print('Введите дату отправления поезда в формате ДД/ММ/ГГ ЧЧ:ММ')
    start_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
except:
    print('Дата в неверном формате')
    exit()


try:
    print('Введите дату прибытия поезда в формате ДД/ММ/ГГ ЧЧ:ММ')
    end_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
except ValueError:
    print('Дата в неверном формате')
    exit()
except TypeError:
    print("Введены не числовые значения")
    exit()


travel_time = end_date - start_date

print('Время поездки', travel_time)





