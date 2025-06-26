def reverse_str(strin, simb):
    strin = list(strin)  # Преобразование строки в список
    for i in range(0, len(strin), 2 * simb):
        # Меняем местами первые символы каждые 2n символов
        strin[i:i + simb] = reversed(strin[i:i + simb])
    return ''.join(strin)


# Пример использования
print(reverse_str("adcd", 2))     # Output: "dacd"
