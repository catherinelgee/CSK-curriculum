"""CSK's very own choose your own adventure game!
based off project developed by CSK Curriculum Committee 2019
special thanks and credit to Julia Yu, Rachel Gregory"""

# The lines below import code other people have written to help us do cool things like have randomization.
import random as rand
import sys
import time
from art import *

# This fancy code prints out the cool header art! Don't worry if you don't understand it.
header = text2art("Go Bears!")
print(header)


# Don't worry if you don't understand this piece of code!.
typing_speed = 350
def slow_type(msg):
    """Prints text slowly, as if it's being typed in terminal"""
    for letter in msg:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')

def bad_input(repeat_msg, correct):
    """This function will repeat infinitely until an input in the proper range of values is inputted by user.
    returns a string of the correct input"""
    while True:
        slow_type(repeat_msg)
        choice = input()
        if choice in correct:
            return choice

######################################################
# ~ Intro ~
######################################################

# The following variable serves as the "in game time" because some decisions might take too long depending on your choice
game_time = 0

# List of names you can make friends with
friends = ["Amy", "Carl", "Cara", "Kevin", "Chad", "Catherine", "Julia", "Rachel", "Stephan"]
met_people = []

# Below is an example of calling a function.
slow_type("Hello there! Before we embark on this Cal adventure, what is your name?")

# Below, we are setting a variable (name) to a user input.
name = input()

slow_type("Congratulations, " + name + ". You are going to be a student at the world's number one public university! Woohoo! \
This definitely calls for a Go Bears! As a new cal bear on campus for all new incoming freshman there's a new rite of passage, \
GBO. Since this year we might not be able to meet in person you can play through this game to find out activities you might be \
interested in doing! Continue?\n y/n")

choice = input()

if choice == "n":
    slow_type("Guess you aren't interested in finding out what Cal has to offer...")
    for i in range(5):
        really_print = ""
        for really in range(i):
            really_print+="really "
        slow_type("Are you "+really_print+"sure?\n y/n")
        input()
    slow_type("Too bad you have to play anyways")


######################################################
# ~ Finding your GBO Group ~
######################################################

slow_type("Now that we have your passion about playing this game taken care of "+ name +", let's continue with our journey! It's the first day of \
GBO and you have a group number but no idea where to meet your group! Where do you go first?\n 0: Towards a clock tower in \
the distance\n1: A green gate where many students are congregating\n2: A hill surrounded by trees\n 0/1/2")

first_choice = int(input())
path = 0

if first_choice not in [0,1,2]:
    first_choice = int(bad_input("That's not a place you marked down as interesting.\n Where do you want to go?\n 0/1/2?", [0,1,2]))

if first_choice == 0:
    slow_type("You have arrived at the Campanile! The Campanile is the third-tallest bell and clock-tower \
    in the world, and an integral part of the campus experience. You can ride up the Campanile for free \
    if you have your student ID! You spot some students about to go up, but are unsure if you want to join them \
    because you still haven't found your GBO group. Do you join them? \n y/n")
    path = 1
elif first_choice == 1:
    slow_type("You arrive at the gate and notice a couple of things. In front of you is a lot of tables with people handing out flyers. \
    There are also some groups you see with signs with numbers on it that could be your GBO group, but you can't read the numbers \
    from where you are. Where do you go, 0: check out the tables or 1: the signs?\n 0/1")
    path = 2
else:
    slow_type("You walk towards the hill, and strangely enough you see people rolling down the hill? What's going on? \
    You lumber down to the bottom of the hill and ask someone what they're doing. They seem a little shocked you don't \
    know what's going on but they seem ready to explain everything to you.")
    slow_type("What do you ask first?\n 0: So why are you rolling down this hill?\n 1: What's your name?\
    \n2: Can I roll down the hill with you?")
    options = 1
    while options:
        subchoice = int(input())
        if subchoice not in [0,1,2]:
            subchoice = int(bad_input("That's not something you want to say!", [0,1,2]))
        if subchoice == 0:
            slow_type("'So why are you rolling down this hill?' You ask. They laugh and tell you that if you roll down \
            the hill that you're destined to get a 4.0. As it turns out, you're at 4.0 hill!")
            slow_type("Do you have any other questions? They ask.")
            slow_type("0: So why are you rolling down this hill?\n 1: What's your name?\
            \n2: Can I roll down the hill with you?")
        elif subchoice == 1:
            friend_name = rand.choice(friends)
            if friend_name in met_people:
                friend_name = rand.choice(friends)
                met_people += [friend_name]
            slow_type("'Wait, what's your name?' You ask. You want to make friends you think. \
            They answer, 'My name is '" +friend_name+".")
            slow_type("Do you have any other questions? They ask.")
            slow_type("0: So why are you rolling down this hill?\n 1: What's your name?\
            \n2: Can I roll down the hill with you?")
        else:
            slow_type("Hey can I roll down this hill with you? It's not that weird of a question evidently because \
            they nod and you both roll down the hill. You can feel the knowledge rush into your brain. You WILL \
            get a 4.0 this semester, and it's all thanks to this hill. Once you're done rolling the other person \
            turns to you and asks if we want to hang out.\n y/n")
            options = 0
    path = 1

game_time += 1
second_choice = input()

######################################################
# ~ Splitting of Paths ~
######################################################

def friend_path(num_friends, potential, choice):
    """Choices and dialogue you can make to make friends
    rates of success contingent on current number of friends and other factors"""
    if choice == "n":
        # then you don't want to make friends ):
        slow_type("You politely tell them no thanks.")
        return

    luck = rand.random() #percentage chance of making friend(s)
    if num_friends == 0: # if you have no friends you are probably guaranteed at least one
        luck = 0.99


def club_path(curr_time):
    """Choice and dialogues you can have during the day for clubs
    Day is separated from [0,6) [6,12) [12,18) with 2 club choices each"""
    if curr_time in range(6):
        slow_type()
    elif curr_time in range(6, 12):
        slow_type()
    elif curr_time in range(12, 18):
        slow_type()
    else:
        slow_type("There are no more tables out on Sproul! Aw man, better come tomorrow to check it out.")

def explore_path(num_friends, curr_time):
    """Choices and dialogue you can make to explore Berkeley on your own
    involves a cute tour of downtown, where you can go is also dependent on time
    and number of friends with you. If it's night time you can see a movie otherwise all options same"""
    slow_type("")

######################################################
# ~ Second choice (following the paths) ~
######################################################

if
