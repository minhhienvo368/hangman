import random
from typing import List, Union
#import re

class Hangman:

    a_blank_char = '_'
    list_of_default_words = ["becode", "learning", "mathematics", "sessions"]

    def __init__(self, possible_words: List[str]):
        self.possible_words: List[str] = self.extensive_default_word(possible_words)
        self.word_to_find: List[str] = self.select_word_to_find()
        self.lives: int = 5
        self.correctly_guessed_letters = [self.a_blank_char for index in range(len(self.word_to_find))]
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.good_answers_count: int = 0

    def start_game(self) -> None:
        # Let's start the game here
        while True:
            self.play()
            self.turn_count += 1

            self._display_info()
            if self.user_won():
                self.well_played()
            elif self.user_lost():
                self.game_over()

    def play(self) -> Union[None, str]:
        get_a_letter = input('Enter a letter to guess: ')
        if get_a_letter.isalpha() and len(get_a_letter) == 1:
            indices = [i for i, x in enumerate(self.word_to_find) if x == get_a_letter]
            if indices:
                for index in indices:
                    self.correctly_guessed_letters[index] = get_a_letter
            else:
                self.wrongly_guessed_letters.append(get_a_letter)
                self.error_count += 1
                self.lives -= 1
        else:
            print('Please enter a single letter')

    def _display_info(self) -> None:
        word = "".join(self.correctly_guessed_letters)
        print(f"[{self.turn_count}] The word to guess: {word}")
        print(f"Wrong guesses: {self.wrongly_guessed_letters}")
        print(f"You have: {self.lives} turn left")

    def user_won(self) -> bool:
        return self.correctly_guessed_letters.count(self.a_blank_char) == 0

    def user_lost(self) -> bool:
        return self.lives == 0

    def well_played(self) -> None:  #Exit the game when user has got the word
        word = "".join(self.word_to_find)
        print(
            f"Weldone! You found the word: {word} , in {self.turn_count} turns with {self.error_count} errors!"
        )
        exit(0)

    def game_over(self) -> None:     #Exit the game when user is out of turn
        print('Game over... you do not have any turn to play')
        exit(1)

    def select_word_to_find(self) -> List[str]:
        # This function allow to pick a random word from list_of_default_word
        # and return a list of letter within selected word
        pick_a_word = random.choice(self.possible_words)
        return [letter for letter in pick_a_word]

    def extensive_default_word(self, possible_words: List[str]) -> List[str]:
        extension_words_list = possible_words.copy()
        for word in self.list_of_default_words:
            if word not in possible_words:
                extension_words_list.append(word)
        return extension_words_list
