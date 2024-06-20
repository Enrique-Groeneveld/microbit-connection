# Add code to automatically download the latest version of the kaspersmicrobit library if it is not installed
try:
    import kaspersmicrobit
except ImportError:
    import os
    os.system("pip install kaspersmicrobit")

import time
from kaspersmicrobit import KaspersMicrobit
import datetime
import json




# Get the current time
current_time = datetime.datetime.now()

# Add 1 minute to the current time
future_time = current_time + datetime.timedelta(minutes=1)

# Format the future time as hour:minute
future_time_string = future_time.strftime("%H:%M")

# Print the future time
print(future_time_string)

def print_received_string(string: str):
    # Load tasks from a JSON file
    print(string)
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)
    
    if "omplete" in string or "started" in string:
        if tasks:
            first_task = next(iter(tasks.items()))
            tasks.pop(first_task[0])
            print(f"Received from microbit: '{string}'")
            print(f"Tasks: {tasks}")
            microbit.uart.send_string(first_task[0] + "..." + first_task[1] +  "\n")
            print(f"Sent to microbit: '{first_task[0] + '...' + first_task[1] }'")

            # Write the updated tasks back to the JSON file
            with open('tasks.json', 'w') as f:
                json.dump(tasks, f)
        else:
            print("No tasks left.")
            microbit.uart.send_string(f"54\n")


    if "time" in string:
        print(f"Received from microbit: '{string}'")
        microbit.uart.send_string(f"{datetime.datetime.now().strftime('%H:%M:%S')}\n")
        print(f"Sent to microbit: '{datetime.datetime.now().strftime('%H:%M:%S')}\n'")
    
    if "stop" in string or "king" in string:
        print("Stopped working")
        microbit.uart.send_string(f"54\n")
        # exit()

with KaspersMicrobit.find_one_microbit() as microbit:        
    while True:
        # listen for strings sent by the micro:bit / luister naar tekst die verzonden wordt door de micro:bit
        microbit.uart.receive_string(print_received_string)
        time.sleep(20)