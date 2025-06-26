import random  # Импорт модуля random для генерации случ. чисел

class Card:  # Класс для представления карточки игрока
    rows = 3  # Кол-во строк в карточке
    columns = 9  # Кол-во столбцов в карточке
    numders_per_row = 5  # Кол-во чисел в строке

    def __init__(self):
        self.card_numbers = self._generate_card()  # Генерация карточку с числами
        self.marked_positions = [[False] * self.columns for _ in range(self.rows)]  # Массив для отмеченных позиций

    def _generate_card(self):
        all_unique_numbers = random.sample(range(1, 91), self.rows * self.numbers)  # Получили уникальные числа для карточки
        card_rows = []  # Список для хранения строк карточки
        for row_index in range(self.rows):  # Для каждой строки
            row_numbers = sorted(all_unique_numbers[row_index * self.numbers_per_row:(row_index + 1) * self.NUMBERS_PER_ROW])  # Сортируем числа в строке по возрастанию
            row = [''] * self.columns  # Создание пустой строки из 9 элементов
            positions_for_numbers = sorted(random.sample(range(self.columns), self.numbers_per_row))  # Выбор случайные позиции для чисел
            for position, number in zip(positions_for_numbers, row_numbers):  # Для каждой позиции и числа
                row[position] = number  # Вставить число в нужную позицию
            card_rows.append(row)  # Добавить строку в карточку
        return card_rows  # Возврат сгенерированнуой карточки

    def has_number(self, number_to_check):
        for row_index in range(self.rows):  # Проход по всем строкам
            for column_index in range(self.columns):  # Проход по всем столбцам
                if self.card_numbers[row_index][column_index] == number_to_check and not self.marked_positions[row_index][column_index]:  # Если число найдено и не зачеркнуто
                    return True  # Возврат True
        return False  # Если число не найдено, возврат False

    def mark_number(self, number_to_mark):
        for row_index in range(self.rows):  # Проход по всем строкам
            for column_index in range(self.columns):  # Проход по всем столбцам
                if self.card_numbers[row_index][column_index] == number_to_mark:  # Если найдено нужное число
                    self.marked_positions[row_index][column_index] = True  # Отметить его как зачеркнутое

    def is_complete(self):
        for row_index in range(self.rows):  # Проходим по всем строкам
            for column_index in range(self.columns):  # Проходим по всем столбцам
                if self.card_numbers[row_index][column_index] != '' and not self.marked_positions[row_index][column_index]:  # Если есть не зачеркнутое число
                    return False  # Карточка не заполнена полностью
        return True  # Все числа зачеркнуты

    def __str__(self):
        card_lines = []  # Список для строк карточки
        card_lines.append('-' * 26)  # Верхняя граница карточки
        for row_index in range(self.rows):  # Для каждой строки
            line = ''  # Строка для вывода
            for column_index in range(self.columns):  # Для каждого столбца
                value = self.card_numbers[row_index][column_index]  # Получаем значение ячейки
                if value == '':  # Если ячейка пустая
                    line += '   '  # Добавляем пробелы
                elif self.marked_positions[row_index][column_index]:  # Если число зачеркнуто
                    line += ' - '  # Добавляем прочерк
                else:
                    line += f'{value:2d} '  # Добавляем число с выравниванием
            card_lines.append(line)  # Добавляем строку в список
        card_lines.append('-' * 26)  # Нижняя граница карточки
        return '\n'.join(card_lines)  # Возвращаем карточку в виде строки

class BarrelBag:  # Класс для мешка с бочонками
    def __init__(self):
        self.barrel_numbers = list(range(1, 91))  # Список всех бочонков от 1 до 90
        random.shuffle(self.barrel_numbers)  # Перемешиваем бочонки

    def draw_barrel(self):
        if self.barrel_numbers:  # Если есть бочонки
            return self.barrel_numbers.pop()  # Достаем один бочонок
        return None  # Если бочонки закончились, возвращаем None

    def barrels_left(self):
        return len(self.barrel_numbers)  # Возвращаем количество оставшихся бочонков

class Player:  # Класс для игрока
    def __init__(self, player_name):
        self.name = player_name  # Имя игрока
        self.card = Card()  # Карточка игрока

    def has_won(self):
        return self.card.is_complete()  # Проверяем, заполнена ли карточка

class LotoGame:  # Класс для игры Лото
    def __init__(self):
        self.user_player = Player("Вы")  # Создаем игрока-пользователя
        self.computer_player = Player("Компьютер")  # Создаем игрока-компьютера
        self.barrel_bag = BarrelBag()  # Создаем мешок с бочонками

    def play(self):
        while True:  # Основной игровой цикл
            current_barrel = self.barrel_bag.draw_barrel()  # Достаем новый бочонок
            if current_barrel is None:  # Если бочонки закончились
                print("Бочонки закончились! Это означает ничью.")  # Сообщаем о ничьей
                break  # Завершаем игру
            print(f"Новый бочонок: {current_barrel} (осталось {self.barrel_bag.barrels_left()})")  # Показываем номер бочонка и сколько осталось
            print("------ Ваша карточка -----")  # Заголовок карточки пользователя
            print(self.user_player.card)  # Выводим карточку пользователя
            print("-- Карточка компьютера ---")  # Заголовок карточки компьютера
            print(self.computer_player.card)  # Выводим карточку компьютера
            user_input = input("Зачеркнуть цифру? (y/n): ").strip().lower()  # Запрашиваем у пользователя действие
            user_has_number = self.user_player.card.has_number(current_barrel)  # Проверяем, есть ли число на карточке пользователя
            if user_input == 'y':  # Если пользователь хочет зачеркнуть
                if user_has_number:  # Если число есть на карточке
                    self.user_player.card.mark_number(current_barrel)  # Зачеркиваем число
                else:  # Если числа нет на карточке
                    print("Число отсутствует на вашей карточке. Вы проиграли!")  # Сообщаем о проигрыше
                    return  # Завершаем игру
            elif user_input == 'n':  # Если пользователь не хочет зачеркивать
                if user_has_number:  # Если число есть на карточке
                    print("Число было на вашей карточке. Вы проиграли!")  # Сообщаем о проигрыше
                    return  # Завершаем игру
            else:  # Если введено что-то другое
                print("Некорректный ввод. Попробуйте снова.")  # Сообщаем об ошибке
                continue  # Переходим к следующей итерации
            if self.computer_player.card.has_number(current_barrel):  # Если у компьютера есть это число
                self.computer_player.card.mark_number(current_barrel)  # Компьютер всегда зачеркивает число
            if self.user_player.has_won():  # Проверяем, выиграл ли пользователь
                print("Вы стали победителем!Поздравляю!")  # Сообщаем о победе пользователя
                print(self.user_player.card)  # Показываем карточку пользователя
                return  # Завершаем игру
            if self.computer_player.has_won():  # Проверяем, выиграл ли компьютер
                print("Компьютер победил! Увы.")  # Сообщаем о победе компьютера
                print(self.computer_player.card)  # Показываем карточку компьютера
                return  # Завершаем игру

if __name__ == "__main__":  # Если файл запущен как основная программа
    LotoGame().play()
