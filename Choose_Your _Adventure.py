name= input("Type your Name: ")
print("Welcome", name,", To this wonderful adventure!")

print("You are  in the middle of the jungle, after running for several hours and u have come to a dead end. There is a bear after u, so make your moves quick")
print("There is no going back.")
print("you got 3 lives.")

life=3

while True:
    User_Input=input("enter right or left to move. Which way would u like to move? \n: ").lower()    
    
         
    if User_Input=="right":
        
            print("There is an axe ahead would u like to pick it up and fight or ignore")
            User_Input=input("Enter 'fight' to fight or enter 'ignore' \n: ").lower()
            if User_Input==("fight"):
                print(" The Bear was too strong, u died.")
                life-=1
                if life==2:
                    print("2 lives remaining.")
                if life==1:
                    print("1 life remaining.")
                if life==0:
                    print("No lives remaining \n Better luck next Time, Thanks for playing.")
                    quit()
                continue
            elif User_Input=="ignore":
                print("Great! Sometimes ignoring is the key to victory.")
                print("Keep on running the bear is still after u.")
                print("Check point reached")
                
                while True:
                    print("Would u like to call ur friend David and give ur friend a signal.")    
                    User_Input=input("Type 'signal' to give him some signs that u are alive or enter 'ignore' \n: ").lower()
                  
                    if User_Input==("signal"):
                        print("Great! he might be helpful and pull u out of this situation.")
                        print("There is a bridge ahead, Would u like to take the bridge or run instead.")
                        User_Input=input("Type 'bridge' to take the bridge or type 'keep running'.\n :").lower()
                        
                        if User_Input==("bridge"):
                                print("Oops the bridge was broken")
                                print("U fell into the ditch")
                                life-=1
                                if life==2:
                                    print("2 lives remaining.")
                                if life==1:
                                    print("1 life remaining.")
                                if life==0:
                                    print("No lives remaining \n Better luck next Time, Thanks for playing.")
                                    quit()
                                continue
                        elif User_Input==("keep running"):
                                                          
                                    print("Nice you dodged a broken bridge.")
                                    print("David got ur signal, he reaches u.")
                                    print("Ohh",name,"look your car is out there, and i got your keys")
                                    print("Would u like to proceed towards your car.")
                                    print("Enter 'proceed' to get in ur car or press 'leave' to continue running.")
                                    User_Input=input("type 'proceed' to run towards the car and sit or type 'leave' to contine running.\n: ").lower()
                                    if User_Input==("proceed"):
                                        print("You both got out safetly, Wellplayed")
                                        print("Thanks for playing, have a great time.")
                                        quit()
                                    elif User_Input==("leave"):
                                        print("The bear got u both")
                                        life-=1
                                        if life==2:
                                            print("2 lives remaining.")
                                        if life==1:
                                            print("1 life remaining.")
                                        if life==0:
                                            print("No lives remaining \n Better luck next Time, Thanks for playing.")
                                            quit()
                                        continue
                                    else:
                                        print("Enter something valid.")
                        else:
                                print("Enter something valid.")
                    elif User_Input==("ignore"):
                            print("David could have been helpful, however keep running.")   
                            User_Input=input("Type 'bridge' to take the bridge or type 'keep running'.\n :").lower()
                            if User_Input==("bridge"):
                                print("Oops the bridge was broken")                            
                                print("U fell into the ditch")
                                life-=1
                                if life==2:
                                    print("2 lives remaining.")
                                if life==1:
                                    print("1 life remaining.")
                                if life==0:
                                    print("No lives remaining \n Better luck next Time, Thanks for playing.")
                                    quit()
                                continue
                            elif User_Input== ("keep running"):
                                print("nice u dodged a broken bridge.")    
                                print("Ohh great its my car overthere")
                                print("Enter 'proceed' to get in ur car or press 'leave' to continue running.")
                                User_Input=input("type 'proceed' to run towards the car and sit or type 'leave' to contine running.\n: ").lower()
                                if User_Input==("proceed"):
                                    print("Ohh Damn it!! David got my keys.")
                                    print("It was too late the bear got u.")
                                    print("You died.")
                                    life-=1
                                    if life==2:
                                        print("2 lives remaining.")
                                    if life==1:
                                        print("1 life remaining.")
                                    if life==0:
                                        print("No lives remaining \n Better luck next Time, Thanks for playing.")
                                        quit()
                                elif User_Input==("leave"):
                                    print("Ohh i am dehydrated ")
                                    print("Slowing your pace")
                                    print("The bear got u")

                                    life-=1
                                    if life==2:
                                        print("2 lives remaining.")
                                    if life==1:
                                        print("1 life remaining.")
                                    if life==0:
                                        print("No lives remaining Better luck next Time, Thanks for playing.")
                                        quit()
                                    continue
                                else:
                                    print("Enter something valid.")    
                            else:
                                print("Enter something valid.")         
                    else:
                        print("Enter something valid.")
            else:
                print("Enter something valid")
    
    elif User_Input==("left"):   
        while True:
            print("Would u like to buy bear some of his time by laying down some mouse traps")
            User_Input=input(" Type 'yes or 'no.\n:").lower()
            if User_Input==("yes"):
                print("bear got stuck")
                print("great! you got couple of extra minutes.")
                print("Damn it! There is a river ahead.")
                User_Input=input("Would u like to dive in.\nEnter 'yes' or 'no'.\n: ").lower()
                if User_Input==("yes"):
                    print("This was the only way out.")
                    print(f"{name} look a boat is there.")
                    User_Input=input(f"would u like to hop in.\nEnter 'yes' or 'no' to proceed.\n:").lower()
                    if User_Input==("yes"):
                        print(f"great U have reached the end of the isle.")
                        print(f"Well played.")
                        quit()
                        
                    elif User_Input==("no"):
                        print(f'Bear got u in water.')
                        life-=1
                        if life==2:
                            print("2 lives remaining.")
                        if life==1:
                            print("1 life remaining.")
                        if life==0:
                            print("No lives remaining \n Better luck next Time, Thanks for playing.")
                            quit()
                    else:
                        print(f"Enter something valid.")
                elif User_Input==("no"):
                    print("Bear got u")
                    print("Diving in was the only option u got.")
                    life-=1
                    if life==2:
                        print("2 lives remaining.")
                    if life==1:
                        print("1 life remaining.")
                    if life==0:
                        print("No lives remaining \n Better luck next Time, Thanks for playing.")
                        quit()             
                else:
                    print("Enter something valid.")        
            elif User_Input==("no"):
                print ("Not much time left.")
                print ("Make your moves quick and sharply.")
                print("Damn it! There is a river ahead.")
                User_Input=input("Would u like to dive in.\nEnter 'yes' or 'no'.\n: ").lower()
                if User_Input==("yes"):
                    print("This was the only way out.")
                    print(f"{name} look a boat is there.")
                    User_Input=input(f"would u like to hop in.\nEnter 'yes' or 'no' to proceed.\n:").lower()
                    if User_Input==("yes"):
                        print(f"great U have reached the end of the isle.")
                    elif User_Input==("no"):
                        print(f'Bear got u in water.')
                        life-=1
                        if life==2:
                            print("2 lives remaining.")
                        if life==1:
                            print("1 life remaining.")
                        if life==0:
                            print("No lives remaining \n Better luck next Time, Thanks for playing.")
                            quit()
                    else:
                        print(f"Enter something valid.")
                elif User_Input==("no"):
                    print("Bear got u")
                    print("Diving in was the only option u got.")
                    life-=1
                    if life==2:
                        print("2 lives remaining.")
                    if life==1:
                        print("1 life remaining.")
                    if life==0:
                        print("No lives remaining \n Better luck next Time, Thanks for playing.")
                        quit()             
                else:
                    print("Enter something valid.")        
            else:
                print("Enter something valid.")
    else:
       print("Enter Something valid next time.")
        
    