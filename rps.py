import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer (Player):
    def move(self):
        move = random.choice(moves)
        return (move)

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class HumanPlayer (Player):
    def __init__(self):
        self.choice = moves

    def move(self):
        while True:
            userInput = input("Rock, Paper, Scissors, Shoot!\n")
            if userInput.lower() not in moves:
                print("Invalid answer. Please try again.")
            else:
                return userInput


class ReflectPlayer (Player):
    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = their_move


class CyclePlayer (Player):
    def __init__(self):
        self.my_move = None

    def move(self):
        moves = ['rock', 'paper', 'scissors']
        while self.my_move is None:
            return moves[0]
        while self.my_move == moves[0]:
            return moves[1]
        while self.my_move == moves[1]:
            return moves[2]
        while self.my_move == moves[2]:
            return moves[0]

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2) is True:
            self.p1_score += 1
            print("Player 1 wins!")
        else:
            if move1 == move2:
                print("Tie!")
            else:
                self.p2_score += 1
                print("Player 2 wins!")
        print(f"Player One: {self.p1_score}, Player Two: {self.p2_score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in [1, 2, 3, 4, 5, 6, 7, 8]:
            print(f"Round {round}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print("Player One wins!")
        else:
            print("Player Two wins!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
