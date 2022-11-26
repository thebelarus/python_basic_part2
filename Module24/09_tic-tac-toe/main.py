class Cell:
    def __init__(self, number, selected=False):
        self.selected = selected
        self.number = number

    def __str__(self) -> str:
        if not self.selected:
            return f'{self.number} *'
        return f'{self.number} {self.selected}'

    def __eq__(self, anothe_cell):
        return (self.selected == anothe_cell.selected
                and self.selected is not False)

    def is_empty(self):
        if not self.selected:
            return True
        return False


class Board:
    def __init__(self):
        self.deck = [Cell(number) for number in range(9)]

    def __getitem__(self, key):
        return self.deck[key]

    def __len__(self):
        return len(self.deck)

    def print_board_to_console(self):
        for i in range(3):
            print(
                (
                    f'{self.deck[0+i*3]} | '
                    f'{self.deck[1+i*3]} | '
                    f'{self.deck[2+i*3]} '
                )
            )

    def is_completed(self):
        for i in range(3):
            if self.deck[0+i*3] == self.deck[1+i*3] == self.deck[2+i*3]:
                return True, self.deck[0+i*3].selected
        for i in range(3):
            if self.deck[0+i] == self.deck[3+i] == self.deck[6+i]:
                return True, self.deck[0+i].selected
        if self.deck[0] == self.deck[4] == self.deck[8]:
            return True, self.deck[0].selected
        if self.deck[2] == self.deck[4] == self.deck[6]:
            return True, self.deck[2].selected
        return False


class Player:
    def __init__(self, name, symbol, board):
        self.name = name
        self.symbol = symbol
        self.board = board

    def fill_cell(self, index):
        if 0 <= index <= len(self.board) and self.board[index].is_empty():
            self.board[index].selected = self.symbol
            return True
        return False


def main():
    board = Board()
    player_1 = Player('Jonh', 'X', board)
    player_2 = Player('Mick', 'O', board)
    players = (player_1, player_2)
    while not board.is_completed():
        for player in players:
            board.print_board_to_console()
            while True:
                player_choise = input((
                    f'{player.name}, вы играете '
                    f'{player.symbol}, выберите ячейку: '))
                if not player_choise.isnumeric():
                    print('Адресс ячейки положительное целое число')
                    continue
                choice_result = player.fill_cell(int(player_choise))
                if choice_result:
                    break
                print('Неправильный адресс ячейки или ячейка уже занята!')
            if board.is_completed():
                board.print_board_to_console()
                print(f'{player.name} is winner!')
                break


if __name__ == '__main__':
    main()
