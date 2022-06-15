from card import Card

class Director:

    def __init__(self):
        self.score = 300
        self.is_playing = True
        self.card = Card()
    
    def start_game(self):
        while self.is_playing:
            card_one = self.card.show_card()
            guess = self.get_input()
            card_two = self.card.show_card()
            self.do_updates(guess, card_one, card_two)
            self.play_again()
    
    def get_input(self):
        guess = input("High or low? [Hi/Lo]: ")
        return guess.capitalize()
    
    def do_updates(self, guess, card_one, card_two):

        # Determine correct answer.
        if card_one > card_two:
            correct_answer = "Hi"
        elif card_one < card_two:
            correct_answer = "Lo"

        # If cards are equal, this will ensure the answer is wrong.
        else:
            correct_answer = "Mid"
        
        # Check if answer was correct.
        if guess == correct_answer:
            print("You guessed correctly!")
            self.score += 100
        else:
            print("You guessed incorrectly.")
            self.score -= 75
        
        # Print out new score.
        print(f"New score: {self.score}")
        
        # Check for no more points
        if self.score <= 0:
            print("Game Over")
            self.is_playing == False

    def play_again(self):

        # If they still have points, give them option to keep playing.
        if self.is_playing:
            again = input("Play again? [y/n] ")
            if again.lower() == "y":
                self.is_playing = True
            else:
                self.is_playing = False
