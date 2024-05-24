import random

favorite_fruits=["apple","banana","cherry","mango","orange"]
word_list=favorite_fruits
print(word_list)
word=random.choice(word_list)
print(word)
counter=1
while counter==1:
    guess=input("Enter any letter=")
    print(guess)
    if len(guess)==1 and guess.isdigit()==False and guess!=" " : 
            print("Good Guess")
            counter=0
    else : 
        print("Oops! That is not a valid input.")
        counter=1
  
