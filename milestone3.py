def check_guess(guess):

    for i in word:
        if i==guess:
            print(f'Good Guess! {guess} is in the word')
            wrong_guess=0
            break
    else:
        wrong_guess=1

    return wrong_guess

def ask_for_input():
    counter=1
    while counter==1:
        guess=input("Enter any letter=")
        print(guess)
        if len(guess)==1 and guess.isdigit()==False and guess!=" " : 
            counter=0
        else : 
            print("Invalid letter. Please, enter a single alphabetical character.")
            counter=1
    wrong_guess=check_guess(guess)
    if wrong_guess==1: print(f'Sorry, {guess} is not in the word. Try again.')
    return wrong_guess

import random

favorite_fruits=["apple","banana","cherry","mango","orange"]
word_list=favorite_fruits
#print(word_list)
word=random.choice(word_list)
print(word)
try_again=1
while try_again==1:
    try_again=ask_for_input()
    
  
