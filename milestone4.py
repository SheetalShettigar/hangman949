class Hangman:
    
    def __init__(self,word_list=list()):
        self.word_list=word_list
        self.num_lives=5
        self.word_guessed=[]
        self.list_of_guessess=[]

        import random

        self.word=random.choice(self.word_list)
        print(len(self.word))
        print(self.word)
        self.num_letters=len(self.word)
        counter=0
        while counter<len(self.word):
            #print(counter)
            self.word_guessed.append("_")
            counter+=1
        print(self.word_guessed)
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
        check_input_counter=1
        while check_input_counter==1:
            guess=input("Enter any letter=")
            print(guess)
            if len(guess)!=1 or guess.isdigit()==True or guess==" " : 
                print("Invalid letter. Please, enter a single alphabetical character.")
                check_input_counter=1
            elif guess in self.list_of_guessess :
                print("You already tried this letter.")
                check_input_counter=1  
            else : 
                wrong_guess=self.check_guess(guess)
                self.list_of_guessess.append(guess)
                if wrong_guess==1: 
                    self.num_lives-=1
                    print(f'Sorry, {guess} is not in the word. You have {self.num_lives} lives left.')
                    check_input_counter=1
                else: check_input_counter=0
        return wrong_guess

        
    
favorite_fruits=["apple","banana","cherry","mango","orange"]
word_list=favorite_fruits
print(word_list)
Hangman1=Hangman(word_list)
Hangman1.ask_for_input()
print(Hangman1.list_of_guessess)
print(Hangman1.word_guessed)