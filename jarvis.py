import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "67300473a41342159d3a704b60db33dc"


def speak(text):
    engine.say(text)                    
    engine.runAndWait()



def aiProcess(command):
    client = OpenAI(
    api_key=" ",  #get key from open ai
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responce please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content   

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif c.lower().startswith ("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]   
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(" ")   #news api key

        data = r.json()

        # Extract all titles into a list
        titles = [article['title'] for article in data['articles']]
        speak("Here are the top news stories of the day:")
        speak(titles)

    else:
        output = aiProcess(c)
        speak(output)



if __name__ == "__main__":
    speak("Initializing Jarvis.........")
    while True:
        r = sr.Recognizer()
       

        print("recognizing.....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source, timeout=2,phrase_time_limit=1)
        
            ward = r.recognize_google(audio)
            if(ward.lower() == "jarvis"):
                speak("Hello Sir")

            with sr.Microphone() as source:
                print("Jarvis Active......")
                audio = r.listen(source)

                command = r.recognize_google(audio) 

                processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

