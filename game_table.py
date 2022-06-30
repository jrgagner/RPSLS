from human import Human
from ai import Ai
import time

class Game_table:
    def __init__(self):
        self.use_ai = True
        self.rounds = int
        self.winner = str
        self.player1 = object
        self.player2 = object

    def run_game_table(self):
        self.display_welcome()
        self.display_rules()
        self.get_mode()
        self.round_count()
        self.start()
        self.display_winner()

    def display_welcome(self):
        print("Welcome to Rock Paper Scissor Lizard Spock!!""\n")
        
    def display_rules(self):
        print("The game RPSLS is simliar to Rock Paper Scissors.")
        time.sleep(2)
        print("However their are five options to select from!""\n")
        time.sleep(2)
        print("The rules are as follows:")
        time.sleep(2)
        print("Best of three wins!""\n")
        time.sleep(2)
        print("Rock crushes Scissors.")
        time.sleep(2)
        print("Scissors cut Paper.")
        time.sleep(2)
        print("Paper covers Rock.")
        time.sleep(2)
        print("Rock crushes Lizard.")
        time.sleep(2)
        print("Lizard poisons Spock.")
        time.sleep(2)
        print("Spock smashes Lizard.")
        time.sleep(2)
        print("Scissors decapitates Lizard.")
        time.sleep(2)
        print("Lizard eats Paper.")
        time.sleep(2)
        print("Paper disproves Spock.")
        time.sleep(2)
        print("Spock vaporizes Rock.")



    

