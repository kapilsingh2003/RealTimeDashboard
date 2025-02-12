import tailer
import threading

LOG_FILE = "response_times.log"
response_times = []  # Shared list to store response times

def read_logs():
    """Reads the log file continuously and updates the response_times list."""
    for line in tailer.follow(open(LOG_FILE, "r")):
        if "Response Time" in line:
            try:
                response_time = int(line.split("Response Time:")[1].strip().replace("ms", ""))
                response_times.append(response_time)  # Store in shared list
            except ValueError:
                continue

def start_log_reader():
    """Runs log reader in a separate thread."""
    thread = threading.Thread(target=read_logs, daemon=True)
    thread.start()
