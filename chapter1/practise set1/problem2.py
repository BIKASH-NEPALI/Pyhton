# install an external module and use it to perform any specific task of your choice.
# here, we will install an external module named pytttsx3
#and it it use to python text to speech conversion.
# pip install pyttsx3 before running this code.
import pyttsx3
engine = pyttsx3.init()
engine.say("twinkle twinkle little star, how i wonder what you are! up above the world so high, like a diamond in the sky")
engine.runAndWait()