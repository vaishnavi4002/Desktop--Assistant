
import pyttsx3
import datetime
import os
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

try:
    with open("Alarmtext.txt", "r") as extractedtime_file:
        time_str = extractedtime_file.read().strip()

    if not time_str:
        print("No alarm time specified in Alarmtext.txt.")
    else:
        alarm_time = datetime.datetime.strptime(time_str, "%H:%M")

        while True:
            current_time = datetime.datetime.now().time()
            if current_time >= alarm_time.time():
                speak("Alarm ringing, sir")
                os.startfile("ai-integration-173570.mp3")  # You can choose any music or ringtone
                break
            time.sleep(30)  # Check every 30 seconds
            
except FileNotFoundError:
    print("Alarmtext.txt not found.")

except ValueError:
    print("Invalid time format in Alarmtext.txt.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
with open("Alarmtext.txt", "w") as file:
    pass