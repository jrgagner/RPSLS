from player import Player

class Human(Player):
    def __init__(self):
        super().__init__(self.set_name())
        pass