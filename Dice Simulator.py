import random
import json
print("Hello")

roll_output=[]

name=input("\nWhats your Name?\n")
first_name=name.split()[0]
print(f"Hello {first_name}")

n=int(input("\nEnter the Number of Dices you want:\n"))

roll_cmd=input("\nRoll Dice(Press R)\n").lower()

if roll_cmd=="r":
    for i in range(1,n+1):
        dice_output=random.randint(1, 6)
        roll_output.append(dice_output)
        print(f"The Output Dice {i} is {dice_output}")

    sum_of_die=sum(roll_output)

    if n>1:
        print(f"\nThe Sum of rolls is {sum_of_die}")

else:
    raise ValueError("Invalid Input")
