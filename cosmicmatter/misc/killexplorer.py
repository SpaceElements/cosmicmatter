import subprocess

subprocess.call('TASKKILL /f /im explorer.exe" & start explorer.exe')
# subprocess.call("TASKKILL /f /im explorer.exe & start "" '%windir%\\explorer.exe'")
subprocess.call(["explorer.exe"])
