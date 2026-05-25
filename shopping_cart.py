foods ={
    "shawarma"  : 12.45,
    "pizza"     : 15.00,
    "burger"    : 20.00,
    "pasta"     : 25.39,
    "sandwich"  : 5.59    
}

Cart=[]
Total = 0

print("---------- Welcome ----------")
for food,price in foods.items():
    print(f"{food:10} :   ${price}")

while True:
    print(f"Enter food or q to quit: ")
    choice=str(input().lower())    
    if choice=='q':
        break
    elif choice in foods.keys():
        Cart.append(choice)
        Total+=foods[choice]
    else:
        print(f"{choice} is not available.")
        
print(f"Thanks for purchasing. Your total bill is ${Total}")
        