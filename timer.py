import time 

print("Enter Seconds: ")
max_time=int(input())



for i in range(max_time, 0, -1):
    seconds=i % 60
    minutes= int(i/60)%60 
    hour= int(i/3600)
       
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)    
    
print("Times Up!!")
    