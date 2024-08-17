print("Hello.")
ask=int(input("\nTo Encode your message type (1)\nTo Decode message type(2)\n"))
if (ask==1):
    user=input("Enter Your message:\n")
    if (len(user)<3):
       u=user[::-1]
       print("Your Coded message is:",u)
    else:
        # print("Your Coded message is:",user[1:]+user[0])
        rback=input("Input ur random 3 characters:")
        rfront=input("Input ur random 3 characters:")
        print("Your Coded message is:",rfront+user[1:]+user[0]+rback)
elif (ask==2):
    user2=input("Enter your Coded message;\n") #abchushkxyz
    if (len(user2)<3):
        u2=user2[::-1]
        print("Here's your Decoded message:",u2)
    else:
        real_m1=user2[3:-3]
        real_m2=real_m1[-1]+real_m1[:-1]
        print(real_m2)
else:
    print("Invalid Input!!. Please give a valid input.")
        
        
