print("Welcome To Quiz Game")

playing = input("Do you want to play: ")
score=0


while playing != "yes" or "no":
    if playing.lower() =="yes":
        print("Lets get started")
        break
    elif playing.lower()=="no":
        print("are you sure you want to quit")
        playing=input(" ")
        
        if playing=="no":
             print("Then lets get started")
             break
        else:
            quit()
    else:
        print("Enter 'YES or 'NO' next time.")
        quit()



answer=input("What does CPU stands for: ")
if answer.lower()=="central processing unit":
    print("Correct :)")
    score+=1
else:
    print("Incorrect")

answer=input("What does ROM stands for: ")
if answer.lower()=="read only memory":
    print("Correct :)")
    score+=1
else:
    print("Incorrect")

answer=input("What does IT stands for: ")
if answer.lower()=="information technology":
    print("Correct :)")
    score+=1
else:
    print("Incorrect")

    
answer=input("What does LAN stands for: ")
if answer.lower()=="local area network":
    print("Correct :)")
    score+=1
else:
    print("Incorrect")

answer=input("Name of our last prophet?\n Prophet  ")
if answer.title()=="Muhaamad":
    print("Correct :)")
    score+=1
elif answer.title()=="Muhammad Pbuh":
    print("Correct")
    score+=1
else:
    print("Incorrect")

answer=input("Bonus Question:\nCube root of 3?:\n ")
if answer=="27":
    print("Correct :)")
else:
     print("Incorrect")
    

print("You got", score, "questions correct")
print("Result", str((score/5)*100)+"%")
