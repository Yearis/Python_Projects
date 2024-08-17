from datetime import datetime
# to get current time from system
Gender=input("What's your Gender: ").lower().strip()
if Gender=="male"or Gender=="m":
    gender="Sir"
elif Gender=="female"or Gender=="f":
    gender="Ma'am"
else:
    ValueError("Provide correct Gender.")
now =datetime.now().time()
# to extract hour and minute from current time
timestamp=now.strftime('%H:%M')
time_int=timestamp.replace(":",".")
# print(time_int)
time=float(time_int)
# print(time)
if(time<12.00):
    print(f"Good Morning {gender}")
elif(time>=12.00):
    if(time<17.00):
        print(f"Good Afternoon {gender}")
    elif(time>=17.00 and time<23.30 ):
        print(f"Good Evening {gender}")
else:
    print(f"Good Night {gender}")

