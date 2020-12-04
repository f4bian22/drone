import socket
import time
import threading
from pynput import keyboard

import random
import time
import sys
import os
import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source,duration=0.25)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

# create recognizer and mic instances
recognizer = sr.Recognizer()
microphone = sr.Microphone()
command = recognize_speech_from_mic(recognizer, microphone)
print("You said: {}".format(command["transcription"]))
print("You said: {}".format(command["error"]))

# Turn the Statement into Tello Commands
# set up the response object
Final_Command = {
        "Command" : None,
        "Value" : None
    }

#Open File for Writing Commands
file = open("command.txt","a")

#Final_Command = command["transcription"]
i = 0
tempCom = command["transcription"]
com_list = tempCom.split()

#identifies Command

for word in (com_list):
    if(com_list[i] == "forward"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "back"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "left"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "right"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "up"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "down"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "takeoff"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "land"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "emergency"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "flip"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "speed"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    else:
        print("Incorrect Command")
        i=i+1

#identifies magnitude

i = 0
for word in (com_list):
    if(com_list[i].isdigit()):
        print("Magnitude of Command to be WRITTEN TO FILE")
        file.write(com_list[i])
        break
    else:
        i = i + 1
         
file.write("\n")

os.system('python tello_test.py')

def speech(s):
    recognize_speech_from_mic(recognizer, microphone)



#adres van tello - altijd hetzelfde
tello = ('192.168.10.1', 8889)

#adres van locale pc - altijd hetzelfde
local = ('0.0.0.0',9010)

def init_drone():
 
    # create upd client on PC
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as err:
        print(err)
        exit()
        
   #kopppelen
    s.bind(local)
   
    try:
        # send command om in de juiste modus te zetten
        s.sendto("command".encode(), tello)
        print('command')
        response, ip_address = s.recvfrom(128)
        print(response.decode(encoding='utf-8'))
        
        time.sleep(2)
        
    except socket.error as err:
        print(err)
 
    return s


 
def info(s):

    print('-----------Information------------')
    
    s.sendto("battery?".encode(), tello)
    response, ip_address = s.recvfrom(128)

    print('Battery: ',  response.decode(encoding='utf-8'))

#Snelheid
def snelheid(s):
    s.sendto('speed 80'.encode(), tello)
    

#Stijgen
def takeoff(s):
    s.sendto('takeoff'.encode(), tello)
    time.sleep(10)

#Hoogte
def omhoog(s):
    s.sendto('up 20'.encode(), tello)
    time.sleep(5)

def omlaag(s):
    s.sendto('down 20'.encode(), tello)
    time.sleep(5)

#RichtingBewegen
def links(s):
    s.sendto('left 20'.encode(), tello)
    time.sleep(5)

def rechts(s):
    s.sendto('right 20'.encode(), tello)
    time.sleep(5)

def vooruit(s):
    s.sendto('forward 20'.encode(), tello)
    time.sleep(5)

def achteruit(s):
    s.sendto('back 20'.encode(), tello)
    time.sleep(5)

#RondjeDraaien
def rondjeRechts(s):
    s.sendto('cw 360'.encode(), tello)

def rondjeLinks(s):
    s.sendto('ccw 360'.encode(), tello)

#Salto
def saltoLinksom(s):
    s.sendto('flip l'.encode(), tello)
    time.sleep(3)

def saltoRechtsom(s):
    s.sendto('flip r'.encode(), tello)
    time.sleep(3)

def saltoVooruit(s):
    s.sendto('flip f'.encode(), tello)
    time.sleep(3)

def saltoAchteruit(s):
    s.sendto('flip b'.encode(), tello)
    time.sleep(3)

#StilStaan
    s.sendto('stop'.encode(),tello)
    time.sleep(5)

#Landen
def land(s):
    s.sendto('land'.encode(), tello)
    time.sleep(5)




#invoer
def invoer(s):
    stop = False
    print('send in your command in apostrophes')
    while stop == False:
        I1 = input()
        if I1 == "stop" :
            stop = True

        s.sendto(str(I1).encode(), tello)
        time.sleep(2)
    
def on_press(a):
    release = False
    def on_release(a):
        release = True
    x = 1
    while release == False:
        x += 1
        s.sendto('left x'.encode, tello)
        time.sleep(2)
       
def on_press(w):
    release = False
    def on_release(w):
        release = True
    x = 1
    while release == False:
        x += 1
        s.sendto('up x'.encode, tello)
        time.sleep(2)

def on_press(s):
    release = False
    def on_release(s):
        release = True
    x = 1
    while release == False:
        x += 1
        s.sendto('down x'.encode, tello)
        time.sleep(2)

def on_press(d):
    release = False
    def on_release(d):
        release = True
    x = 1
    while release == False:
        x += 1
        s.sendto('right x'.encode, tello)
        time.sleep(2)
    
def freemove(s):
    on_press(a)




 
def main():
    s = init_drone()

    takeoff(s)
    invoer(s)
    land(s)


 
if __name__ == '__main__':
    main()
   
    
