# Area of a Square
class bcolors:
    AA = '\033[1m'
    AB = '\033[2m'
    AC = '\033[3m'
    AD = '\033[4m'
    AE = '\033[5m'
    AF = '\033[6'
    AG = '\033[7m'
    AH = '\033[8m'
    AI = '\033[9m'
    AJ = '\033[10m'
    AK = '\033[11m'
    AL = '\033[12m'
    AM = '\033[13m'
    AN = '\033[14m'
    AO = '\033[15m'
    AP = '\033[16m'
    AQ = '\033[17m'
    AR = '\033[18m'
    AS = '\033[19m'
    AT = '\033[20m'
    AU = '\033[21m'
    AV = '\033[21m'
    AW = '\033[22m'
    AX = '\033[23m'
    AY = '\033[24m'
    AZ = '\033[96m'
    BA = '\033[38;5;206m'
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


print(bcolors.BA + "Initializing SpacePy" + bcolors.ENDC)
print(bcolors.DRACULA + "...." + bcolors.ENDC)
print(bcolors.DRACULA + "..." + bcolors.ENDC)
print(bcolors.DRACULA + "....." + bcolors.ENDC)
print(bcolors.DRACULA + "...." + bcolors.ENDC)
print(bcolors.DRACULA + "..." + bcolors.ENDC)
print(bcolors.DRACULA + "..." + bcolors.ENDC)
print(bcolors.DRACULA + "........" + bcolors.ENDC)

# print(bcolors.DRACULA + "Warning: Ira has figured out colors in Python. Continue?" + bcolors.ENDC)

# print("\\033[XXm")

for i in range(30,37+1):
    print("\033[%dm%d\t\t\033[%dm%d" % (i,i,i+60,i+60));

# print("\033[39m\\033[49m - Reset colour")
# print("\\033[2K - Clear Line")
# print("\\033[<L>;<C>H OR \\033[<L>;<C>f puts the cursor at line L and column C.")
# print("\\033[<N>A Move the cursor up N lines")
# print("\\033[<N>B Move the cursor down N lines")
# print("\\033[<N>C Move the cursor forward N columns")
# print("\\033[<N>D Move the cursor backward N columns")
# print("\\033[2J Clear the screen, move to (0,0)")
# print("\\033[K Erase to end of line")
# print("\\033[s Save cursor position")
# print("\\033[u Restore cursor position")
# print(" ")
# print("\\033[4m  Underline on")
# print("\\033[24m Underline off")
# print("\\033[1m  Bold on")
# print("\\033[21m Bold off")
#Ensure Clear / Reset can occur at the end of every respective line.
# print(bcolors.AA + "Warning: Ira has figured out colors in Python. Continue?" + bcolors.ENDC)
# print(bcolors.AB + "Warning: Ira has figured out colors in Python. Continue?" + bcolors.ENDC)
# print(bcolors.AC + "Warning: Ira has figured out colors in Python. Continue?" + bcolors.ENDC)
# print(bcolors.AD + "Warning: Ira has figured out colors in Python. Continue?" + bcolors.ENDC)

# print(bcolors.WHITE + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.CYAN + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.MAGENTA + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.BLUE + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.YELLOW + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.GREEN + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.RED + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.GREY + "Color Initialize..." + bcolors.ENDC)

# print(bcolors.SOFTWHITE + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.SOFTCYAN + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.SOFTMAGENTA + "Color Initialize.. " + bcolors.ENDC)
# print(bcolors.SOFTBLUE + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.SOFTYELLOW + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.SOFTGREEN + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.SOFTRED + "Color Initialize..." + bcolors.ENDC)
# print(bcolors.SOFTGREY + "Color Initialize..." + bcolors.ENDC)


print(bcolors.GREY + "_________________________________________" + bcolors.ENDC)
print(bcolors.GREY + " -> Created by Ira Bell" + bcolors.ENDC)
print(bcolors.GREY + " -> Version 0.01a" + bcolors.ENDC)
print(bcolors.GREY + " -> Release: March 20th, 2022" + bcolors.ENDC)
print(bcolors.GREY + "_________________________________________" + bcolors.ENDC)
print(bcolors.GREY + "" + bcolors.ENDC)
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

import subprocess
subprocess.call([r'C:\Users\Space\Desktop\Scripts\script2.bat'])

# print("Area of a square.")
# intSquareSideLength = int(input("Enter a number: "))
# squared = intSquareSideLength ** 2
# print("The area of a square is %s" % squared)

print("")
chooseDirection = input(bcolors.CYAN + "Enter a command. " + bcolors.SOFTWHITE + "-> " + bcolors.ENDC)

goesEast = "You travel east, to the Libary"
goesSouth = "You travel south, to the Hall of Chemistry"
goesWest = "You travel west, to the Hall of Mathematics"
goesNorth = "You travel north, to the Astronomer's Lodge"

if chooseDirection == "east":
    print(bcolors.GREY + "" + bcolors.ENDC)
    print("You travel east, to the libary.")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.GREY + "You see a man who resembles Carl Sagan in the sitting at a desk in the corner." + bcolors.ENDC)
    print(bcolors.GREY + "The man looks up at you and smiles, then says:")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.WHITE + "-> 'Pale blue dot. It's just a pale, blue dot.'"+ bcolors.ENDC)
elif chooseDirection == "south":
    print("You travel south, to the Hall of Chemistry.")
elif chooseDirection == "west":
    print(bcolors.GREY + "" + bcolors.ENDC)
    print("You travel west, to the Hall of Mathematics.")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.GREY + "Two men are standing near a chalkboard, debating.")
    print(bcolors.GREY + "One of the men looks up at you and says:")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.WHITE + "-> 'Hello, I'm Euclid. And this is Pythagoras.'"+ bcolors.ENDC)
elif chooseDirection == "north":
    print(bcolors.GREY + "" + bcolors.ENDC)
    print("You travel north, to the Astronomer's Lodge.")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.GREY + "Something smells like it was recently burning.")
    print(bcolors.GREY + "Einstein smiles in your direction and says:")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.WHITE + "-> 'Hello, I'm not sure you should be here. But what's done is done.'"+ bcolors.ENDC)
elif chooseDirection == "down":
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.GREY + "You open the trap door and travel down, to the Cloud Room")
    print(bcolors.GREY + "" + bcolors.ENDC)
    print(bcolors.WHITE + "Cloud Service 1")
    print(bcolors.WHITE + "Cloud Service 2")
    print(bcolors.WHITE + "Cloud Service 3")
else:
	print ("Please enter east, west, north, or south")
	chooseDirection = input(bcolors.CYAN + "Enter a command, explorer. " + bcolors.SOFTWHITE + "-> " + bcolors.ENDC)

print(bcolors.GREY + "..." + bcolors.ENDC)
chooseDirection = input(bcolors.CYAN + "Enter a command, explorer. " + bcolors.SOFTWHITE + "-> " + bcolors.ENDC)  

print(bcolors.SOFTGREY + "..." + bcolors.ENDC)
print(bcolors.SOFTGREY + "..." + bcolors.ENDC)
print(bcolors.WHITE + "Thank you for using" + bcolors.SOFTCYAN + " " + "SpacePy"+ bcolors.WHITE + "." + bcolors.ENDC)
print(bcolors.SOFTBLUE + "www.spaceelements.com" + bcolors.ENDC)
print(bcolors.SOFTGREY + "..." + bcolors.ENDC)
print(bcolors.SOFTGREY + "..." + bcolors.ENDC)