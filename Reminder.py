import time
from win10toast import ToastNotifier

if __name__ == "__main__":
    toaster = ToastNotifier()
    while True:
        toaster.show_toast("Notification", "Hey Bibek, drink water", duration=10)
        time.sleep(60*30)  
