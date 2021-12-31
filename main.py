# Created by Zachary Criswell

from PIL import Image
import time
import pyglet
from playsound import playsound

def ask_name():
    name = input("Tell me your name ")
    if name.lower() == 'no':
        print("If you refuse to give me even this, then I can't trust you. Good bye")
        exit()
    else:
        pass

    answer = input("'" + name + "', Is this correct? ")
    if answer.lower() == 'y' or answer.lower() == 'yes':
        game_start()
    elif answer.lower() == 'n' or answer.lower() == 'no':
        ask_name()
    else:
        print("I do not understand.")
        ask_name()


def game_start():
    print("You did it")

ask_name()