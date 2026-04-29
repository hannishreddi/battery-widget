import psutil
import pandas as pd
import time
import os

file = "data.csv"

if not os.path.exists(file):
    df = pd.DataFrame(columns=["cpu", "ram", "battery", "plugged", "context", "drain"])
    df.to_csv(file, index=False)

print("Enter context: coding / browsing / gaming")
context = input("Context: ")

prev_battery = psutil.sensors_battery().percent

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery().percent
    plugged = int(psutil.sensors_battery().power_plugged)

    drain = prev_battery - battery  # battery drop
    prev_battery = battery

    row = pd.DataFrame([[cpu, ram, battery, plugged, context, drain]],
                       columns=["cpu", "ram", "battery", "plugged", "context", "drain"])

    row.to_csv(file, mode='a', header=False, index=False)

    print(f"Saved: CPU={cpu}, Drain={drain}")
    time.sleep(60)