import tkinter as tk
import psutil
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

contexts = ["coding", "browsing", "gaming", "idle"]

# Top CPU process
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

def predict():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery().percent
    plugged = int(psutil.sensors_battery().power_plugged)

    processes = len(psutil.pids())

    net = psutil.net_io_counters()
    net_sent = net.bytes_sent
    net_recv = net.bytes_recv

    top_cpu = get_top_process_cpu()

    results = []

    for ctx in contexts:
        try:
            ctx_encoded = encoder.transform([ctx])[0]
        except:
            continue

        X = np.array([[
            cpu, ram, battery, plugged,
            processes, net_sent, net_recv,
            top_cpu, ctx_encoded
        ]])

        drain = model.predict(X)[0]

        if drain <= 0.01:
            time_left = "Calculating..."
        else:
            time_left = f"{battery / drain:.1f} min"

        results.append(f"{ctx.capitalize()}: {time_left}")

    label.config(text=f"🔋 Battery: {battery}%\n\n" + "\n".join(results))

    root.after(3000, predict)

# UI
root = tk.Tk()
root.title("Battery AI Widget")
root.geometry("260x180")
root.configure(bg="#1e1e1e")

label = tk.Label(
    root,
    text="Loading...",
    fg="white",
    bg="#1e1e1e",
    font=("Segoe UI", 10)
)
label.pack(pady=20)

predict()
root.mainloop()