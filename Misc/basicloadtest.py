# very basic load test
# import webbrowser
import time

count = 0
while count < 22:
    print(count)
    webbrowser.open('https://www.someurlhere.com', new=2, autoraise=True)
    count += 1
    time.sleep(1.3) # Seconds 



