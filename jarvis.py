import pyttsx3
import speech_recognition
import datetime
import wikipedia
import webbrowser
import random
import smtplib #simple mail transfer protocol library

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning!")
    elif hour > 12 and hour <= 18:
        speak("good afternoon!")
    elif hour > 18 and hour <= 24:
        speak("good evening!")

speak("I am Jarvis sir, how may I help you?")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.microphone() as source:
        print("Listening...")
        r.pause_threshold = 1;
        audio = r.listen(source)

try:
    print("Recognizing...")
    query = r.recognize_google(audio, language = 'en-in') #using google for voice recognition
    print(f"User said: {query}\n") #user query will be printed.

except exception as e:
    #print(e)
    print("Say that again please...") #say that again will be printed in case of improper voice
    return "None" #none string will be returned

return query

if __name__ == "__main__":
    wishme()

    while True:
        #if 1:

        query = takeCommand(). lower()

    # logic for executing tasks based on query
    if 'wikipedia' in query: #if wikipedia found in the query then this block will be executed
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'play music' in query:
        music_dir = 'C:\Users\Atishay\Music\YMusic'
        YMusic = os.listdir(music_dir)
        print(YMusic)
        os.startfile(os.path.join(music_dir, songs[5]))
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S"))
        speak(f"Sir, the time is {strTime}")
    elif 'open code' in query:
        codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
        os.startfile(codePath)
    def sendEmail(to, content)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, connect)
    server.close()

    elif 'email to atishay' in query:
        try:
            speak("What should I say?")
            content = takecommand()
            to = "atishayyourEmail.com"
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
             speak("sorry my friend atishay. I am not able to send this email")

    






    