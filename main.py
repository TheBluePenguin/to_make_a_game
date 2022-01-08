# Created by Zachary Criswell
from PIL import Image
import time
import sys
from playsound import playsound


def ask_name():
    global name
    name = input("Please tell me your name. ")
    if name.lower() == 'no':
        print("If you refuse to give me even your name, then I cant trust you.")
        time.sleep(2)
        slow_print("Good bye")
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


def slow_print(str):
    for letter in str:
        if letter != ' ':
            sys.stdout.write(letter)
            time.sleep(.20)
        else:
            sys.stdout.write(letter)


def bad_end():
    image = Image.open("assets/pictures/escape.png")
    image.show()
    playsound('assets/sounds/sample2.mp3')


def game_start():
    input("I could use your help " + name)
    input("I've really been struggling to finish any of the projects I've been working on.")
    input("I have so many good ideas, but I just can't seem to find time to do them all.")
    input("Like I got some great 8 bit soundtrack concepts in my head.")
    input("I just need to transfer them to a music production software.")
    input("But I'd have to learn more about how to USE a musical program before I really get running with that one.")
    input("I already have a music production program I want, but I just don't have it on my system right now.")
    input("I also got some fun drawing ideas. They are mostly original characters with cool twists.")
    input("Like a koi fish pattern for skin on a frog man. He's got the head of a frog, and flippers for hands/feet.")
    input("And He's like a traveller. So he's got a big backpack with a bunch of trinkets sticking out.")
    input("I'm calling him Weeple.")
    input("But I really only want to draw him if I can draw the whole series of mythical creatures I made up.")
    input("But as it stands now I haven't drawn in a couple years. I've seen a lot of videos on how to draw though!")
    input("I'm sure I can just transfer the skills over from what I watched.")
    slow_print("Im sorry " + name)
    time.sleep(2)
    print("\n")
    input("I'm starting to get off track here.")
    input("The point is. I have a lot of ideas and I need to really narrow down what I should be working on.")
    input("My last idea is I really want to make a game.")
    input("I've been stuck up in my room for so long playing other games I never ended up making ones I wanted.")
    input("I studied a lot of computer science back in college, but I haven't really done much since graduating.")
    answer = input(name + " What should I do? Make music, draw, or create a game? ")
    while answer != "valid response":
        if answer.lower() == "make music" or answer.lower() == "music":
            answer = 'valid response'
            music_end()
        elif answer.lower() == "draw":
            answer = 'valid response'
            draw_end()
        elif answer.lower() == "make a game" or answer.lower() == "create a game" or answer.lower() == "game":
            answer = 'valid response'
            game_continue()
        else:
            answer = input("I don't understand. Should I make music, draw, or create a game? ")


def music_end():
    input("I'm really happy you choose music.")
    input("I think music can really express what I feel in my soul.")
    input("I just need 200$ to afford the music production software.")
    input("Right now I'm not making any money so I wont be able to afford it.")
    input("But I can learn how to use it with some free Youtube tutorials!")
    input("I really don't want to use a free one, as I'd rather not be held back by any restrictions in the software.")
    input("I have a very particular idea for how I want my music to sound -")
    input("and only the nice software allows editing in the way I need.")
    input("...")
    input("I feel as if you are looking down on me.")
    input("That you think that I'm setting my standards too high.")
    input("...")
    input("It needs to be perfect!")
    input("I'm not going to use just any free crappy music production software! I need quality!")
    input("You said make some music, and if I'm going to make music, I'm going to do it MY way!")
    input("I don't need you " + name + ".")
    input("I bet you couldn't even appreciate the unique sounds I would create.")
    input("You're not helping me.")
    slow_print("Go away " + name)
    bad_end()


