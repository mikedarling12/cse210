import random

class Card:

    def __init__(self):
        self.value = 0

    # Create random card value.
    def show_card(self):
        self.value = random.randint(1, 13)
        print(f"The card is {self.value}")
        return self.value