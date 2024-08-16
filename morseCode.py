import time
import fileinput
from pysinewave import SineWave
import tkinter

# Create a sine wave, with a starting pitch of 7 (note G).
dotPerSecond = 20
dotSpeed = 1/dotPerSecond
volume = 10
sinewave = SineWave(pitch = 7, pitch_per_second = 10, decibels_per_second = 15)
sinewave.set_volume(volume)
#used to adjust speed



# Dictionary representing the morse code chart
morseDict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
#input: string. output: string converted into morse code
def encrypt(message):
    cipher = ''
    #dict only has upper case letters, so make message uppercase
    message = message.upper()

    for letter in message:
        if letter != ' ':
            #finds morse code associated with letter and adds space to have division per character
            try:
                cipher += morseDict[letter] + ' '
            except:
                pass
        else:
            #adds additional 2 spaces if it's a word, totalling 3 spaces between words
            cipher += '  '
    
    print("morse: %s" % (cipher))
    return cipher

#takes morse code and plays each dot and dash
def playMorse(message):
    for letter in message:
        #finds what to play
        if letter == '.':
            # sinewave.play()
            # sinewave.set_volume(volume)
            # time.sleep(dotSpeed)
            # sinewave.set_volume(volume * 0.8)
            # sinewave.stop()
            # time.sleep(dotSpeed)
            sinewave.set_volume(0.5)
            sinewave.play()
            sinewave.set_volume(8)
            time.sleep(dotSpeed/2)
            sinewave.set_volume(0.5)
            time.sleep(dotSpeed/2)
            sinewave.stop()
            time.sleep(dotSpeed)
        elif letter == '-':
            # sinewave.play()
            # time.sleep(dotSpeed * 3)
            # sinewave.stop()
            # time.sleep(dotSpeed)
            sinewave.set_volume(0.5)
            sinewave.play()
            sinewave.set_volume(8)
            time.sleep(dotSpeed)
            sinewave.set_volume(0.5)
            time.sleep(dotSpeed*2)
            sinewave.stop()
            time.sleep(dotSpeed)
        else:
            time.sleep(dotSpeed * 2)

#takes user input and plays it in morse
def userMorse():
    message = input("Enter a message: ")
    message = encrypt(message)
    playMorse(message)
    return message

def fileConverter():
    txt = ''
    #read file content
    with open('./ogMessage.txt') as file:
        txt = file.read()
    #remove any indents
    txt = txt.replace('\n', ' ')
    print("file contents: %s" % (txt))
    txt = encrypt(txt)
    playMorse(txt)
    return txt

def fileWrite(message):
    with open('./morseMessage.txt', 'w') as file:
        file.write(message)

if __name__ == '__main__':
    morse = ''
    #which variation of converter you want: terminal user input or file
    option = input("Choose 1 for user input and 2 for file read: \n")
    option = int(option)
    while(not(option == 1 or option == 2)):
        option = input("Option invalid, select 1 for user input and 2 for file read: \n")
        option = int(option)

    if(option == 1):
        print("Doing user input")
        morse = userMorse()
    elif (option == 2):
        print("Reading file")
        morse = fileConverter()

    option = input("Do you want to write onto a file? Y or N\n")
    option = option.strip()
    while(not(option == "Y" or option == "N")):
        option = input("Option invalid, Y or N for file write: \n")
        option = option.strip()

    if(option == "Y"):
        fileWrite(morse)
        print("Writing done, exiting program")
        
    elif (option == "N"):
        print("No write. Exiting program")






