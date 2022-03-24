import os
import subprocess
# add current Windows user profile to below variable
userProfile = "space"

# add desired application file paths here to start
oneDrive = "C:\\Users\\" + userProfile + "\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe"
thinTeams = "C:\\Users\\space\\AppData\\Local\\Microsoft\\WindowsApps\\msteams.exe"
fatTeams = "C:\\Program Files (x86)\\Teams Installer\\Teams.exe"

# Open Microsoft Teams (Windows Apps version - thin'ish client)
os.startfile(thinTeams)
# Previous attempts below
# os.system("\"C:\\Users\\space\\AppData\\Local\\Microsoft\\WindowsApps\\msteams.exe\"")
# os.startfile("\"C:\\Users\\space\\AppData\\Local\\Microsoft\\WindowsApps\\msteams.exe\"")
# subprocess.Popen([r"C:\\Users\\space\\AppData\\Local\\Microsoft\\WindowsApps\\msteams.exe"])
# subprocess.Popen([r"C:\\Users" + userProfile + "AppData\\Local\\Microsoft\\WindowsApps\\msteams.exe"])

# Open Microsoft Teams (fat client)
os.startfile(fatTeams)
# Previous attempts below
# os.system("\"C:\\Program Files (x86)\\Teams Installer\\Teams.exe\"")
# subprocess.Popen([r"C:\\Program Files (x86)\\Teams Installer\\Teams.exe"])

# Open OneDrive
os.startfile(oneDrive)
# Previous attempts below
# subprocess.Popen([r"C:\\Users\\space\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe"])
# subprocess.Popen([r"C:\\Users" + userProfile + "\\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe"])
# os.system(r"C:\\Users\\space\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe")
# os.startfile(r"C:\\Users\\space\AppData\\Local\\Microsoft\\OneDrive\\OneDrive.exe")
exit()