from human import Human
from ai import Ai
import time

class Game_table:
    def __init__(self):
        # self.use_ai = True
        # self.rounds = int
        # self.winner = str
        self.player1 = None
        self.player2 = None

    def run_game_table(self):
        self.display_welcome()
        self.display_rules()
        self.round()
        # self.start()
        # self.display_winner()

    def display_welcome(self):
        print("Welcome to Rock Paper Scissor Lizard Spock!!""\n")
        
    def display_rules(self):
        print("The game RPSLS is simliar to Rock Paper Scissors.")
        time.sleep(0.5)
        print("However their are five options to select from!""\n")
        time.sleep(0.5)
        print("The rules are as follows:")
        time.sleep(0.5)
        print("Best of three wins!""\n")
        time.sleep(0.5)
        print("Rock crushes Scissors.")
        time.sleep(0.5)
        print("Scissors cut Paper.")
        time.sleep(0.5)
        print("Paper covers Rock.")
        time.sleep(0.5)
        print("Rock crushes Lizard.")
        time.sleep(0.5)
        print("Lizard poisons Spock.")
        time.sleep(0.5)
        print("Spock smashes Lizard.")
        time.sleep(0.5)
        print("Scissors decapitates Lizard.")
        time.sleep(0.5)
        print("Lizard eats Paper.")
        time.sleep(0.5)
        print("Paper disproves Spock.")
        time.sleep(0.5)
        print("Spock vaporizes Rock.""\n")
        

    def mode(self):
        game_type = int(input("Please select a game mode:\n(1) Player vs. Player\n(2) Player vs AI\n"))
        if game_type == 1:
            self.player1 = Human("Steve")
            print(f"Hello {self.player1.name}.")
            self.player2 = Human("John")
            print(f"Hello {self.player2.name}.")
            print()
            print(f"{self.player1.name} vs {self.player2.name}")
        elif game_type == 2:
            self.player1 = Human("Steve")
            print(f"Hello {self.player1.name}.")
            self.player2 = Ai("Fred")
            print(f"Hello {self.player2.name}.")
            print()
            print(f"{self.player1.name} vs {self.player2.name}")

    def round(self):


        




    

