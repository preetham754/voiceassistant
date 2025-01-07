import speech_recognition as sr
import pyttsx3

def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to the user's voice and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
        except sr.RequestError:
            speak("Network error. Please check your connection.")
        except sr.WaitTimeoutError:
            speak("You didn't say anything.")
        return ""

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif "your name" in command:
            speak("I am your personal assistant.")
        elif "time" in command:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}.")
        elif "weather" in command:
            speak("Sorry, I cannot fetch the weather right now.")
        else:
            speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
