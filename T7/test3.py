def calculate_positive_average(numbers):
    """
    Вычисляет среднее арифметическое положительных элементов в списке `numbers`.
    Возвращает 0, если положительных элементов нет.
    """
    # Проверка предусловий
    if not isinstance(numbers, list):
        raise TypeError("Вход должен быть списком")
    if any(not isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Все элементы списка должны быть числами")

    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
            count += 1

    if count > 0:
        average = total / count  # Строка A
    else:
        average = 0
    return average
