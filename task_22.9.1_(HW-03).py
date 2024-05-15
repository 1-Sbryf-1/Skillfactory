def binary_search(arr, x):
    """Функция для двоичного поиска индекса элемента в отсортированном массиве."""
    left, right = 0, len(arr) - 1
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return res

def find_position(sorted_list, user_number):
    """Функция для нахождения позиции элемента в отсортированном списке."""
    position = binary_search(sorted_list, user_number)
    if position != -1 and sorted_list[position] == user_number:
        return position
    else:
        print("Число не соответствует условиям.")
        return None

# Чтение последовательности чисел и преобразование в список
numbers = input("Введите последовательность чисел через пробел: ").split()
numbers = list(map(int, numbers))

# Запрос числа у пользователя
user_number = int(input("Введите число: "))

# Проверка соответствия введенных данных
if not all(isinstance(num, int) for num in numbers):
    print("Не все числа введены корректно.")
else:
    # Преобразование последовательности в отсортированный список
    sorted_list = sorted(numbers)

    # Поиск позиции элемента
    position = find_position(sorted_list, user_number)

    # Вывод результата
    if position is not None:
        print(f"Позиция числа {user_number}: {position}")