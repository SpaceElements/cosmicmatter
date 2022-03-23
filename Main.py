#####################
# SpacePy
# 
# Created by Ira Bell
# 
# License: Spacepy is goverened under a BSD 3-Clause "New" or 
# "Revised" License, which is a permissive license similar to 
# the BSD 2-Clause License, but with a 3rd clause that prohibits 
# others from using the name of the project or its contributors 
# to promote derived products without written consent.
#
# GitHub: https://github.com/SpaceElements/spacepy
# 
#####################

#####################
# Libraries Go Here #
#####################

import time

###################
# Classes Go Here #
###################


class bcolors:
    WHITE = '\033[97m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    GREY = '\033[90m'
    SOFTWHITE = '\033[37m'
    SOFTCYAN = '\033[36m'
    SOFTMAGENTA = '\033[35m'
    SOFTBLUE = '\033[34m'
    SOFTYELLOW = '\033[33m'
    SOFTGREEN = '\033[32m'
    SOFTRED = '\033[31m'
    SOFTGREY = '\033[30m'
    DRACULA = '\033[38;5;87m'
    ENDC = '\033[0m'

class Equipment:
    def __init__(self, item1, item2, item3, item4, item5, item6):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        self.item6 = item6

    def __repr__(self):
        rep = bcolors.GREY + "You are currently equiped with the following" + "\n" + bcolors.WHITE + "____________________________________________" + "\n" + bcolors.BLUE + "Item 1: " + self.item1 + "\n" + "Item 2: " + self.item2 + "\n" + "item 3: " + self.item3 + "\n\n" + bcolors.GREY + "Secret Stash:" + "\n" + bcolors.WHITE + "____________________________________________" + "\n" + bcolors.SOFTWHITE + "Item 4: " + self.item4 + "\n" + "Item 5: " + self.item5 + "\n" "Item 6: " + self.item6 + bcolors.ENDC
        return rep

############################
# Global Variables Go Here #
############################

var = currentRoomNumber = 1000
somevariable = Equipment("shield", "sword", "helmet", "private cert 1", "privatecert2", "privatecert3")

#####################
# Functions Go Here #
#####################

def countdown(t):
    
    print("")
    print("Take a deep breath and find your center.")
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print('Loading...')


def room_1000():
  global currentRoomNumber
  currentRoomNumber = 1000
  print("")
  print(bcolors.YELLOW + "A Large Cylindrical Room")
  print("")
  print(bcolors.GREY + "You appear in a cylindrical room with four exits. To the" + bcolors.ENDC)
  print(bcolors.GREY + "south is the Hall of Chemistry. To the west is the Hall of" + bcolors.ENDC)
  print(bcolors.GREY + "Mathematics. To the north is the Astronomer's Lodge. To the" + bcolors.ENDC)
  print(bcolors.GREY + "east is the Library. A loose board creaks below your feet." + bcolors.ENDC)
  print(bcolors.GREY + "In the middle of the floor, the words Nosce Te Ipsum glow.")
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.SOFTWHITE + "A " + bcolors.GREEN + "green " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "SROCDK24" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTYELLOW + "yellow " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "SROTAKFC76" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "DEERCDK20A" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "DEERCDK20B" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "DEERCDK17A" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "DEERCDK17B" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.GREEN + "green " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "MOBMEADELK200" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.GREEN + "green " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "MOBTAKTSA120" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "MOBCDK14" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "A holographic being appears and says:")
  print("")
  print(bcolors.WHITE + "-> 'Ohh how I wish someone would name me.'"+ bcolors.ENDC)
  initial_menu()

def room_1001():
  global currentRoomNumber
  currentRoomNumber = 1001
  print("")
  print(bcolors.YELLOW + "The Great SpacePy Library")
  print("")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.WHITE + "A dusty book is" + bcolors.GREEN + " " + "floating" + " " + bcolors.WHITE + "here" + bcolors.ENDC)
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "You see a man who resembles Carl Sagan in the sitting at a desk in the corner." + bcolors.ENDC)
  print(bcolors.GREY + "The man looks up at you and smiles, then says:")
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.WHITE + "-> 'Pale blue dot. It's just a pale, blue dot.'"+ bcolors.ENDC)
  initial_menu()

def room_1002():
  global currentRoomNumber
  currentRoomNumber = 1002
  print("")
  print(bcolors.YELLOW + "The Astronomer's Lodge")
  print("")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.WHITE + "Mission control is" + bcolors.GREEN + " " + "floating" + " " + bcolors.WHITE + "here" + bcolors.ENDC)
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "Something smells like it was recently burning.")
  print(bcolors.GREY + "Einstein smiles in your direction and says:")
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.WHITE + "-> 'Hello, I'm not sure you should be here. But what's done is done.'"+ bcolors.ENDC)
  initial_menu()

