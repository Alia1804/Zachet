def create_abbreviation(phrase):
    words = phrase.split()  # Разделить фразу на слова
    abbreviation = ""
    for word in words:
        if word[0].isalpha():  # Проверить начинается ли слово с буквы
            abbreviation += word[0].upper()  # Добавить первую букву в верхнем рег.
    return abbreviation


#Примеры использования
print(create_abbreviation("Привет я Алина"))  # Ожидаемый результат: ПЯИ
print(create_abbreviation("Высшая математика"))  # Ожидаемый результат: ВМ
