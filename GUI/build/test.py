import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

LOG_FILE = "response_times.log"
response_times = []
timestamps = []

def read_last_response_time():
    """Reads the last response time from the log file."""
    try:
        with open(LOG_FILE, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                if "Response Time" in last_line:
                    response_time = int(last_line.split("Response Time:")[1].strip().replace("ms", ""))
                    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                    return timestamp, response_time
    except FileNotFoundError:
        pass
    return None, None

def update_ui():
    """Fetch new response time, update UI labels and graph with a moving window."""
    timestamp, new_response_time = read_last_response_time()
    if new_response_time is not None:
        response_times.append(new_response_time)
        timestamps.append(timestamp)

        # Keep only the last 10 seconds of data
        if len(response_times) > 10:
            response_times.pop(0)
            timestamps.pop(0)

        # Update Labels
        response_label.config(text=f"Latest Response Time: {new_response_time} ms")
        avg_time = sum(response_times) / len(response_times)
        avg_label.config(text=f"Average Response Time: {avg_time:.2f} ms")

        # Update Graph
        ax.clear()
        ax.plot(timestamps, response_times, marker="o", linestyle="-", color="blue")
        ax.set_title("Response Time Trend (Last 10 sec)")
        ax.set_xlabel("Time (HH:MM:SS)")
        ax.set_ylabel("Response Time (ms)")
        ax.set_xticklabels(timestamps, rotation=45)  # Rotate X-axis labels for better readability
        ax.grid(True)
        canvas.draw()

    # Call this function again after 1000ms (1 second)
    root.after(1000, update_ui)

# Initialize Tkinter Window
root = tk.Tk()
root.title("Real-Time Log Dashboard")
root.geometry("700x500")
print(response_times)

# Labels for displaying response times
response_label = ttk.Label(root, text="Latest Response Time: -- ms", font=("Arial", 14))
response_label.pack(pady=10)

avg_label = ttk.Label(root, text="Average Response Time: -- ms", font=("Arial", 14))
avg_label.pack(pady=10)

# Matplotlib Figure
fig, ax = plt.subplots(figsize=(6, 3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=20)

# Start UI updates
update_ui()

# Run Tkinter main loop
root.mainloop()
