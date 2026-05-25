from plyer import notification
import random

User_wins=0
computer_wins=0
Draw=0
options=["rock", "paper", "scissor"]

while True:
    User_Input=input("Rock /Paper /Scissor or Q to quit: ").lower()
    if User_Input=="q":
        break
    if User_Input not in options:
        print("Enter something valid next time")
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("Computer picked", computer_pick)
    
    if User_Input=="rock" and computer_pick=="scissor":
        print("U Won")
        User_wins+=1
        continue      
    
    elif User_Input=="paper" and computer_pick=="rock":
        print("U Won")
        User_wins+=1
        continue      
    
    elif User_Input=="scissor" and computer_pick=="paper":
        print("U Won")
        User_wins+=1
        continue      
    
    elif User_Input=="rock" and computer_pick=="rock":
        print("DRAW!!")
        Draw+=1
        continue      
    
    elif User_Input=="paper" and computer_pick=="paper":
        print("DRAW!!")
        Draw+=1
        continue      
    
    elif User_Input=="scissor" and computer_pick=="scissor":
        print("DRAW!!")
        Draw+=1
        continue      
    
    else:
        print("U lost")
        computer_wins+=1

print("U won", User_wins, "times.")
print("Computer won", computer_wins, "times.")
print("No of times match tied", Draw)

print("\nDecision pending:")
if  computer_wins>User_wins:
    not_if=("Computer won")
    not_desc=("Better luck next time!")
elif User_wins==computer_wins:
    not_if=("Match Tied")
    not_desc=("Better luck next time")
else:
    not_if=("U won") 
    not_desc=("Well Played")
    
notification.notify(
    title=not_if,
    message=not_desc,
    timeout=5
)