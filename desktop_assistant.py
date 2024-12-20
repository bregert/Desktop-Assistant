import pyttsx3
import speech_recognition as sr
import datetime
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def main():
    greet()
    while True:
        command = listen()
        if 'exit' in command:
            speak("Goodbye!")
            break
        elif 'open notepad' in command:
            os.system('notepad')
        elif 'what time is it' in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}")

if __name__ == "__main__":
    main()