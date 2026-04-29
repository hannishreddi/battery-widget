import tkinter as tk
import psutil
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")

contexts = ["coding", "browsing", "gaming"]

def predict():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery().percent
    plugged = int(psutil.sensors_battery().power_plugged)

    results = []

    for ctx in contexts:
        ctx_encoded = encoder.transform([ctx])[0]

        X = np.array([[cpu, ram, battery, plugged, ctx_encoded]])
        drain = model.predict(X)[0]

        if drain <= 0:
            time_left = "∞"
        else:
            time_left = f"{battery / drain:.1f} min"

        results.append(f"{ctx.capitalize()}: {time_left}")

    label.config(text=f"Battery: {battery}%\n\n" + "\n".join(results))
    root.after(3000, predict)

# UI
root = tk.Tk()
root.title("Battery AI Widget")
root.geometry("250x150")
root.configure(bg="#1e1e1e")

label = tk.Label(root, text="Loading...",
                 fg="white", bg="#1e1e1e",
                 font=("Segoe UI", 10))
label.pack(pady=20)

predict()
root.mainloop()