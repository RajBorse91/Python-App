"""
Mini - Assistant : A virtual AI assistant
Libraries Used :
speech_recognition - https://pypi.org/project/SpeechRecognition/
pywhatkit - https://pypi.org/project/pywhatkit/
pyttsx3 - https://pypi.org/project/pyttsx3/
datetime - https://pypi.org/project/DateTime/
wikipedia - https://pypi.org/project/wikipedia/
pyjokes - https://pypi.org/project/pyjokes/
sys - https://docs.python.org/3/library/sys.html
"""
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


def engine_talk(text):
    engine.say(text)
    engine.runAndWait()


def run_alexa():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('\n')
        print("Start Speaking!!")
        engine_talk('listening.. ')
        recordedaudio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(recordedaudio, language='en-in')
            command = command.lower()
            if 'Assistant' in command:
                command = command.replace('Assistant', '')
                print('you said' + command)
            else:
                print('you said : ' + command)

                if 'hello' in command:
                    print('hello how can i helpp you ??')
                    engine_talk('hello, how can i help you ??')

                elif 'who are you' in command:
                    print('I am mini Assistant a k a your virtual assistant master')
                    engine_talk('I am mini Assistant a k a your virtual assistant master. how can i help you ??')

                elif 'can you do' in command:
                    print(
                        '''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,
                        find your location, locate area on map,  open different websites like instagram, youtube,
                        gmail, git hub, stack overflow and searches on google.How may i help you ??''')
                    engine_talk(
                        '''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,
                        find your location, locate area on map,  open different websites like insta gram, youtube,
                        gmail, git hub, stack overflow and searches on google. How may i help you ??''')
                elif 'play' in command:
                    song = command.replace('play', '')
                    print('Playing' + song)
                    engine_talk('Playing' + song)
                    pywhatkit.playonyt(song)
                elif 'date and time' in command:
                    today = date.today()
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    # Textual month, day and year
                    d2 = today.strftime("%B %d, %Y")
                    print("Today's Date is ", d2, 'Current time is', time)
                    engine_talk('Today is : ' + d2)
                    engine_talk('and current time is ' + time)

                elif 'time and date' in command:
                    today = date.today()
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    # Textual month, day and year
                    d2 = today.strftime("%B %d, %Y")
                    print("Today's Date is ", d2, 'Current time is', time)
                    engine_talk('Current time is ' + time)
                    engine_talk('and Today is : ' + d2)


                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print('The current time is' + time)
                    engine_talk('The current time is')
                    engine_talk(time)

                elif 'date' in command:
                    today = date.today()
                    print("Today's date:", today)
                    # Textual month, day and year
                    d2 = today.strftime("%B %d, %Y")
                    print("Today's Date is ", d2)
                    engine_talk('The todays date is')
                    engine_talk(d2)

                elif 'tell me about' in command:
                    name = command.replace('tell me about', '')
                    info = wikipedia.summary(name, 1)
                    print(info)
                    engine_talk(info)

                elif 'wikipedia' in command:
                    name = command.replace('wikipedia', '')
                    info = wikipedia.summary(name, 1)
                    print(info)
                    engine_talk(info)
                elif 'what is' in command:
                    name = command.replace('what is ', '')
                    info = wikipedia.summary(name, 1)
                    print(info)
                    engine_talk(info)

                elif 'who is ' in command:
                    name = command.replace('who is', '')
                    info = wikipedia.summary(name, 1)
                    print(info)
                    engine_talk(info)

                elif 'what is ' in command:
                    search = 'https://www.google.com/search?q=' + command
                    print(' Here is what i found on the internet..')
                    engine_talk('searching... Here is what i found on the internet..')
                    webbrowser.open(search)

                elif 'joke' in command:
                    _joke = pyjokes.get_joke()
                    print(_joke)
                    engine_talk(_joke)

                elif 'search' in command:
                    search = 'https://www.google.com/search?q=' + command
                    engine_talk('searching... ')
                    webbrowser.open(search)

                elif "my location" in command:
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    engine_talk("You must be somewhere near here, as per Google maps")
                elif 'locate ' in command:
                    engine_talk('locating ...')
                    loc = command.replace('locate', '')
                if 'on map' in loc:
                    loc = loc.replace('on map', ' ')
                    url = 'https://google.nl/maps/place/' + loc + '/&amp;'
                    webbrowser.get().open(url)
                    print('Here is the location of ' + loc)
                    engine_talk('Here is the location of ' + loc)

                elif 'on map' in command:
                    engine_talk('locating ...')
                    loc = command.split(" ")
                    print(loc[1])
                    url = 'https://google.nl/maps/place/' + loc[1] + '/&amp;'
                    webbrowser.get().open(url)
                    print('Here is the location of ' + loc[1])
                    engine_talk('Here is the location of ' + loc[1])


                elif 'location of' in command:
                    engine_talk('locating ...')
                    loc = command.replace('find location of', '')
                    url = 'https://google.nl/maps/place/' + loc + '/&amp;'
                    webbrowser.get().open(url)
                    print('Here is the location of ' + loc)
                    engine_talk('Here is the location of ' + loc)


                elif 'where is ' in command:
                    engine_talk('locating ...')
                    loc = command.replace('where is', '')
                    url = 'https://google.nl/maps/place/' + loc + '/&amp;'
                    webbrowser.get().open(url)
                    print('Here is the location of ' + loc)
                    engine_talk('Here is the location of ' + loc)

                elif 'bootcamp' in command:
                    search = 'http://tathastu.twowaits.in/index.html#courses'
                    engine_talk('opening boot camps')
                    webbrowser.open(search)

                elif 'boot camps' in command:
                    search = 'https://www.google.com/search?q=' + 'boot camps'
                    engine_talk('searching... ')
                    webbrowser.open(search)

                elif 'python bootcamp' in command:
                    search = 'https://www.google.com/search?q=' + 'python bootcamp'
                    engine_talk('searching... ')
                    webbrowser.open(search)

                elif 'data science bootcamp' in command:
                    search = 'https://www.google.com/search?q=' + 'data science bootcamp'
                    engine_talk('searching... ')
                    webbrowser.open(search)

                elif 'open google' in command:
                    print('opening google ...')
                    engine_talk('opening google..')
                    webbrowser.open_new('https://www.google.co.in/')

                elif 'gmail' in command:
                    print('opening gmail ...')
                    engine_talk('opening gmail..')
                    webbrowser.open_new('https://mail.google.com/')

                elif 'open youtube' in command:
                    print('opening you tube ...')
                    engine_talk('opening you tube..')
                    webbrowser.open_new('https://www.youtube.com/')

                elif 'open instagram' in command:
                    print('opening instagram ...')
                    engine_talk('opening insta gram...')
                    webbrowser.open_new('https://www.instagram.com/')

                elif 'open stack overflow' in command:
                    print('opening stackoverflow ...')
                    engine_talk('opening stack overflow...')
                    webbrowser.open_new('https://stackoverflow.com/')

                elif 'open github' in command:
                    print('opening git hub ...')
                    engine_talk('opening git hub...')
                    webbrowser.open_new('https://github.com/')

                elif 'bye' in command:
                    print('good bye, have a nice day !!')
                    engine_talk('good bye, have a nice day !!')
                    sys.exit()

                elif 'thank you' in command:
                    print("your welcome")
                    engine_talk('your welcome')

                elif 'stop' in command:
                    print('good bye, have a nice day !!')
                    engine_talk('good bye, have a nice day !!')
                    sys.exit()

                elif 'tata' in command:
                    print('good bye, have a nice day !!')
                    engine_talk('good bye, have a nice day !!')
                    sys.exit()

                elif 'activity graph' in command or 'graph' in command:
                    engine_talk('here is the graph of all the activities')
                    'showgraph()'

                elif 'What you can do' in command or 'your features' in command:
                    engine_talk("Here is the list of my features of EDITH...")
                    engine_talk('I can introduce myself..')
                    engine_talk(
                        "Can take you to some websites like Google, youtube, Facebook, Instagram, Yahoo, amazon, "
                        "flipkart")
                    engine_talk('Also can search your queries on google as well as youtube')
                    engine_talk("Can show you different places on google map")
                    engine_talk('Searching wikipedia')
                    engine_talk('I can tell current time')
                    engine_talk('Open notepad..')
                    engine_talk('Open Teams')
                    engine_talk('Open Calculator')
                    engine_talk('I can tell battery status')
                    engine_talk('Taking screenshot')
                    engine_talk('Play Music')
                    engine_talk('Taking notes')
                    engine_talk('Crack lots of jokes')
                    engine_talk('Change Background')
                    engine_talk('Lock your system')
                    engine_talk('clean recycle bin')
                    engine_talk('Take ScreenShots')
                    engine_talk('Also can Restart your computer')

                else:
                    print(' Here is what i found on the internet..')
                    engine_talk('Here is what i found on the internet..')
                    search = 'https://www.google.com/search?q=' + command
                    webbrowser.open(search)

        except Exception as ex:
            print(ex)

    print('Clearing background noise...Please wait')
    engine_talk('Clearing background noise...Please wait')
    print('\n')
    print("hello, i am mini alexa how can i help you ??")
    engine_talk("hello i am mini Voice Assistant how can i help you ")


while True:
    run_alexa()
