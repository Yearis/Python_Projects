import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Hello!!")

Names_List = []

Number_of_Names = int(input("Enter the Number of Names you want to add: "))


for i in range(Number_of_Names):
    Names=input("Enter the Name of the Person you want to give Shoutout: ").strip()
    Names_List.append(Names)


for j in Names_List:
    speaker.Speak(f"ShoutOut to {j}!!!")

speaker.Speak("Thanks For Your Hard Work.")    
