from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
        pass

    def set_name(self):
        self.name =  "Johnny 5"
        pass

    def pick_gesture(self):
        print(f"Pick your gesture: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, {self.gestures[4]}")
        self.picked_gesture = random.choice(self.gestures)
        print(f"{self.name} picks {self.picked_gesture}.")
        pass


