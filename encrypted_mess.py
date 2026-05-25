import random , string, time

chars= " " + string.ascii_letters + string.digits + string.punctuation

chars = list(chars)
key = chars.copy()

def encryption():
    
    random.shuffle(key)

    encrypted = ""
    decrypted = ""
    
    # Encryption
    Txt=str(input(f"Enter a text to encrypt: "))
    
    for i in Txt:
        index=chars.index(i)
        encrypted += key[index]
        
    print(f"Your message is being incrypted in: ")
    for z in range(3,0,-1):
        print(z)
        time.sleep(1)
        
    print(f"Encrypted Text: {encrypted}")
    
    #Decryption    
    decrypted_txt = str(input("Enter the key to Decrypt your Text: "))
        
    for x in decrypted_txt:
        index2=key.index(x)
        decrypted += chars[index2]

    print(f"Your message is being decrypted in: ")
    for y in range(3,0,-1):
        print(y)
        time.sleep(1)
        
    if decrypted == Txt:
        print(f"Your message is decrypted: {decrypted}")
                
    else:
        print(f"You entered a wrong key")
                   
if __name__ == "__main__":
    encryption()
    