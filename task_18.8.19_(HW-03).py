# Запрашиваем количество билетов
number_of_tickets = int(input("Введите количество билетов: "))

# Инициализируем сумму стоимости билетов
total_cost = 0

# Обрабатываем каждый билет
for _ in range(number_of_tickets):
    # Запрашиваем возраст посетителя
    age = int(input("Введите возраст посетителя: "))

    # Определяем стоимость билета в зависимости от возраста
    if age < 18:
        cost = 0
    elif 18 <= age <= 25:
        cost = 990
    else:
        cost = 1390

    # Добавляем стоимость билета к общей сумме
    total_cost += cost

# Проверяем, применилась ли скидка
if number_of_tickets >= 4:
    total_cost -= total_cost * 0.1  # Скидка 10%

# Выводим общую стоимость
print(f"Общая стоимость билетов: {total_cost} рублей")