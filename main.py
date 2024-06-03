import time
from kaspersmicrobit import KaspersMicrobit
import datetime

# Get the current time
current_time = datetime.datetime.now()

# Add 1 minute to the current time
future_time = current_time + datetime.timedelta(minutes=1)

# Format the future time as hour:minute
future_time_string = future_time.strftime("%H:%M")

# Print the future time
print(future_time_string)

tasks = {
   future_time.strftime("%H:%M") : "Start presentation",
   (future_time + datetime.timedelta(minutes=1) ).strftime("%H:%M") : "Finish presentation",
}

def print_received_string(string: str):
    if "omplete" in string:
        first_task = next(iter(tasks.items()))
        tasks.pop(first_task[0])
        print(f"Received from microbit: '{string}'")
        print(f"Tasks: {tasks}")
        microbit.uart.send_string(first_task[0] + "..." + first_task[1] +  "\n")
        print(f"Sent to microbit: '{first_task[0] + '...' + first_task[1] }'")
    if "time" in string:
        print(f"Received from microbit: '{string}'")
        microbit.uart.send_string(f"{datetime.datetime.now().strftime('%H:%M:%S')}\n")
        print(f"Sent to microbit: '{datetime.datetime.now().strftime('%H:%M:%S')}\n'")

with KaspersMicrobit.find_one_microbit() as microbit:        
    while True:
        # listen for strings sent by the micro:bit / luister naar tekst die verzonden wordt door de micro:bit
        microbit.uart.receive_string(print_received_string)
        time.sleep(20)
