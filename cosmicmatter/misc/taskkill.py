import os
import subprocess

# Kill OneDrive
os.system(r"taskkill /F /IM OneDrive.exe")

# Kill Microsoft Teams (fat client)
os.system(r"taskkill /F /IM Teams.exe")

# Kill Microsoft Teams (Windows Apps version - thin'ish client)
os.system(r"taskkill /F /IM msteams.exe")

# Popen doesn't work either as script hangs after explorer kill (see attemps / notes below)
# subprocess.Popen("TASKKILL /f /im explorer.exe")
# subprocess.Popen("explorer.exe")

###########################################################################
# The below code doesn't work correctly. The issue in Windows 10/11 is    #
# that the SysTray keeps the killed icons present until you hover over    #
# them with the mouse. Worked on this for a couple of hours but have lost #
# interest for the moment                                                 #
###########################################################################

# This seems to be required to kill lingering icons in Windowsr
# Taskbar Corner and Taskbar Corner Overflow
#
# os.system(r"taskkill /f /im explorer.exe")
# os.system(r"explorer.exe")

# import subprocess
# consider subprocess.Popen

# Note: I tried the below wihout the /f switch, which will allow the python process to continue
# but it doesn't kill windows explorer...
# subprocess.call([r"TASKKILL /f /im explorer.exe"])

# Note: it's not necessary to use the r process to convert it to a string literal
# subprocess.call("TASKKILL /f /im explorer.exe")

# This was my attempt at calling a second python file in hopes that the main python
# script would continue to run. Doesn't work.
# subprocess.call("C:\\Users\\space\\AppData\\Local\\Programs\\Python\\Python310\\python.exe C:\\Users\\space\\Documents\\GitHub\\spacepy\\Misc\\killexplorer.py")

# Can't ever get to this point due to explorer killing the python process
# Note that print won't work either
# print("I'm lost in the matrix.")
# subprocess.call("explorer.exe")

# Interesting approaches I found on StackOverflow
# subprocess.call(['taskkill', '/F', '/T', '/PID', str(p.pid)])
# subprocess.call([r"C:\Windows\SysWOW64\taskkill /f /im explorer.exe"])

# I thought that potentially systray.exe might force a refresh... nope
# subprocess.call([r'systray.exe'])
# subprocess.call([r'explorer.exe'])
