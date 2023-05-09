import pyttsx3
import speech_recognition as sr
import random

iorona = pyttsx3.init('sapi5')
voices = iorona.getProperty('voices')
iorona.setProperty('voice', voices[1].id)

def speak(audio):
    iorona.say(audio)
    iorona.runAndWait()
    
def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Let's play the game. Stone, Scissor, Paper")
        speak("I am Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("Recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User Said {query}")
    except Exception as e:
        speak("Sorry Sir i did not hear you, can you say that again")
        return "None"
    return query


if __name__ == "__main__":
	print(" \t\t\t\t STONE SCISSOR PAPER GAME")
	speak("This is a Stone Scissor Paper Game")
	speak("You have to choose either stone, scissor or paper")
	us = 0 #us = user_score
	cs = 0 #cs = computer_score

	char = ["stone", "scissor", "paper"]
	while True:
		query = Command().lower()
		comp = random.choice(char)

		if "stone" in query and "paper" in comp:
			speak("Computer win")
			cs+=1
		elif "stone" in query and "scissor" in comp:
			speak("User win")
			us+=1
		elif "stone" in query and "stone" in comp:
			speak("Match tie")
		elif "paper" in query and "scissor" in comp:
			speak("Computer win")
			cs+=1
		elif "paper" in query and "stone" in comp:
			speak("User win")
			us+=1
		elif "paper" in query and "paper" in comp:
			speak("Match tie")
		elif "scissor" in query and "stone" in comp:
			speak("Computer win")
			cs+=1
		elif "scissor" in query and "paper" in comp:
			speak("User win")
			us+=1
		elif "scissor" in query and "scissor" in comp:
			speak("Match tie")
		elif "exit" in query or "quit" in query:
			break
		else:
			speak("Please input stone or scissor or paper")

	speak(f"User total score is:{us} ")
	speak(f"Computer total score is: {cs}")
	if us > cs:
		speak("Finally User win")
	elif us == cs:
		speak("Match Tie")
	else:
		speak("Finally Computer win")