import time
from win10toast import ToastNotifier

while True:
    toaster = ToastNotifier()
    time.sleep("interval in minutes" * 60) #//reminder interval in seconds
    toaster.show_toast("your desired message 1", "your desired message 2", duration = 12, threaded = True)
    
while toaster.notification_active:
    time.sleep(0.2)

