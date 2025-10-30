def month_to_season(month):
    if month == 1 or month == 2 or month == 12:
        return "Зима"
    if month == 3 or month == 4 or month == 5:
        return "Весна"
    if month == 6 or month == 7 or month == 8:
        return "Лето"
    if month == 9 or month == 10 or month == 11:
        return "Осень"
    else:
        return "Неверный номер месяца"

try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month)) 
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")