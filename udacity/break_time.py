import webbrowser
import time
breaks = 0
current_time = time.ctime()
while breaks < 3:
    print('This program started on' + current_time)
    time.sleep(10)
    webbrowser.open("http://openpuppies.com/#jHj0VTa")
    breaks += 1