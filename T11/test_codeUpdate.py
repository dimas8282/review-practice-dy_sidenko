# Задача 1: Факториал (исправленный)
def factorial(n):
    result = 1
    for i in range(1, n + 1):  # Исправлен диапазон
        result *= i
    return result

print(factorial(5))  # Теперь выводит 120


# Задача 2: Проверка пароля (без изменений, логика верная)
def check_password(password):
    if len(password) < 8:
        return "Слишком короткий!"
    elif not any(char.isdigit() for char in password):
        return "Нет цифр!"
    else:
        return "Пароль надёжен!"

print(check_password("qwerty"))  # Теперь останавливается на точке останова


# Задача 3: Сумма элементов массива (исправленный)
def calculate_sum(arr):
    total = 0
    for i in range(0, len(arr)):  # Исправлен диапазон
        total += arr[i]
    return total

numbers = [10, 20, 30]
print(calculate_sum(numbers))  # Теперь выводит 60
