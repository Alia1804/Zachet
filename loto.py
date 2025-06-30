import random

class Card:
    ROWS = 3
    COLUMNS = 9
    NUMBERS_PER_ROW = 5

    def __init__(self):
        self.card_numbers = self._generate_card()
        self.marked_positions = [[False] * self.COLUMNS for _ in range(self.ROWS)]

    def _generate_card(self):
        all_unique_numbers = random.sample(range(1, 91), self.ROWS * self.NUMBERS_PER_ROW)
        card_rows = []
        for row_index in range(self.ROWS):
            row_numbers = sorted(all_unique_numbers[row_index * self.NUMBERS_PER_ROW:(row_index + 1) * self.NUMBERS_PER_ROW])
            row = [''] * self.COLUMNS
            positions_for_numbers = sorted(random.sample(range(self.COLUMNS), self.NUMBERS_PER_ROW))
            for position, number in zip(positions_for_numbers, row_numbers):
                row[position] = number
            card_rows.append(row)
        return card_rows

    def has_number(self, number_to_check):
        for row_index in range(self.ROWS):
            for column_index in range(self.COLUMNS):
                if self.card_numbers[row_index][column_index] == number_to_check and not self.marked_positions[row_index][column_index]:
                    return True
        return False

    def mark_number(self, number_to_mark):
        for row_index in range(self.ROWS):
            for column_index in range(self.COLUMNS):
                if self.card_numbers[row_index][column_index] == number_to_mark:
                    self.marked_positions[row_index][column_index] = True

    def is_complete(self):
        for row_index in range(self.ROWS):
            for column_index in range(self.COLUMNS):
                if self.card_numbers[row_index][column_index] != '' and not self.marked_positions[row_index][column_index]:
                    return False
        return True

    def __str__(self):
        card_lines = []
        card_lines.append('-' * 26)
        for row_index in range(self.ROWS):
            line = ''
            for column_index in range(self.COLUMNS):
                value = self.card_numbers[row_index][column_index]
                if value == '':
                    line += '   '
                elif self.marked_positions[row_index][column_index]:
                    line += ' - '
                else:
                    line += f'{value:2d} '
            card_lines.append(line)
        card_lines.append('-' * 26)
        return '\n'.join(card_lines)

class BarrelBag:
    def __init__(self):
        self.barrel_numbers = list(range(1, 91))
        random.shuffle(self.barrel_numbers)

    def draw_barrel(self):
        if self.barrel_numbers:
            return self.barrel_numbers.pop()
        return None

    def barrels_left(self):
        return len(self.barrel_numbers)

class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.card = Card()

    def has_won(self):
        return self.card.is_complete()

class LotoGame:
    def __init__(self):
        self.user_player = Player("Вы")
        self.computer_player = Player("Компьютер")
        self.barrel_bag = BarrelBag()

    def play(self):
        while True:
            current_barrel = self.barrel_bag.draw_barrel()
            if current_barrel is None:
                print("Бочонки закончились! Ничья.")
                break
            print(f"Новый бочонок: {current_barrel} (осталось {self.barrel_bag.barrels_left()})")
            print("------ Ваша карточка -----")
            print(self.user_player.card)
            print("-- Карточка компьютера ---")
            print(self.computer_player.card)
            user_input = input("Зачеркнуть цифру? (y/n): ").strip().lower()
            user_has_number = self.user_player.card.has_number(current_barrel)
            if user_input == 'y':
                if user_has_number:
                    self.user_player.card.mark_number(current_barrel)
                else:
                    print("Числа нет на вашей карточке. Вы проиграли!")
                    return
            elif user_input == 'n':
                if user_has_number:
                    print("Число было на вашей карточке. Вы проиграли!")
                    return
            else:
                print("Некорректный ввод. Попробуйте снова.")
                continue
            if self.computer_player.card.has_number(current_barrel):
                self.computer_player.card.mark_number(current_barrel)
            if self.user_player.has_won():
                print("Вы победили!")
                print(self.user_player.card)
                return
            if self.computer_player.has_won():
                print("Компьютер победил!")
                print(self.computer_player.card)
                return

if __name__ == "__main__":
    LotoGame().play()

