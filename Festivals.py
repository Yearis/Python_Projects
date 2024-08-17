from datetime import datetime
month=datetime.now().month
day=datetime.now().day
# print(day,month)
ask=(input("Do you want to know what Festival is Today:"))
if(ask=="yes"):
    if(month==1 and day==1):
        print("Happy New Year!!")
    elif(month==1 and day==13):
        print("Happy Lohri!!")
    elif(month==1 and day==14):
        print("Happy Makar Sankranti!!")
    elif(month==1 and day>=14 and day<=17):
        print("Happy Pongal!!")
    elif(month==1 and day==17):
        print("Happy Guru Govind Singh Jayanti!!")
    elif(month==1 and day==26):
        print("Happy Republic Day!!")
    elif(month==2 and day==14):
        print("Happy Valentines Day !!")
    elif(month==2 and day==14):
        print("Happy Basant Panchami!!")
    elif(month==3 and day==8):
        print("Happy Maha Shiv Ratri!!")
    elif(month==3 and day==8):
        print("Happy Womens Day!!")
    elif(month==3 and day==8):
        print("Happy Mahashiv Ratri!!")
    elif(month==3 and day==24):
        print("Happy Holika Dahan!!")
    elif(month==3 and day==25):
        print("Happy Holi!!")
    elif(month==4 and day==14):
        print("Happy Ambedkar Jayanti!!")
    elif(month==4 and day==17):
        print("Happy Ramnavami!!")
    elif(month==4 and day==21):
        print("Happy Mahavir Jayanti")
    elif(month==5 and day==1):
        print("Happy Workers Day!!")
    elif(month==5 and day==12):
        print("Happy Mothers Day")
    elif(month==6 and day==5):
        print("Happy World Environment Day")
    elif(month==6 and day==16):
        print("Happy Fathers Day!!")
    elif(month==8 and day==15):
        print("Happy Independence Day!!")
    elif(month==8 and day==26):
        print("Happy Janmashtami!!")
    elif(month==9 and day==7):
        print("Happy Ganesh Chaturthi!!")
    elif(month==9 and day==15):
        print("Happy Onam!!")
    elif(month==10 and day==2):
        print("Happy Gandhi Jayanti!!")
    elif(month==10 and day==12):
        print("Happy Dusshera!!")
    elif(month==10 and day==20):
        print("Happy Karwa Chauth!!")
    elif(month==10 and day==31):
        print("Happy Halloween!!")
    elif(month==10 and day==31):
        print("Happy Choti Diwali!!")
    elif(month==11 and day==1):
        print("Happy Diwali!!")
    elif(month==11 and day==2):
        print("Happy Govardhan Puja!!")
    elif(month==11 and day==3):
        print("Happy Bhai Dooj!!")
    elif(month==12 and day==25):
        print("Happy Christmas!!")
    else:
        print("Unfortunately, No Festivals Today ")
else:
    print("Understood, Have a Nice Day!!!")