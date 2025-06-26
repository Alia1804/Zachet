def fibonacci(n):
    count_one, count_two = 0, 1  # Первые два числа посл.Фиб.
    for _ in range(n):
        yield count_one  # Возврат текущего числа
        count_one, count_two = count_two,count_one + count_two  # Обновление значений для следующей ит.


# Пример использования
for num in fibonacci(6):
    print(num)
