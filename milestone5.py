class Hangman:
    
    def __init__(self,word_list=list(),num_lives=5):
        self.word_list=word_list
        self.num_lives=5
        self.word_guessed=[]
        self.list_of_guessess=[]

        import random

        self.word=random.choice(self.word_list)
        self.num_letters=len(self.word)
        counter=0
        while counter<len(self.word):
            self.word_guessed.append("_")
            counter+=1
        return
    
    def check_guess(self,guess):
        guess=guess.lower()
        for guessed_letter in self.word:
            if guessed_letter==guess:
                print(f'Good Guess! {guess} is in the word')
                for i in self.word:
                    if i==guess:
                        index=self.word.index(i)
                        self.word_guessed[index]=guess
                        self.num_letters-=1
                wrong_guess=0
                break
            else:
                wrong_guess=1
        return wrong_guess

    def ask_for_input(self):
        while True: 
            guess=input("Enter any letter=")
            if len(guess)!=1 or guess.isalpha()==False :
                print("Invalid letter. Please, enter a single alphabetical character.")                              
            elif guess in self.list_of_guessess :
                print("You already tried this letter.")
            else :
                wrong_guess=self.check_guess(guess)
                self.list_of_guessess.append(guess)
                if wrong_guess==1: 
                    self.num_lives-=1
                    print(f'Sorry, {guess} is not in the word. You have {self.num_lives} lives left.')
                break                 
        return


def play_game(word_list):
    num_lives=5
    game=Hangman(word_list,num_lives)
    while True:
        if game.num_lives==0:
            print("You Lost")
            break
        if game.num_lives>0 and game.num_letters>0:
            print(game.word_guessed)
            game.ask_for_input()

        if game.num_lives!=0 and game.num_letters==0:
            print(f'Congratulations, You won the game. You guessed the word "{game.word}"')
            break

    return


favorite_fruits=["banana","kiwi","chikoo","mango","orange"]
word_list=favorite_fruits
play_game(word_list)
