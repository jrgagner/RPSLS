class Player:
    def __init__(self):
        self.name = ""
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock  "]
        self.picked_gesture = ""
        self.score = 0
        pass

    def set_name(self):
        self.name = input("Enter player name?")
        
    def pick_gesture(self):
        picked_gesture = input(f"Choose your gesture: {self.gestures[0]}, {self.gestures[1]}, {self.gestures[2]}, {self.gestures[3]}, or {self.gestures[4]} ")
        if picked_gesture in self.gestures:
            self.picked_gesture = picked_gesture
            print(f"{self.name} picked {self.picked_gesture}.")
        else:
            self.pick_gesture()