import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk
listening = sr.Recognizer()
engine = pt.init('dummy')

def speak(text):
    engine.say(text)
    engine.runAndWait()
def hear():
    cmd = ""  # Initialize cmd with an empty string
    try:
        with sr.Microphone() as mic:
            print('listening....')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'manoj' in cmd:
                cmd = cmd.replace('manoj', '')
                print(cmd)
    except Exception as e:
        print(f"Error in audio capture: {e}")
    return cmd


def run():
    cmd = hear()
    print(cmd)
    if 'play' in cmd:
        song = cmd.replace('play', '')
        speak('playing' + song)
        pk.playonyt('Playing...' + song)

run()