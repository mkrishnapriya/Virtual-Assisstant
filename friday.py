import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
#mail = {'work':'20071a6630@vnrvjiet.in','daddy':'markapuramramana1972@gmail.com','lohitha':'markapuramlohitha4@gmail.com'}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak('Good Morning!')
    elif hour >= 12 and hour <= 17:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak("Hello!. I'm friday!. How may I help you ?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print('Say that again please...')
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')
        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')
        elif 'open dashboard' in query:
            webbrowser.open('https://cohort3.we.talentsprint.com/login?next=/dashboard#')
        elif 'play music' in query:
            music = 'C:\\Users\\Krishna Priya\\Downloads\\Music'
            songs = os.listdir(music)
            print(songs)
            if 'sakhi' in query:
                os.startfile(os.path.join(music, songs[2]))
            elif 'pal' in query:
                os.startfile(os.path.join(music, songs[1]))
            else:
                os.startfile(os.path.join(music, songs[0]))
        elif 'the time' in query:
            ntime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"It's {ntime} right now")
        '''
        elif 'send email' in query:
            try:
                speak('What should I say?')
                content = take_command()
                speak('To whom?')
                recipent = take_command()
        '''






