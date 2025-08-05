import random
from os import system

words = ['питон', 'программирование', 'виселица', 'алгоритм', 'функция', 
         'переменная', 'список', 'словарь', 'множество', 'итератор']

class Hangman:
    def __init__(self):
        self.word = random.choice(words).upper()
        self.guessed = ['_'] * len(self.word)
        self.used_letters = set()
        self.tries = 6
        self.hangman_states = [
            """
            -----
            |   |
                |
                |
                |
                |
            --------
            """,
            """
            -----
            |   |
            O   |
                |
                |
                |
            --------
            """,
            # ... остальные состояния виселицы ...
        ]
    
    def display(self):
        system('cls' if os.name == 'nt' else 'clear')
        print("Угадай слово по буквам!")
        print(self.hangman_states[6 - self.tries])
        print(' '.join(self.guessed))
        print(f"Осталось попыток: {self.tries}")
        print(f"Использованные буквы: {' '.join(sorted(self.used_letters))}")
    
    def play(self):
        while self.tries > 0 and '_' in self.guessed:
            self.display()
            guess = input("Введите букву: ").upper()
            if len(guess) != 1 or not guess.isalpha():
                print("Пожалуйста, введите одну букву!")
                continue
            
            if guess in self.used_letters:
                print("Вы уже пробовали эту букву!")
                continue
            
            self.used_letters.add(guess)
            
            if guess in self.word:
                for i, letter in enumerate(self.word):
                    if letter == guess:
                        self.guessed[i] = guess
            else:
                self.tries -= 1
        
        self.display()
        if '_' not in self.guessed:
            print("Поздравляем! Вы выиграли!")
        else:
            print(f"Игра окончена! Загаданное слово: {self.word}")

if __name__ == "__main__":
    game = Hangman()
    game.play()
