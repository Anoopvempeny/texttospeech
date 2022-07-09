#pip install pyttsx3
import pyttsx3

engine=pyttsx3.init()


textToSpeech=input("texttospeach")



engine.say(textToSpeech)
engine.runAndWait()