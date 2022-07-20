from player import Player

class Human(Player):
    def __init__(self):
        super().__init__(self.set_name())
        pass

    def set_name(self):
        return "James"
        
    def pick_gesture(self):
        pick_gesture = input(f"Pick your gesture: {self.gestures[0]},{self.gestures[1]},{self.gestures[2]},{self.gestures[3]}, {self.gestures[4]}")
        if pick_gesture in self.gestures:
            self.pick_gesture = pick_gesture
            print(f"{self.name} chooses {self.pick_gesture}.")
        else:
            self.pick_gesture()
            pass