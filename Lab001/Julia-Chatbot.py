#This is an Input/Output AI Chatbot based on Manual Rules

import os
os.system('color 3f') # sets the background to blue

#make Python speak
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

#start the conversation
print('Hi mate!') #greeting
speak.Speak('Hi mate!')

#keep going the conversation
print('Whats your name?') #ask
speak.Speak('Whats your name?')
Name = input() #save answer
print('Im glad to meet you, ' + Name + '!!') #reply
speak.Speak('Im glad to meet you, ' + Name + '!!')
print('The number of letters of your name is:')
speak.Speak('The number of letters of your name is:')
print(len(Name))
speak.Speak(len(Name))

#keep going the conversation
print('How old are you?') #ask
speak.Speak('How old are you?')
Reply = input() #save answer
print('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.') #reply
speak.Speak('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.')

#keep going the conversation 
print('Whats the name of your brother?') #ask
speak.Speak('Whats the name of your brother?')
Reply = input() #save answer
print('Awesome!, my brothers name is also ' + Reply + '!!') #reply
speak.Speak('Awesome!, my brothers name is also ' + Reply + '!!')

#keep going the conversation
print('What is your aunts name?') #ask
speak.Speak('What is your aunts name?')
Reply = input() #save answer
print('Ah ha! I do not have any aunt whose name is ' + Reply) #reply
speak.Speak('Ah ha! I do not have any aunt whose name is ' + Reply)

#keep going the conversation
print('And do you have an aunt named Jeniffer?') #ask
speak.Speak('And do you have an aunt named Jeniffer?')
Reply = input() #save answer
print('Okay, I have 2 aunts whose name is Jeniffer') #reply
speak.Speak('Okay, I have 2 aunts whose name is Jeniffer')

#keep going the conversation
print('By the way, are you enjoying this conversation?') #ask
speak.Speak('By the way, are you enjoying this conversation?')
Reply = input() #save answer
print('Oh nice, me too. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!') #reply
speak.Speak('Oh nice, me too. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!')


#keep going the conversation
print('Can you lend me your new car?') #ask
speak.Speak('Can you lend me your new car?')
Reply = input() #save answer
print('Oh, well, tomorrow Ill pick it up early. Perfect, well talk tomorrow when I come back. Bye ' + Name) #reply
speak.Speak('Oh, well, tomorrow Ill pick it up early. Perfect, well talk tomorrow when I come back. Bye' + Name)



