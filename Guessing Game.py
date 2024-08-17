import random

def Get_Check_UserInput():
    while True:
        try:
            number = int(input("Enter a Number (Between 0 to 100): "))
            if 0 <= number <= 100:
                return number
            else:
                print("Enter a Number Between 0 to 100")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    system_num = random.randint(0, 100)
    global Choice

    if Choice == "M":
        max_tries = 20
    elif Choice == "E":
        max_tries = 30
    elif Choice == "H":
        max_tries = 10
    else:
        print("Invalid Choice")
        return

    tries = 1
    while True:
        user_num = Get_Check_UserInput()
        if system_num > user_num:
            print("Higher Number Please")
            tries += 1
        elif system_num < user_num:
            print("Lower Number Please")
            tries += 1
        else:
            print(f"Congrats!! You guessed the number in {tries} tries.")
            break
        
        if tries > max_tries:
            print(f"Game Over! You've exceeded the maximum number of tries: {max_tries}\nYou Lost the Challenge!!")
            break
        elif tries < max_tries:
            print("You Completed the Challenge!!!")

    Total_tries = f"Total Tries: {tries}"
    print(Total_tries)

def intro():
    global Choice #Make this usable throughout the fns
    print("Hello")
    name = input("What's your Name:\n")
    first_name = name.split()[0]  # Split the input string and take the first part
    print(f"Hello {first_name}")

    ask = input("Are you ready to take the Challenge (Yes or No):\n").lower().strip()
    if ask in ["yes", "y"]:
        Choice = input("""
Choose the Challenge you like:

EASY: Guess the Number in 30 Tries (Press E).
MEDIUM: Guess the Number in 20 Tries (Press M).
HARD: Guess the Number in 10 Tries (Press H).
""").upper().strip()

        if Choice == "M":
            print("So you have chosen MEDIUM Mode")
        elif Choice == "E":
            print("So you have chosen EASY Mode")
        elif Choice == "H":
            print("So you have chosen HARD Mode")
        else:
            print("Invalid choice")
            return
       
    elif ask in ["no",'n']:
        print("Okay have a Nice Day!")
    else:
        raise ValueError("Invalid Response")
    main()

intro()