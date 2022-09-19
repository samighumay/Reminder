import time
from win10toast import ToastNotifier

while True:
    toaster = ToastNotifier()
    time.sleep(2)
    toaster.show_toast("Hey Kid", "Lol you are single", duration=12, threaded=True)
    
while toaster.notification_active:
    time.sleep(0.2)