def draw_end():
    questions = []
    input("Alright " + name + " lets do some drawing!")
    input("I don't want to draw Weeple just yet, I want to improve my drawing skills a bit more before drawing him.")
    input("Instead I'll just draw some generic sword fighter. I just need to get some paper real quick...")
    slow_print("...")
    time.sleep(2)
    print(" ")
    slow_print("......")
    time.sleep(2)
    print(" ")
    slow_print("...............")
    time.sleep(2)
    print(" ")
    slow_print("......................")
    time.sleep(2)
    print(" ")
    input("Okay so I got some paper and a pencil but It's not drawing paper.")
    input("It's just some regular printer paper.")
    input("I also couldn't find my good pencil either but it's okay because this is just a practice drawing.")
    input("Okay, I know I said generic sword fighter but now I don't know what kind of sword we are talking about.")
    answer = input("Should I do a giant steel sword, a samurai sword, or a classic knight sword? ")
    while answer != "valid response":
        if answer.lower() == "samurai sword" or answer.lower() == "samurai":
            answer = 'valid response'
            input("Alright a samurai sword sounds good.")
        elif answer.lower() == "giant" or answer.lower() == "giant steel" or answer.lower() == "giant steel sword":
            answer = 'valid response'
            input("Alright a giant sword sounds good.")
        elif answer.lower() == "make a game" or answer.lower() == "create a game" or answer.lower() == "game":
            answer = 'valid response'
            input("Alright a classic sword sounds good.")
        else:
            answer = input("I don't understand. Draw a giant steel sword, a samurai sword, or a classic knight sword? ")
    input("Now lets think about armor")
    answer2 = input("Should I draw bulky armor, slim futuristic armor, or classic armor? ")
    while answer2 != "valid response":
        if answer2.lower() == "bulky" or answer2.lower() == "bulky armor":
            answer2 = 'valid response'
            input("Alright a bulky armor it is.")
        elif answer2.lower() == "slim armor" or answer2.lower() == "slim futuristic armor":
            answer2 = 'valid response'
            input("Alright slim futuristic armor it is.")
        elif answer2.lower() == "classic armor" or answer2.lower() == "classic":
            answer2 = 'valid response'
            input("Alright a classic armor it is.")
        else:
            answer2 = input("I don't understand. Draw a bulky armor, slim futuristic armor, or classic armor? ")
    input("Now lets talk about their size!")
    answer3 = input("Should I draw them as a big build, normal build, or a slender build? ")
    while answer3 != "valid response":
        if answer3.lower() == "big build" or answer3.lower() == "big":
            answer3 = 'valid response'
            input("One big man coming up.")
        elif answer3.lower() == "normal build" or answer3.lower() == "normal":
            answer3 = 'valid response'
            input("One normal sized man coming up")
        elif answer3.lower() == "slender build" or answer3.lower() == "slender":
            answer3 = 'valid response'
            input("One slender man coming up... And no not THAT kind of slender man.")
        else:
            answer3 = input("I don't understand. Draw them as a big build, normal build, or a slender build? ")
    input("Okay Im pooped. I think this is a great place to stop for today.")
    input("We spent a good while coming up with ideas for practice drawings.")
    input("But Im feeling pretty mentally tired now.")
    input("I think I'll start putting pencil to paper tomorrow.")
    slow_print("Ill see you again after I finish some practice drawings " + name)
    bad_end()


def game_continue():
    input("Okay " + name + " I think you are right.")
    input("I have a good understanding of programming, and I don't need to buy a game maker studio to make a game.")
    input("The hardest part for me right now, is figuring out what I want to make.")
    input("Here is one I just came up with on the fly!")
    input("A 3D adventure game, reenacting an epic tale of a knight who saves two warring kingdoms.")
    input("You'll get to choose which kingdom to fight for, and a bunch of different endings are possible.")
    input("I'll have to make the graphics. That might take a while.")
    input("I've never made 3D assets before.")
    input("Then I have to draw all the textures for it too.")
    input("But then I'll also be able to make some music to go with it!")
    input("I’ll have a big soundtrack that is full of classic instruments inspired by the medieval period.")
    input("By doing this I can draw, make music, and all the while make a video game!")
    answer = input("It's perfect; I can do all 3 at once! Isn't this a great idea?! ")
    while answer != 'valid response':
        if answer.lower() == "yes":
            input("This game is going to be awesome!")
            input("I got a lot to learn before I really start though")
            input("Its a bit overwhelming to be honest")
            input("But you said to do it, so Ill shoot for the stars!")
            input("Im going to watch some videos on how to make 3D assets.")
            input("Actually I should learn which program to use to make 3D assets before doing that.")
            input("The music is also going to be really important.")
            input("Maybe I should work on that first?")
            input("I guess the story needs to be created too. That is the first thing I should really work on.")
            input("I'll figure it out eventually. I just need to think on it for a while")
            bad_end()
        elif answer.lower() == "no":
            answer = 'valid response'
            true_end()
        else:
            answer = input("Its a yes or no question. Is this idea good? ")