def room_1003():
  global currentRoomNumber
  currentRoomNumber = 1003
  print("")
  print(bcolors.YELLOW + "The Hall of Mathematics")
  print("")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.WHITE + "A calculator is" + bcolors.GREEN + " " + "floating" + " " + bcolors.WHITE + "here" + bcolors.ENDC)
  print(bcolors.WHITE + "A ruler is" + bcolors.GREEN + " " + "floating" + " " + bcolors.WHITE + "here" + bcolors.ENDC)
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "Two men are standing near a chalkboard, debating.")
  print(bcolors.GREY + "One of the men looks up at you and says:")
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.WHITE + "-> 'Hello, I'm Euclid. And this is Pythagoras.'"+ bcolors.ENDC)
  initial_menu()

def room_1004():
  global currentRoomNumber
  currentRoomNumber = 1004
  print("")
  print(bcolors.YELLOW + "The Hall of Chemistry")
  print("")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.WHITE + "A centrifuge is" + bcolors.GREEN + " " + "here" + bcolors.GREY + ".")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "A man silently mixes a compound in the corner.")
  print(bcolors.GREY + "He glances up at you and says:")
  print("")
  print(bcolors.WHITE + "-> 'Don't - touch - anything. I mean it.'"+ bcolors.ENDC)
  initial_menu()

def room_1005():
  global currentRoomNumber
  currentRoomNumber = 1005
  print("")
  print(bcolors.YELLOW + "The Hall of Cloud Computing")
  print("")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.SOFTWHITE + "A " + bcolors.GREEN + "green " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "AzureStorage" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.GREEN + "green " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "AzureVM1039" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "AzureMediaServices" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "A mysterious man is walking around with a clipboard, taking notes.")
  print(bcolors.GREY + "The man looks up at you and asks:.")
  print("")
  print(bcolors.WHITE + "-> 'I wonder if you happen to have an opinion on who the best cloud provider might be?'"+ bcolors.ENDC)
  initial_menu()

def lookAction():
  if currentRoomNumber == 1000:
    room_1000()
  elif currentRoomNumber == 1001:
    room_1001()
  elif currentRoomNumber == 1002:
    room_1002()
  elif currentRoomNumber == 1003:
    room_1003()
  elif currentRoomNumber == 1004:
    room_1004()
  elif currentRoomNumber == 1005:
    room_1005()
  else:
    initial_menu()

def areaOfSquare():
  lengthSide = int(input("Enter the length of one side: x -> "))
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.WHITE + "We shall now calculate the area of the square:" + bcolors.ENDC)
  print(bcolors.GREEN + "Formula: x^2" + bcolors.ENDC)
  lengthSide = lengthSide ** 2
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.SOFTWHITE + "Answer: " + str(lengthSide))
  print(bcolors.GREY + "" + bcolors.ENDC)
  initial_menu()

def exit_message():
  print("exit message")
  exit()

def call_menu():
  print("")
  print(bcolors.YELLOW + "Global Menu Options" + bcolors.ENDC)
  print(bcolors.SOFTWHITE + "----------------------------------------------------" + bcolors.ENDC)
  print(bcolors.GREY + "area of a square" + bcolors.ENDC)
  print(bcolors.GREY + "area of a square" + bcolors.ENDC)
  print(bcolors.GREY + "area of a circle" + bcolors.ENDC)
  print(bcolors.GREY + "area of a triangle" + bcolors.ENDC)
  print(bcolors.GREY + "luminosity of a star" + bcolors.ENDC)
  print(bcolors.GREY + "define" + bcolors.ENDC)
  initial_menu()

def initial_menu():
  print(bcolors.GREY + "" + bcolors.ENDC)
  menuChoice = input(bcolors.CYAN + "Enter a command, explorer. " + bcolors.SOFTWHITE + "-> " + bcolors.ENDC)
  global currentRoomNumber
  if menuChoice == "east" or menuChoice == "e":
    room_1001()
  elif menuChoice == "north" or menuChoice == "n":
    room_1002()
  elif menuChoice == "west" or menuChoice =="w":
    room_1003()
  elif menuChoice == "south" or menuChoice == "s":
    room_1004()
  elif menuChoice == "down" or menuChoice == "d":
    room_1005()
  elif menuChoice == "menu":
    call_menu()
    initial_menu()
  elif menuChoice == "batch":
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.GREY + "A holographic being acknolwedges your request and says:")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.WHITE + "-> 'Your wish is my command. The batch has been executed.'"+ bcolors.ENDC)
    import subprocess
    subprocess.call([r'C:\Users\Space\Desktop\Scripts\batch-obtain-local-copy-of-images.bat'])
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.WHITE + "-> 'The hologram releases his grasp from your hand.'"+ bcolors.ENDC)
    initial_menu()
  elif menuChoice == "batch2":
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.GREY + "A holographic being acknolwedges your request and says:")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.WHITE + "-> 'Your wish is my command. The batch has been executed.'"+ bcolors.ENDC)
    import subprocess
    subprocess.call([r'C:\Users\Space\Desktop\Scripts\batch-script-make-directories.bat'])
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.WHITE + "-> 'The hologram releases his grasp from your hand.'"+ bcolors.ENDC)
    initial_menu()
  elif menuChoice == "look" or menuChoice == "l":
    lookAction()
    print(currentRoomNumber)
  elif menuChoice == "eq" or menuChoice == "equipment":
    print(repr(somevariable))
    initial_menu()
  elif menuChoice == "area of a square":
    areaOfSquare()
