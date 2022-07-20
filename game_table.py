from human import Human
from ai import Ai
import time

class Game_table:
    def __init__(self):
        self.player1 = Human("James")
        self.player2 = None
        pass

    def run_game_table(self):
        self.display_welcome()
        self.display_rules()
        self.game_type()
        self.round()
        self.display_winner()
        pass

    def display_welcome(self):
        print("Welcome to Rock Paper Scissor Lizard Spock!!""\n")
        pass

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
        pass

    def game_type(self):
            game_type = int(input("Please select a game mode:\n(1) Player vs. Player\n(2) Player vs AI\n"))
            
            if game_type == 1:
                self.player2 = Human(self)
                self.player1.set_name()
                time.sleep(0.5)
                print(f"Hello {self.player1.name}.")
                self.player2.set_name()
                time.sleep(0.5)
                print(f"Hello {self.player2.name}.")
                time.sleep(0.5)
                print()
                time.sleep(0.5)
                print(f"{self.player1.name} vs {self.player2.name}")
                return
            elif game_type == 2:
                self.player2 = Ai(self)
                self.player1.set_name()
                time.sleep(0.5)
                print(f"Hello {self.player1.name}.")
                time.sleep(0.5)
                self.player2.set_name()
                time.sleep(0.5)
                print(f"Hello {self.player2.name}.")
                time.sleep(0.5)
                print()
                time.sleep(0.5)
                print(f"{self.player1.name} vs {self.player2.name}")
                return
            

    def round(self):
            while self.player1.score < 2 and self.player2.score < 2:

                print("\nNew Round:\n")

                self.player1.pick_gesture()
                self.player2.pick_gesture()

            if self.player1.pick_gesture == self.player2.pick_gesture:
                print("Round is a tie.")
                
            elif self.player1.pick_gesture == self.player1.gestures[0] and self.player2.pick_gesture == self.player2.gestures[2]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[0] and self.player2.pick_gesture == self.player2.gestures[3]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[1] and self.player2.pick_gesture == self.player2.gestures[0]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[1] and self.player2.pick_gesture == self.player2.gestures[4]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[2] and self.player2.pick_gesture == self.player2.gestures[1]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[2] and self.player2.pick_gesture == self.player2.gestures[3]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[3] and self.player2.pick_gesture == self.player2.gestures[1]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[3] and self.player2.pick_gesture == self.player2.gestures[4]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[4] and self.player2.pick_gesture == self.player2.gestures[0]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            elif self.player1.pick_gesture == self.player1.gestures[4] and self.player2.pick_gesture == self.player2.gestures[2]:
                print(f"{self.player1.name} wins the round.")
                self.player1.score += 1
                
            else:
                print(f"{self.player2.name}) wins the round.")
                self.player2.score += 1
            
            print(f"Scoreboard:\n{self.player1.name}: {self.player1.score}.\n{self.player2.name}: {self.player2.score}")
            pass

    def display_winner(self):
            if self.player1.score >= 2:
                print(f"\n{self.player1.name} wins the match!")
            if self.player2.score >= 2:
                print(f"\n{self.player2.name} wins the match!")
                pass

    

