import random

class Revolver:
    def __init__(self):
        self.chambers = 6
        self.bullet_position = random.randint(1, 6)
        self.current_position = 0

    def pull_trigger(self):
        self.current_position += 1
        if self.current_position == self.bullet_position:
            return True
        return False

    def reset(self):
        self.bullet_position = random.randint(1, 6)
        self.current_position = 0