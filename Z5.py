def get_row(rowIndex):
    row = [1]  # Начало с первой строки
    for _ in range(rowIndex):
        # Формирование след. строки на основе текущей
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    return row


# Примеры использования
print(get_row(0))  # Output: [1]
print(get_row(2))  # Output: [1, 2, 1]
print(get_row(4))  # Output: [1, 4, 6, 4, 1]
print(get_row(6))  # Output: [1, 6, 15, 20, 15, 6, 1]
