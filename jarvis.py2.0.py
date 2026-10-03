import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
import os
import subprocess
import ctypes
import sys


# =========================
# JARVIS VOICE ENGINE
# =========================

engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

# Safe/default voice
engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 165)
engine.setProperty("volume", 1.0)


# =========================
# SPEAK FUNCTION
# =========================

def speak(text):
    print("Jarvis:", text)

    engine.say(text)
    engine.runAndWait()


# =========================
# GREETING
# =========================

def wish_me():

    hour = datetime.datetime.now().hour

    if hour < 12:
        greeting = "Good Morning"
    elif hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    speak(f"{greeting} Tanu sir.")
    speak("I am Jarvis. How can I help you?")


# =========================
# LISTEN FUNCTION
# =========================

def take_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

        except sr.WaitTimeoutError:
            print("No voice detected.")
            return ""

    try:

        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-in"
        )

        print("You:", query)

        return query.lower()

    except sr.UnknownValueError:

        print("Could not understand.")

        return ""

    except sr.RequestError:

        speak("Speech recognition service is unavailable.")

        return ""


# =========================
# MAIN COMMAND SYSTEM
# =========================

def execute_command(query):

    # ---------------------
    # TIME
    # ---------------------

    if "time" in query:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"Tanu sir, the time is {current_time}")


    # ---------------------
    # DATE
    # ---------------------

    elif "date" in query:

        today = datetime.datetime.now().strftime("%d %B %Y")

        speak(f"Today is {today}")


    # ---------------------
    # GOOGLE
    # ---------------------

    elif "open google" in query:

        speak("Opening Google.")

        webbrowser.open("https://www.google.com")


    # ---------------------
    # YOUTUBE
    # ---------------------

    elif "open youtube" in query:

        speak("Opening YouTube.")

        webbrowser.open("https://www.youtube.com")


    # ---------------------
    # PLAY SONG
    # ---------------------

    elif "play" in query:

        song = query.replace("play", "").strip()

        if song:

            speak(f"Playing {song}")

            pywhatkit.playonyt(song)

        else:

            speak("Please tell me the song name.")


    # ---------------------
    # WIKIPEDIA
    # ---------------------

    elif "wikipedia" in query:

        topic = query.replace(
            "wikipedia",
            ""
        ).strip()

        if topic:

            speak(f"Searching Wikipedia for {topic}")

            try:

                result = wikipedia.summary(
                    topic,
                    sentences=2
                )

                speak(result)

            except Exception:

                speak("Sorry, I could not find that information.")

        else:

            speak("Please tell me what to search.")


    # ---------------------
    # JOKE
    # ---------------------

    elif "joke" in query:

        speak(pyjokes.get_joke())


    # ---------------------
    # NOTEPAD
    # ---------------------

    elif "open notepad" in query:

        speak("Opening Notepad.")

        subprocess.Popen("notepad.exe")


    # ---------------------
    # CALCULATOR
    # ---------------------

    elif "open calculator" in query:

        speak("Opening Calculator.")

        subprocess.Popen("calc.exe")


    # ---------------------
    # FILE EXPLORER
    # ---------------------

    elif "open file explorer" in query:

        speak("Opening File Explorer.")

        subprocess.Popen("explorer.exe")


    # ---------------------
    # VS CODE
    # ---------------------

    elif "open vs code" in query:

        speak("Opening Visual Studio Code.")

        os.system("code")


    # ---------------------
    # GOOGLE SEARCH
    # ---------------------

    elif "search" in query:

        search_query = query.replace(
            "search",
            ""
        ).strip()

        if search_query:

            speak(f"Searching for {search_query}")

            webbrowser.open(
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )


    # ---------------------
    # LOCK PC
    # ---------------------

    elif "lock computer" in query or "lock pc" in query:

        speak("Locking your computer.")

        ctypes.windll.user32.LockWorkStation()


    # ---------------------
    # SHUTDOWN
    # ---------------------

    elif "shutdown computer" in query:

        speak("Shutting down the computer.")

        os.system("shutdown /s /t 10")


    # ---------------------
    # RESTART
    # ---------------------

    elif "restart computer" in query:

        speak("Restarting the computer.")

        os.system("shutdown /r /t 10")


    # ---------------------
    # CANCEL SHUTDOWN
    # ---------------------

    elif "cancel shutdown" in query:

        os.system("shutdown /a")

        speak("Shutdown cancelled.")


    # ---------------------
    # EXIT
    # ---------------------

    elif (
        "exit" in query
        or "quit" in query
        or "stop jarvis" in query
        or "goodbye" in query
    ):

        speak("Goodbye Tanu sir. Have a nice day.")

        sys.exit()


    # ---------------------
    # UNKNOWN COMMAND
    # ---------------------

    else:

        speak(
            "I understood your command, "
            "but this feature is not added yet."
        )


# =========================
# START JARVIS
# =========================

if __name__ == "__main__":

    wish_me()

    while True:

        query = take_command()

        if query:

            execute_command(query)