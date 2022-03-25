# Area of a Square
import subprocess


class Bcolors:
    AA = "\033[1m"
    AB = "\033[2m"
    AC = "\033[3m"
    AD = "\033[4m"
    AE = "\033[5m"
    AF = "\033[6"
    AG = "\033[7m"
    AH = "\033[8m"
    AI = "\033[9m"
    AJ = "\033[10m"
    AK = "\033[11m"
    AL = "\033[12m"
    AM = "\033[13m"
    AN = "\033[14m"
    AO = "\033[15m"
    AP = "\033[16m"
    AQ = "\033[17m"
    AR = "\033[18m"
    AS = "\033[19m"
    AT = "\033[20m"
    AU = "\033[21m"
    AV = "\033[21m"
    AW = "\033[22m"
    AX = "\033[23m"
    AY = "\033[24m"
    AZ = "\033[96m"
    BA = "\033[38;5;206m"
    WHITE = "\033[97m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    GREY = "\033[90m"
    SOFTWHITE = "\033[37m"
    SOFTCYAN = "\033[36m"
    SOFTMAGENTA = "\033[35m"
    SOFTBLUE = "\033[34m"
    SOFTYELLOW = "\033[33m"
    SOFTGREEN = "\033[32m"
    SOFTRED = "\033[31m"
    SOFTGREY = "\033[30m"
    DRACULA = "\033[38;5;87m"
    ENDC = "\033[0m"


print(Bcolors.BA + "Initializing SpacePy" + Bcolors.ENDC)
print(Bcolors.DRACULA + "...." + Bcolors.ENDC)
print(Bcolors.DRACULA + "..." + Bcolors.ENDC)
print(Bcolors.DRACULA + "....." + Bcolors.ENDC)
print(Bcolors.DRACULA + "...." + Bcolors.ENDC)
print(Bcolors.DRACULA + "..." + Bcolors.ENDC)
print(Bcolors.DRACULA + "..." + Bcolors.ENDC)
print(Bcolors.DRACULA + "........" + Bcolors.ENDC)

# print(Bcolors.DRACULA + "Warning: Ira has figured out colors in Python. Continue?" + Bcolors.ENDC)

# print("\\033[XXm")

for i in range(30, 37 + 1):
    print("\033[%dm%d\t\t\033[%dm%d" % (i, i, i + 60, i + 60))

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
# Ensure Clear / Reset can occur at the end of every respective line.
# print(Bcolors.AA + "Warning: Ira has figured out colors in Python. Continue?" + Bcolors.ENDC)
# print(Bcolors.AB + "Warning: Ira has figured out colors in Python. Continue?" + Bcolors.ENDC)
# print(Bcolors.AC + "Warning: Ira has figured out colors in Python. Continue?" + Bcolors.ENDC)
# print(Bcolors.AD + "Warning: Ira has figured out colors in Python. Continue?" + Bcolors.ENDC)

# print(Bcolors.WHITE + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.CYAN + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.MAGENTA + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.BLUE + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.YELLOW + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.GREEN + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.RED + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.GREY + "Color Initialize..." + Bcolors.ENDC)

# print(Bcolors.SOFTWHITE + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.SOFTCYAN + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.SOFTMAGENTA + "Color Initialize.. " + Bcolors.ENDC)
# print(Bcolors.SOFTBLUE + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.SOFTYELLOW + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.SOFTGREEN + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.SOFTRED + "Color Initialize..." + Bcolors.ENDC)
# print(Bcolors.SOFTGREY + "Color Initialize..." + Bcolors.ENDC)


print(Bcolors.GREY + "_________________________________________" + Bcolors.ENDC)
print(Bcolors.GREY + " -> Created by Ira Bell" + Bcolors.ENDC)
print(Bcolors.GREY + " -> Version 0.01a" + Bcolors.ENDC)
print(Bcolors.GREY + " -> Release: March 20th, 2022" + Bcolors.ENDC)
print(Bcolors.GREY + "_________________________________________" + Bcolors.ENDC)
print(Bcolors.GREY + "" + Bcolors.ENDC)
print(
    Bcolors.GREY
    + "You appear in a cylindrical room with four exits. To the"
    + Bcolors.ENDC
)
print(
    Bcolors.GREY
    + "south is the Hall of Chemistry. To the west is the Hall of"
    + Bcolors.ENDC
)
print(
    Bcolors.GREY
    + "Mathematics. To the north is the Astronomer's Lodge. To the"
    + Bcolors.ENDC
)
print(
    Bcolors.GREY
    + "east is the Library. A loose board creaks below your feet."
    + Bcolors.ENDC
)
print(Bcolors.GREY + "In the middle of the floor, the words Nosce Te Ipsum glow.")
print(Bcolors.GREY + "" + Bcolors.ENDC)
print(Bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + Bcolors.ENDC)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.GREEN
    + "green "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "SROCDK24"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.SOFTYELLOW
    + "yellow "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "SROTAKFC76"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.SOFTRED
    + "red "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "DEERCDK20A"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.SOFTRED
    + "red "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "DEERCDK20B"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.SOFTRED
    + "red "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "DEERCDK17A"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.SOFTRED
    + "red "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "DEERCDK17B"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.GREEN
    + "green "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "MOBMEADELK200"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.GREEN
    + "green "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "MOBTAKTSA120"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(
    Bcolors.SOFTWHITE
    + "A "
    + Bcolors.SOFTRED
    + "red "
    + Bcolors.SOFTWHITE
    + "orb named "
    + Bcolors.WHITE
    + "MOBCDK14"
    + Bcolors.SOFTWHITE
    + " is floating here"
)
print(Bcolors.GREY + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-" + Bcolors.ENDC)
print(Bcolors.GREY + "" + Bcolors.ENDC)
print(Bcolors.GREY + "" + Bcolors.ENDC)
print(Bcolors.GREY + "A holographic being appears and says:")
print(
    Bcolors.WHITE +
    "-> 'Ohh how I wish someone would name me.'" +
    Bcolors.ENDC)
print(Bcolors.GREY + "" + Bcolors.ENDC)
print(
    Bcolors.GREY +
    "The holographic figure grins at you and says:" +
    Bcolors.ENDC)
print(
    Bcolors.WHITE
    + "-> 'Welcome to"
    + Bcolors.SOFTCYAN
    + " "
    + "SpacePy"
    + Bcolors.WHITE
    + ", traveler.'"
    + Bcolors.ENDC
)


subprocess.call([r"C:\Users\Space\Desktop\Scripts\script2.bat"])

# print("Area of a square.")
# intSquareSideLength = int(input("Enter a number: "))
# squared = intSquareSideLength ** 2
# print("The area of a square is %s" % squared)

print("")
chooseDirection = input(
    Bcolors.CYAN + "Enter a command. " + Bcolors.SOFTWHITE + "-> " + Bcolors.ENDC
)

goesEast = "You travel east, to the Libary"
goesSouth = "You travel south, to the Hall of Chemistry"
goesWest = "You travel west, to the Hall of Mathematics"
goesNorth = "You travel north, to the Astronomer's Lodge"

if chooseDirection == "east":
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print("You travel east, to the libary.")
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print(
        Bcolors.GREY
        + "You see a man who resembles Carl Sagan in the sitting at a desk in the corner."
        + Bcolors.ENDC
    )
    print(Bcolors.GREY + "The man looks up at you and smiles, then says:")
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print(
        Bcolors.WHITE + "-> 'Pale blue dot. It's just a pale, blue dot.'" + Bcolors.ENDC
    )
elif chooseDirection == "south":
    print("You travel south, to the Hall of Chemistry.")
elif chooseDirection == "west":
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print("You travel west, to the Hall of Mathematics.")
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print(Bcolors.GREY + "Two men are standing near a chalkboard, debating.")
    print(Bcolors.GREY + "One of the men looks up at you and says:")
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print(
        Bcolors.WHITE + "-> 'Hello, I'm Euclid. And this is Pythagoras.'" + Bcolors.ENDC
    )
elif chooseDirection == "north":
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print("You travel north, to the Astronomer's Lodge.")
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print(Bcolors.GREY + "Something smells like it was recently burning.")
    print(Bcolors.GREY + "Einstein smiles in your direction and says:")
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print(
        Bcolors.WHITE
        + "-> 'Hello, I'm not sure you should be here. But what's done is done.'"
        + Bcolors.ENDC
    )
elif chooseDirection == "down":
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print(Bcolors.GREY + "You open the trap door and travel down, to the Cloud Room")
    print(Bcolors.GREY + "" + Bcolors.ENDC)
    print(Bcolors.WHITE + "Cloud Service 1")
    print(Bcolors.WHITE + "Cloud Service 2")
    print(Bcolors.WHITE + "Cloud Service 3")
else:
    print("Please enter east, west, north, or south")
    chooseDirection = input(
        Bcolors.CYAN
        + "Enter a command, explorer. "
        + Bcolors.SOFTWHITE
        + "-> "
        + Bcolors.ENDC
    )

print(Bcolors.GREY + "..." + Bcolors.ENDC)
chooseDirection = input(
    Bcolors.CYAN
    + "Enter a command, explorer. "
    + Bcolors.SOFTWHITE
    + "-> "
    + Bcolors.ENDC
)

print(Bcolors.SOFTGREY + "..." + Bcolors.ENDC)
print(Bcolors.SOFTGREY + "..." + Bcolors.ENDC)
print(
    Bcolors.WHITE
    + "Thank you for using"
    + Bcolors.SOFTCYAN
    + " "
    + "SpacePy"
    + Bcolors.WHITE
    + "."
    + Bcolors.ENDC
)
print(Bcolors.SOFTBLUE + "www.spaceelements.com" + Bcolors.ENDC)
print(Bcolors.SOFTGREY + "..." + Bcolors.ENDC)
print(Bcolors.SOFTGREY + "..." + Bcolors.ENDC)
