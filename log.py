import time
from datetime import datetime

start_time = time.time()
duration = 5 * 60  # 5 minutes in seconds

while time.time() - start_time < duration:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)  # wait 1 second
