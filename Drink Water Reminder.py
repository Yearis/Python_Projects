import winsound
import time
import win32com.client
from datetime import datetime,timedelta

speaker=win32com.client.Dispatch("SAPI.SpVoice")
msg="Drink 1 Glass of Water"

def alarm(end_time):
    stop_time=datetime.strptime(end_time,"%H:%M:%S").time()#time()just takes the time part and ignores rest
    # it checks the end_time with the current time(%H:%M:%S)

    while True:
        now=datetime.now().time()
        
        if now <= stop_time:
            winsound.Beep(500,500)
            speaker.Speak(msg)
        else:
            break
    time.sleep(3600)

alarm(end_time="23:00:00")

        