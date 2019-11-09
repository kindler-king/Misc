"""
Arya Sarkar
TEXT BASED ADVENTURE GAME
10/18/2019
PYTHON PROJECT- GROUP 4
"""
import time 
from sys import exit

print("You wake up looking at an unfamiliar ceiling. There is a sharp pain at the back of your head.You look to your left slowly to find an unknown elderly man sitting by the bed staring at you.")
time.sleep(1)
print("\n","Seeing that you've woken up, he suddenly seemed to be on guard. His features gave away that this was no ordinary senile old man. He seemed wise and battle trained.")
time.sleep(1)
print("\n", "GOOD THAT YOU'VE WOKEN UP, OTHERWISE WOULD'VE BEEN A HASSLE GETTING RID OF YOUR BODY. WHO'RE YA CHAP? WHATS YER NAME. asked the old man" )
name=str(input("ENTER YOUR NAME : "))
time.sleep(1)

#STARTING POINT OF THE GAME   

def start_room():
        choice_list=["1","2"]
        choice1=""
        print("\n", "OH GOOD GODS I'VE HEARD OF YER NAME. I WONT ASK WHAT SOMEONE AS INFAMOUS AS YOU ARE DOING DOWN HERE IN THE DUMPS JUST LEAVE FIRST THING IN THE MORNING I DONT WANT ANY HASSLE IN MY HOME." )
        time.sleep(1)
        print('\n The night passes by... you dream of the events leading to your situation right now. You were betrayed by your one and only sworn partner and thrown into the most treacherous dungeon for the crimes you didnt commit.')
        time.sleep(2)
        while choice1 not in choice_list:
            print('\n','THE FIRST SUN WAS UP:','\n',"1. THANK THE STRANGE ELDER BEFORE LEAVING","\n","2. SAY NOTHING AND  LEAVE THE SHACK QUIETELY","\n","MAKE A CHOICE TO CONTINUE...")
            choice1=str(input("ENTER YOUR CHOICE (1/2) : "))
        if choice1 == choice_list[0]:
            room1()
        elif choice1==choice_list[1]:
            room2()

#SCENARIO 1 BASED ON PREV CHOICE

def room1():
    choice_list=["1","2"]
    choice2=""
    time.sleep(1)
    print("The elder stops you as you're about to leave and asks you a question.","\n","name"+" ARE YOU RESPONSIBLE FOR THE MURDER OF YOUR FAMILY LIKE THEY ALL SAY? YOU DONT SEEM LIKE A BAD FELLOW TO ME.")
    time.sleep(1)
    while choice2 not in choice_list:
        print("\n 1. I DIDNT KILL THEM BUT ITS MY FAULT THEY DIED.","\n 2. I KILLED THEM, I HAD TO.")
        choice2=str(input("ENTER YOUR CHOICE (1/2) : "))
    if choice2 == choice_list[0]:
        print("\n I KNEW THAT MY INTUITONS WERENT WRONG, I CAN TELL YOU ARE QUITE A DISCIPLINED AND TRAINED WARRIOR AND THERES NO WAY YOU'D KILL YER OWN BLOOD. WHATS DONE IS DONE YOU CANT CHANGE THE PAST BUT YOU CAN CHANGE THE FUTURE FOR SURE")
        time.sleep(1)
        print('\n The old man gave you a backpack of supplies and a SWORD, "YE LOOK LIKE A WARRIOR USE THESE AND GET YERSELF OUT OF THESE DUMPS, YE DONT DESERVE TO BE DOWN HERE." You thank the old man for his kindness and leave. ' )
        room2_1()
    elif choice2 == choice_list[1]:
        time.sleep(1)
        print("\n THERE AINT NO REASON STRONG ENOUGH THAT COULD MAKE YOU KILL YOUR OWN BLOOD, YOU DIGUST ME GET OUT IMMEDIATELY BEFORE I GET RID OF YOU MYSELF")
        room2()

#SCENARIO 2 BASED ON PREV CHOICE
        
def room2():
    choice_list=["1","2"]
    choice3=""
    time.sleep(1)
    print("\n You leave the shack and encounter monsters after travelling just a bit. A group of huge SLIMES were in the region and it would be hard to avoid them and run away. In the above world slimes were the weakest monsters even kids could defeat them but you dont know about what it would be down here.")
    while choice3 not in choice_list:
        print("\n 1. TRY TO BEAT THE SLIME WITH A STICK YOU FOUND","\n","2. TRY TO AVOID THEM AND RUN AWAY")
        choice3=str(input("ENTER YOUR CHOICE (1/2) : "))
    if choice3 == choice_list[0]:
        time.sleep(2)
        print("\n THESE SLIMES ARE MUCH STRONGER THAN NORMAL ONES, ITS EXPECTED SINCE THIS IS ONE OF THE MOST DANGEROUS DUNGEONS IN THE WORLD. YOU COULD BEAT IT IF YOU HAD A SWORD BUT THE STICK BREAKS ASAP. AND THE SLIME ACID MELTS YOUR SKIN AND BONES AND YOU DIE IN PAIN.")
        end()   
    elif choice3 == choice_list[1]:
        time.sleep(2)
        print("\n YOU TRY TO AVOID THE SLIMES, BUT WHILE TRYING TO CROSS THE LEDGE THE ROCK GIVES AWAY UNDER YOUR WEIGHT AND YOU FALL TUMBLING DOWN, YOU SOMEHOW USE A STICK TO MAINTAIN BAL:ANCE BUT END UP HURTING YOUR LEG BAD, YOU CANT RUN ANYMORE.")

#SCENARIO 2.1 BASED ON SCENARIO  1
       
def room2_1():
    choice_list=["1","2"]
    choice4=""
    time.sleep(1)
    print("\n You leave the shack and encounter monsters after travelling just a bit. A group of huge SLIMES were in the region and it would be hard to avoid them and run away. In the above world slimes were the weakest monsters even kids could defeat them but you dont know about what it would be down here. ITS A GOOD THING THAT YOU HAVE A SWORD")
    while choice4 not in choice_list:
        print("\n 1. FIGHT THE SLIMES WITH THE SWORD THE OLD MAN GAVE YOU","\n","2. TRY TO AVOID THEM AND RUN AWAY")
        choice4=str(input("ENTER YOUR CHOICE (1/2) : "))
    if choice4 == choice_list[0]:
        time.sleep(1)
        print("\n Even though the slimes were stronger down here, IT'S A PIECE OF CAKE FOR",name,"THE SWORD SAINT.")
        print("... The monsters drop a suspicious key...")
        


def end():
    print("\n"*4)
    print("YOU SEE YOUR LIFE SLIPPING BY. YOU THE STRONGEST WARRIOR IN THE HIGH KINGDOM OF VALERIA DIDNT DESERVE SUCH AN END. MAY IN YOUR NEXT LIFE YOU FIND HAPINESS.")
    time.sleep(2)
    print("\n ---THE END---")
    print ("\n PLAY AGAIN (y / n)")
    time.sleep(1)
    exit_var = input("Press Y or N: ")
    if "n" in exit_var or "N" in exit_var:
        exit(0)
    else:
        start_room() 

def break_leg():
    print("..The Pain is excrutiating as down here the air stings. You continue on with a broken leg. ")
    time.sleep(2)
    print("After Travelling some more you spot a dragon sleeping by a huge gate. Dragons are wise creatures they have no interest in humans as they are superior.")
    print("\n 1. TRY TO SNEAK PAST THE DRAGON","2. TRY TO BARGAIN WITH THE DRAGON ")
        
#Main PROGRAM
start_room()