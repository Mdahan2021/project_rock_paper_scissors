#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    index_of_current_move = 0
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move


class HumanPlayer(Player):
    def move(self):
        while True:
            choice = input("select your choice among: 'rock,"
                           "'paper', 'scissors'\n").lower()
            if choice in moves:
                break
            else:
                print("Incorrect entry, Please Try again")
        return choice


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        next_move = moves[self.index_of_current_move]
        self.index_of_current_move = (
            self.index_of_current_move + 1) % len(moves)
        return next_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 != move2:
            if beats(move1, move2):
                print("** PLAYER ONE WINS **")
                self.score_p1 += 1
            else:
                print("** PLAYER TWO WINS **")
                self.score_p2 += 1
        else:
            print("** TIES **")
        print(f"PLAYER ONE got {self.score_p1} wins and"
              f" PLAYER TWO got {self.score_p2} wins")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if round == 4:
            if self.score_p1 > self.score_p2:
                print("** Human_Player IS THE WINNER **")
            elif self.score_p1 < self.score_p2:
                print("** Player_Two IS THE WINNER **")
            else:
                print("THE Game IS DRAW")

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round(round)
        print("Game over!")


if __name__ == '__main__':
    strategies = {
        "1": Player(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer()
    }

    user_input = input("Select the Player strategy "
                       "you want to play against\n"
                       "1- Rock Player\n"
                       "2- Random Player\n"
                       "3- Cycle Player\n"
                       "4- Reflect Player\n")

    game = Game(HumanPlayer(), strategies[user_input])
    game.play_game()
