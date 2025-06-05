# Задача 1: Факториал
def factorial(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

print(factorial(5))  # Выводит 24, ожидалось 120


# Задача 2: Проверка пароля
def check_password(password):
    if len(password) < 8:
        return "Слишком короткий!"
    elif not any(char.isdigit() for char in password):
        return "Нет цифр!"
    else:
        return "Пароль надёжен!"

print(check_password("qwerty"))  # Ожидалось "Слишком короткий!"


# Задача 3: Сумма элементов массива
def calculate_sum(arr):
    total = 0
    for i in range(0, len(arr) + 1):  # Выход за границы массива
        total += arr[i]
    return total

numbers = [10, 20, 30]
print(calculate_sum(numbers))  # IndexError
