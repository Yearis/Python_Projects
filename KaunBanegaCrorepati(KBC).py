# def options(a,b,c,d):
#     optionsforans=f"(a) {a}        (b) {b}\n(c) {c}      (d) {d}"
#     print(optionsforans)

#     ans=(input("What's your final answer:"))
#     return ans

# def anschecking(a,b):
#     if a in b:
#         print("Congratulations!!,Its the Correct Answer.")
        
#     else:
#         print("Buzz!!,Wrong Answer")                
#         return 0
# question1="What is the Capital of Australia"
# print(question1)
# a="Sydney"
# b="Melbourne"
# c="Canberra"
# d="Perth"
# cans=options(a,b,c,d)

# correctans=["(c)","Canberra","(c)","(C)","c","C","Canberra","canberra"]

# anschecking(cans,correctans)

# question2="What is the capital of France?"
# print(question2)
# a="Paris"
# b="Rome"
# c="Berlin"
# d="London"
# cans=options(a,b,c,d)

# correctans2=["(a)", "Paris", "(a)", "(A)", "a", "A", "Paris", "paris"]
            
# anschecking(cans,correctans2) 

###KBC Start
name=input("Whats your Name?\n")
print("\nGood to have you",name,"Welcome!!")
yn=input("\nAre You Ready.\nAnswer in yes or no:\n")
if(yn.lower()=="yes"):
    print("\nThen here's your 1st Question")
else:
    print("It was good to meet you.Have a Nice Day")
pts=[1000,1000]
# Question 1
print("\nWhat is the Capital of Australia?")
a = "Sydney"
b = "Melbourne"
c = "Canberra"
d = "Perth"
optionsforans = f"(a) {a}        (b) {b}\n(c) {c}      (d) {d}"
print(optionsforans)

ans = input("What's your final answer: ")

correctans = ["(c)", "Canberra", "(c)", "(C)", "c", "C", "Canberra", "canberra"]

if ans in correctans:
    print("Congratulations!!. It's the Correct Answer.\nYour Total Points now are:",pts[0])
else:
    print("Wrong Answer: You Lose!!")
    quit()
# Question 2
print("\nWhat is the capital of France?")
a = "Paris"
b = "Rome"
c = "Berlin"
d = "London"
optionsforans = f"(a) {a}        (b) {b}\n(c) {c}      (d) {d}"
print(optionsforans)

ans = input("What's your final answer: ")

correctans2 = ["(a)", "Paris", "(a)", "(A)", "a", "A", "Paris", "paris"]

if ans in correctans2:
    print("Congratulations!!. It's the Correct Answer.Your Total points now are:",pts[0]+pts[1])
    print("\nThankyou for Playing with us. We will be back with more Questions Soon.\nTill then Goodbye!")
    exit()
else:
    print("Buzz!!, Wrong Answer.Your total points now are:",pts[0])
    print("\Try again!!")