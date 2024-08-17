import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine, which will convert speach into text
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)  # This command set the voice type We also can change type of voice according to owr wish.
        
    
# Function for speaking the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen 
def listen():
    with sr.Microphone() as source:
        print("I'm Listening, please say...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand what did you said...")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

# Main loop
while True:
    command = listen()

    if "hello" in command or "hi" in command:
        speak("Hello! How can I assist you today?")
    elif "who are you?" in command:
        speak("I am your voice assistent. And my name is priya")
    elif "how are you?" in command:
        speak("I am so good! what about you?")
    elif "play" in command:
        song = command.replace('play', "")
        speak("Playing.." +song)
        pywhatkit.playonyt(song)
        break
    elif "open Google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
        break
    elif "open Youtube" in command:
        speak("Opening Youtube.")
        webbrowser.open("https://www.youtube.com")
        break
    elif "search Wikipedia for" in command:
        query = command.replace("search Wikipedia for", "").strip()
        speak("Searching Wikipedia for " + query)
        try:
            res = wikipedia.summary(query, sentences=2)
            print(res)
            speak("According to Wikipedia, " + res)
            
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results for this query. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information on Wikipedia for " + query)
        continue;
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M%p')
        speak('Current Time' +time)
        print('Current Time' +time)
    elif "date" in command:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        speak('Todays Date is' +date)
        print(speak('Todays Date is' +date))
    elif "lough" in command:
        speak("HA Ha Ha")
    elif "tell me a joke" in command:
        speak("Sure! Here's one for you: Why don't skeletons fight each other? Because they don't have the guts!")
        print("Sure! Here's one for you: Why don't skeletons fight each other? Because they don't have the guts!")
    elif "goodbye" in command:
        speak("Yeah,Goodbye!")
        print("yeah, Goodbye!")
        break
    else:
        speak("I'm sorry, I do not understand what you have said, can you please repeat...")
        continue
       
