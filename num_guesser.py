import random


print("Enter a number to make a top of range")
Top_of_range=input("Type a number: ")

if Top_of_range.isdigit():
    Top_of_range=int(Top_of_range)
    if Top_of_range <=0:
        print ("Enter a number greater than zero")
        quit()
else:
    print("Enter a number")
    quit()
        

print("Your number is in between 0 to", Top_of_range)
random_number=random.randint(0, Top_of_range)
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)   
    else:
        print("please type a number next time.") 
        continue   
    if user_guess ==random_number:
        print ("You got it correct!")
        break
    elif user_guess<random_number:
        print("U were a below the number ") 
    else:
        print("U wre above the number")
        
print("You got it in", guesses, "guesses.")