#  elif menuChoice == "open script":
#    import subprocess
#    subprocess.call([r'C:\Users\Space\Desktop\Scripts\script.bat'])
#    subprocess.call([r'c:\Progra~1\Sublim~1\subl.exe c:\Users\space\Desktop\spacepy\delscript.bat'])
#    print(bcolors.GREY + "" + bcolors.ENDC)
#    print(bcolors.WHITE + "-> 'The hologram releases his grasp from your hand.'"+ bcolors.ENDC)
#    initial_menu()
  elif menuChoice == "exit" or menuChoice == "x":
    exit_message()
  elif menuChoice == "quit" or menuChoice == "q":
    exit_message()
  else:
    print(bcolors.GREY + "Enter" + " " + bcolors.WHITE + "menu" + bcolors.GREY + " " + "for options." + bcolors.ENDC)
    initial_menu()

def credits():
  print(bcolors.GREY + "_________________________________________" + bcolors.ENDC)
  print(bcolors.GREY + " ->" + " " + bcolors.SOFTCYAN + "SpacePy" + bcolors.ENDC)
  print(bcolors.GREY + " -> Version:" + " " + bcolors.SOFTGREEN + "0.01a" + bcolors.ENDC)
  print(bcolors.GREY + " -> Release:" + " " + bcolors.SOFTGREEN + "March 20th, 2022" + bcolors.ENDC)
  print(bcolors.GREY + "_________________________________________" + bcolors.ENDC)
  print("")
  print(bcolors.GREY + "_________________________________________" + bcolors.ENDC)
  print(bcolors.GREY + " -> Created by: Ira Bell" + bcolors.ENDC)
  print(bcolors.GREY + " -> Founder @ Space Elements" + bcolors.ENDC)
  print(bcolors.GREY + " -> www.spaceelements.com" + bcolors.ENDC)
  print(bcolors.GREY + "_________________________________________" + bcolors.ENDC)
  countdown(int(7))

def welcomeScreen():
  print("")
  print(bcolors.YELLOW + "A Large Cylindrical Room")
  print("")
  print(bcolors.GREY + "You appear in a cylindrical room with four exits. To the" + bcolors.ENDC)
  print(bcolors.GREY + "south is the Hall of Chemistry. To the west is the Hall of" + bcolors.ENDC)
  print(bcolors.GREY + "Mathematics. To the north is the Astronomer's Lodge. To the" + bcolors.ENDC)
  print(bcolors.GREY + "east is the Library. A loose board creaks below your feet." + bcolors.ENDC)
  print(bcolors.GREY + "In the middle of the floor, the words Nosce Te Ipsum glow.")
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.SOFTWHITE + "A " + bcolors.GREEN + "green " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "SROCDK24" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTYELLOW + "yellow " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "SROTAKFC76" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "DEERCDK20A" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "DEERCDK20B" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "DEERCDK17A" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "DEERCDK17B" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.GREEN + "green " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "MOBMEADELK200" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.GREEN + "green " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "MOBTAKTSA120" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.SOFTWHITE + "A " + bcolors.SOFTRED + "red " + bcolors.SOFTWHITE + "orb named " + bcolors.WHITE + "MOBCDK14" + bcolors.SOFTWHITE + " is floating here")
  print(bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "A holographic being appears and says:")
  print(bcolors.WHITE + "-> 'Ohh how I wish someone would name me.'"+ bcolors.ENDC)
  print(bcolors.GREY + "" + bcolors.ENDC)
  print(bcolors.GREY + "The holographic figure grins at you and says:"+ bcolors.ENDC)
  print(bcolors.WHITE + "-> 'Welcome to" + bcolors.SOFTCYAN + " " + "SpacePy"+ bcolors.WHITE + ", traveler.'" + bcolors.ENDC)

#########################
# Main Code Here        #
#########################


## Calls copyright information
credits()
## First time splash / welcome screen
welcomeScreen()
## imitialize main program
initial_menu()
## exit in case of weirdness
exit()






