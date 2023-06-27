import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Notification",
            message="Hey Bibek Drink Water",
            timeout=10
        )
        time.sleep(60*30)  