def true_end():
    input("What do you mean? If I make a game I gotta go all out.")
    input("...")
    input("Well I guess there are text based adventure games, and some simple visual novels.")
    answer = input("Is that what you are suggesting? I make a text based adventure game? ")
    while answer != "valid response":
        if answer.lower() == "yes":
            answer = "valid response"
            input("Alright fine.")
            input("Ill do that.")
        elif answer.lower() == "no":
            answer = 'valid response'
            input("Well I really don't know what else to make that is simple but also interests me.")
            input("To be honest its not that bad of an idea. Making a text based adventure game.")
            input("I think I'll do it anyway.")
        else:
            answer = input("Its a yes or no question. Should I make a text based adventure game? ")
    input("But I am totally going to tell an awesome story.")
    input("I still like the epic tale of two kingdoms at war, and you, a humble knight, must stop the war.")
    input("It'll have a bunch of locations, NPCs, and puzzles. I'd probably have four different endings.")
    input("One ending for each respective kingdom winning, and one ending for mutual destruction.")
    input("Oh and of course the good ending where you make peace between the two.")
    input("But I guess that doesn't account for all the player deaths, those should be unique endings too.")
    input("And I could add a secret ending! Like where it's actually just a kid playing with a bunch of toys.")
    input("Or maybe a true ending? Like where the knight leaves the two kingdoms alone to do a different adventure.")
    answer2 = input("Does all that sound good for me to make? ")
    while answer2 != "valid response":
        if answer2.lower() == "yes":
            input("Awe heck yeah!")
            input("I knew you'd like it!")
            input("This game is going to be so awesome.")
            input("Im not really sure where to start.")
            input("This game is going to have so much depth, most people wont even scrape the bottom!")
            input("I remember getting some videos recommended to me about world building. Ill have to watch those.")
            input("I should also research The Hero's Journey.")
            input("Maybe I should read some fantasy books, and play some medieval RPG games for inspiration.")
            input("Ahhhh... but what to play? So many to choose from. Ill have to make a list.")
            bad_end()
        elif answer2.lower() == "no":
            answer2 = 'valid response'
            pass
        else:
            answer2 = input("Its a yes or no question. Does all that sound good for me to make? ")
    input("You are really putting a damper on my ideas here. " + name)
    input("I guess you want me to make the project smaller?")
    input("Perhaps something more familiar and personal...")
    input("I don't really know if I got any good small ideas...")
    input("I could just make the game like what I'm living through now.")
    input("Make it about someone struggling to figure out what to do with themselves.")
    input("They can't seem to finish anything they start.")
    input("And after doing this for years they finally get help from someone else, or a personified alter ego.")
    input("Then with their guidance they are able to select a project to work on, and make it simple enough to do.")
    input("And then they can FINALLY finish something.")
    answer3 = input("Does that sound like a feasible game " + name + "? ")
    while answer3 != "valid response":
        if answer3.lower() == "no":
            answer3 = "valid response"
            input("Well fuck you then!")
            input("I don't need your help!")
            input("You've been nothing but unsupportive!")
            input("I'm really trying to make something of myself and you can't even give me the encouragement to try.")
            input("I don't want to talk to you anymore.")
            bad_end()
        elif answer3.lower() == "yes":
            answer3 = 'valid response'
            pass
        else:
            answer3 = input("Its a yes or no question. Does all that sound good for me to make? ")
    input("I'm glad you are finally agreeing with me on something.")
    input("I really think I could do this too!. I'll just stick to keeping it simple.")
    input("I'll make it in Python. That's a simple programming language I'm already familiar with.")
    input("Do you mind leaving for just 2 minutes? I need to focus on writing some code.")
    for i in range(120, 0, -1):
        print('\r', str(i), end="")
        time.sleep(.1)
        print("\n")
    input("Thank you for waiting " + name)
    input("I got the whole project foundation set up.")
    input("All that's really left is adding a script for the story, and then just plugging it in to the code.")
    input("I was thinking about taking a break though.")
    input("I did a lot of work already.")
    input("I think I can just call it a day and work on it again next week.")
    input("I'll try to watch some videos on how to write a compelling narrative.")
    input("Oh! And maybe get some energy drinks to help me focus for longer next time")
    answer4 = input("What do you think? Should I take a break, or keep working? ")
    while answer4 != "valid response":
        if answer4.lower() == "keep working":
            answer4 = "valid response"
            pass
        elif answer4.lower() == "take a break":
            input("You're right. I deserve it.")
            input("I'm going to play some games first, then watch the videos after.")
            input("Probably tomorrow though. I don't feel like doing much else today")
            input("I think I did a lot.")
            bad_end()
        else:
            answer4 = input("I don't understand. Should I take a break? or keep working? ")
    input("You're probably right " + name)
    input("The hardest part of getting something done is to start.")
    input("And I already started, so let's just keep this momentum going!")
    input("I can type up the script really fast. Just give me a moment.")
    slow_print("...")
    time.sleep(2)
    print("\n")
    slow_print("......")
    time.sleep(2)
    print("\n")
    slow_print("...............")
    time.sleep(2)
    print("\n")
    slow_print("......................")
    time.sleep(2)
    print("\n")
    input("I did it " + name + "!!")
    input("I got it all finished and plugged into my code!")
    input("I can tell it's a bit rough but at least it's working.")
    input("It may not be perfect but it is functional and complete.")
    input("I can show this off to people even the way it is now!")
    input("I'll try to polish it a bit here and there. But for now I think it's safe to say it's completed.")
    input("Completed.")
    slow_print("Complete")
    time.sleep(1.5)
    slow_print("I really finished it")
    time.sleep(3)
    slow_print("Thank you " + name)
    time.sleep(4)
    print("I feel like this is the start of something great")

ask_name()
