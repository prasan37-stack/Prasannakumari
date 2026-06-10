import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
        self.current_winner = None

    def print_board(self):
        print("\n")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print("\n")

    def print_board_nums(self):
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        return False

    def ai_move(self):
        # Simple AI: try to win, block opponent, or take center/corners
        move = self.minimax(self.board, self.ai)['position']
        if move is not None:
            self.make_move(move, self.ai)
            return move

    def minimax(self, board, player, depth=0):
        if player == self.ai:
            best = {'position': None, 'score': -10}
        else:
            best = {'position': None, 'score': 10}

        # Terminal states
        if self.current_winner == self.ai:
            return {'position': None, 'score': 10 - depth}
        elif self.current_winner == self.human:
            return {'position': None, 'score': depth - 10}
        elif not self.empty_squares():
            return {'position': None, 'score': 0}

        for possible_move in self.available_moves():
            self.board[possible_move] = player
            if self.winner(possible_move, player):
                self.current_winner = player

            sim_score = self.minimax(board, self.human if player == self.ai else self.ai, depth + 1)

            self.board[possible_move] = ' '
            self.current_winner = None
            sim_score['position'] = possible_move

            if player == self.ai:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best


def play():
    print("=" * 30)
    print("Welcome to Tic Tac Toe!")
    print("You are X, I am O")
    print("=" * 30)

    game = TicTacToe()

    print("\nBoard positions:")
    game.print_board_nums()

    while game.empty_squares():
        # Human move
        valid_square = False
        while not valid_square:
            square = input("Pick your square (0-8): ")
            try:
                square = int(square)
                if square < 0 or square > 8:
                    print("Invalid square!")
                    continue
                if not game.make_move(square, game.human):
                    print("That square is already taken!")
                    continue
                valid_square = True
            except ValueError:
                print("Please enter a number!")

        if game.current_winner:
            print("\n🎉 You won! Congratulations!")
            game.print_board()
            break

        print("\nYour move:")
        game.print_board()

        if not game.empty_squares():
            print("It's a draw!")
            break

        # AI move
        move = game.ai_move()
        print(f"\nI chose square {move}")

        if game.current_winner:
            print("\n😔 I won! Better luck next time!")
            game.print_board()
            break

        print("\nMy move:")
        game.print_board()

    print("\nThanks for playing!")


if __name__ == "__main__":
    play()
