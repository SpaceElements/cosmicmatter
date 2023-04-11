import os
import time
import winsound
import ctypes

last_file_time = time.time()

while True:
    # Check if a new file has been created within the last 100 seconds
    files = os.listdir('.')
    newest_file_time = max(os.stat(f).st_mtime for f in files if os.path.isfile(f))
    if newest_file_time > last_file_time:
        last_file_time = newest_file_time
    else:
        # Play alert sound and display message box
        winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
        ctypes.windll.user32.MessageBoxW(None, 'No new files created within the last 100 seconds. Click OK to acknowledge.', 'File Alert', 0x40)
    time.sleep(1)
