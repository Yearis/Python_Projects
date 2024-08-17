import random
#List of Games.
#Snake-Water-Gun Game.
def Snake_Water_Gun_Game():
    Choice_list=["Snake","Water","Gun"]#s>w,w>g,g>s
    a=[1,2,3]
    game_start(Choice_list,a)
#Rock-Paper-Scissors Game.
def Rock_Paper_Scissors_Game():
    Choice_list=["Rock","Scissors","Paper"]#r>s,s>p,p>r
    a=[1,2,3]
    game_start(Choice_list,a)
#Game Processing.
def game_start(Choice_list,a):
    UserScores=0
    CompScores=0 
    try:
        rounds=int(input("Enter the number of rounds you want to play: "))
        if 1 <= rounds <= 9:
            print(f"Pick your Choice:\n1 for {Choice_list[0]}\n2 for {Choice_list[1]}\n3 for {Choice_list[2]}")
            for i in range(rounds):
                #Users Choice.
                uc=int(input("Whats Your Input: ").lower())#UserChoice
                if(uc==1):
                    print(f"So your Choice is {Choice_list[0]}.")
                elif(uc==2):
                    print(f"So your Choice is {Choice_list[1]}.")
                elif(uc==3):
                    print(f"So your Choice is {Choice_list[2]}.")
                else:
                    print("Invalid Choice!!Please choose a Valid Choice.")
                    continue

                #Computers Choice.
                cc=random.choice(a)#Computer_choice
                print(f"Computers Choice is {Choice_list[cc - 1]}") 
                # if(cc==1):                                        
                #     print(f"Computers Choice is {Choice_list[0]}")
                # elif(cc==2):                                      
                #     print(f"Computers Choice is {Choice_list[1]}")
                # elif(cc==3):                                      
                #     print(f"Computers Choice is {Choice_list[2]}")

                #Battle.
                if(uc==cc):
                    print("Its a Draw!!")
                elif(uc==1 and cc==2)or(uc==2 and cc==3)or(uc==3 or cc==1):
                    print("You Win!!!")
                    UserScores+=1
                    CompScores-=1
                elif(uc==2 and cc==1)or(uc==3 and cc==2)or(uc==1 or cc==3):
                    print("You Lose!!!")
                    UserScores-=1
                    CompScores+=1
            #Displaying Final Scores.
            print(f"\nFinal Scores are:\n{nm} -> {UserScores} pts\nComputer-> {CompScores} pts\n")
            #Final Result.
            if (UserScores>CompScores):
                print("The Final Result :\nYou Won!!! Congratulations.")
            elif (UserScores<CompScores):
                print("The Final Result :\nYou Lost!!! Better Luck Next Time.")
            elif (UserScores==CompScores):
                print("The Final Result :\nIts a Tie!!! What a Close Match.")
    except ValueError:
        print("Please Enter a Valid Value for Rounds (1 to 9)")

# Intro and Starting of Game.
nm=input("Please Enter your Name:\n")
print(f"Hello!{nm}, Its Nice to meet you.")
yn=input("Lets Start the Game.\nAre you ready? Yes/No\n").lower()
if (yn=="yes")or(yn=="y"):
    print("Please chose the Game you want to play.")
elif(yn=="no")or(yn=="n"):
    print("Okay have  nice day.")
    exit()
else:
    print("Invalid Input.")
    exit()
#Choosing Game.
Game=input("Snake-Water-Gun ->\nType 'A'\nRock-Paper-Scissors ->\nType 'B'\n").lower()
if (Game=="a"):
    Snake_Water_Gun_Game()
elif(Game=="b"):
    Rock_Paper_Scissors_Game()
else:
    print("Invalid Game Choice!!!")
    exit()
print("Thankyou for Playing with us.")


