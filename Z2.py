def count_digits(num):
    digit_count = {str(digit): 0 for digit in range(10)}  # Инициализация словаря
    for digit in str(num):  # Преобразовка числа в строку и перебор
        digit_count[digit] += 1
    return digit_count


# Пример использования
num = int(input("Положительное целое число: "))
result = count_digits(num)
print("Частота цифр:")
for digit, count in result.items():
    print(f"{digit}: {count}")
