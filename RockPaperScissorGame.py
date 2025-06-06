import random
compList = ["Rock", "Paper", "Scissor"]
inputList = ["1","2","3","q"]

while True:
    try:
        print("Welcome to the Rock Paper Scissor game")
        userChoice = input("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissor\nPress q other key to quit\n")

        if userChoice in inputList:
            pass
        else:
            print("Wrong Input. Retry")
            
        
        compChoice= random.choice(compList)
        
        if userChoice == "q":
            exit()
            
        if userChoice == str(1):
            print("You chose Rock")
            print(f"Comp chose {compChoice}")
            if compChoice == "Rock":
                print("Comp tied")
            elif compChoice == "Paper":
                print("Comp win")
            elif compChoice == "Scissor":
                print("Comp lose")
                
        
        if userChoice == str(2):
            print("You chose Paper")
            print(f"Comp chose {compChoice}")
            if compChoice == "Rock":
                print("Comp lose")
            elif compChoice == "Paper":
                print("Comp tied")
            elif compChoice == "Scissor":
                print("Comp win")
        
        if userChoice == str(3):
            print("You chose Scissor")
            print(f"Comp chose {compChoice}")
            if compChoice == "Rock":
                print("Comp win")
            elif compChoice == "Paper":
                print("Comp lose")
            elif compChoice == "Scissor":
                print("Comp tied")

    except Exception as e:
        print(e)

    finally:
        print("Thank you for playing the game.\n\n")
