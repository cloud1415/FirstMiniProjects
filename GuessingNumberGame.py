import random
randInt = random.randint(1,10)
print(randInt)
i = 0
while True:
    i += 1 # Attempt counter
    try:
        num = input("Enter guess no. between 1 and 10\nPress q to quit\n")
        
        if num == "q": #Quit code
            break

        num = int(num) #Changing str to int for next code
        
        if num >0 and num <11:
            if num > randInt:
                print("Go lower")
            elif num < randInt:
                print("Go higher")
            else:
                print(f"You guessed it right. It took {i} no of attempts.")
                
        
        else:
            print("Wrong input. Please enter no. between 1 and 10\n")

    except Exception as e:
        print(e)
        
print("Thank you for playing the game")    