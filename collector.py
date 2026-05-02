import psutil
import pandas as pd
import time
import os

file = "data.csv"

# Create dataset if not exists
if not os.path.exists(file):
    df = pd.DataFrame(columns=[
        "cpu", "ram", "battery", "plugged",
        "processes", "net_sent", "net_recv",
        "top_cpu", "context", "drain"
    ])
    df.to_csv(file, index=False)

# Auto context detection
def get_context():
    try:
        for p in psutil.process_iter(['name']):
            name = p.info['name']
            if name:
                name = name.lower()

                if "chrome" in name or "edge" in name:
                    return "browsing"
                elif "code" in name or "pycharm" in name:
                    return "coding"
                elif "valorant" in name or "steam" in name or "game" in name:
                    return "gaming"
    except:
        pass

    return "idle"

# Get top CPU-consuming process
def get_top_process_cpu():
    max_cpu = 0
    try:
        for p in psutil.process_iter(['cpu_percent']):
            cpu = p.info['cpu_percent']
            if cpu and cpu > max_cpu:
                max_cpu = cpu
    except:
        pass
    return max_cpu

prev_battery = psutil.sensors_battery().percent
prev_time = time.time()
prev_net = psutil.net_io_counters()

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery().percent
    plugged = int(psutil.sensors_battery().power_plugged)

    processes = len(psutil.pids())

    net = psutil.net_io_counters()
    net_sent = net.bytes_sent - prev_net.bytes_sent
    net_recv = net.bytes_recv - prev_net.bytes_recv
    prev_net = net

    top_cpu = get_top_process_cpu()
    context = get_context()

    # Better drain calculation (per minute)
    current_time = time.time()
    time_diff = (current_time - prev_time) / 60
    drain = (prev_battery - battery) / max(time_diff, 0.01)

    prev_battery = battery
    prev_time = current_time

    row = pd.DataFrame([[
        cpu, ram, battery, plugged,
        processes, net_sent, net_recv,
        top_cpu, context, drain
    ]],
    columns=[
        "cpu", "ram", "battery", "plugged",
        "processes", "net_sent", "net_recv",
        "top_cpu", "context", "drain"
    ])

    row.to_csv(file, mode='a', header=False, index=False)

    print(f"Saved | CPU={cpu}% | Context={context} | Drain={drain:.4f}")

    time.sleep(15)