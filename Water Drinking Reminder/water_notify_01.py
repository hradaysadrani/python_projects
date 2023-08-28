import time
from plyer import notification

notification.notify(
    title = "My Friend, please drink Water",
    message = "Thak gaye hoge, Paani pe lo"
)

h1 = int(time.strftime('%H'))

while True:
    current_hour = int(time.strftime('%H'))
    
    if current_hour != h1:
        notification.notify(
            title="Drink Water",
            message="Thak gaye hoge, Paani pe lo"
        )
        break
    
    time.sleep(3600)  
    

