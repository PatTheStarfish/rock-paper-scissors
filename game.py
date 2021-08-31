import random


class Game:

    def __init__(self):
        self.score = 0
        self.choices = None

    def make_game(self):
        user = input("Enter your name: ")
        print("Hello,", user)
        f = open("rating.txt", "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            if user in line.split()[0]:
                self.score = int(line.split()[1])
        self.choices = input()
        if self.choices == "":
            self.choices = ["rock", "paper", "scissors"]
        else:
            self.choices = self.choices.split(",")
        print("Okay, let's start")

    def game_loop(self):
        while True:
            computer_choice = random.choice(self.choices)
            user_choice = input()
            if user_choice in self.choices:
                idx = self.choices.index(user_choice)
                winners = self.choices[idx + 1:] + self.choices[:idx]
                losers = winners[len(winners) // 2:]
                winners = winners[:len(winners) // 2]
                if user_choice == computer_choice:
                    print(f"There is a draw ({computer_choice})")
                    self.score += 50
                elif computer_choice in winners:
                    print(f"Sorry, but the computer chose {computer_choice}")
                elif computer_choice in losers:
                    print(f"Well done. The computer chose {computer_choice} and failed")
                    self.score += 100
            elif user_choice == "!exit":
                print("Bye!")
                break
            elif user_choice == "!rating":
                print("Your rating:", self.score)
            else:
                print("Invalid input")


game = Game()

game.make_game()
game.game_loop()
