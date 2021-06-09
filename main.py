from utils.game import Hangman

if __name__ == "__main__":
    game = Hangman(possible_words = ['difficult', 'numpy'])
    game.start_game()
