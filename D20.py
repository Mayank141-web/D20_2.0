import random
while True: 
    d20 = random.randint(1, 20)
    print(d20)
    exit = input("Do you wish to stop rolling? Press '1' for yes and '2' for no: ")
    try:
        exit = int(exit)
        if exit == 1:
            print("Thank you for using this D20!")
            break
        elif exit == 2:
            print("Continuing with the dice roll!")
        else:
            print("Invalid input. Enter '1' to leave and '2' to continue")
    except ValueError:
        print("Invalid input. Please enter a number ('1' or '2').")