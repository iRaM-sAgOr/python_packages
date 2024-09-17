#!/usr/bin/python

import speedtest
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Global variables to control the test loop and store results
running = False
results = []


def get_internet_speed():
    st = speedtest.Speedtest()
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Update the status label
    status_label.config(text="Finding the best server...")
    root.update()
    st.get_best_server()

    # Perform speed tests and update labels accordingly
    status_label.config(text="Performing download speed test...")
    root.update()
    download_speed = st.download() / 1_000_000  # Convert to Mbps

    status_label.config(text="Performing upload speed test...")
    root.update()
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    status_label.config(text="Performing Ping speed test...")
    root.update()
    ping_speed = st.results.ping

    # Store the result in a single line and log the time
    result = "Time: {} | Download: {:.2f} Mbps | Upload: {:.2f} Mbps | Ping: {:.2f} ms".format(
        formatted_datetime, download_speed, upload_speed, ping_speed
    )

    # Add the new result to the list and keep only the last 10 results
    results.append(result)
    if len(results) > 10:
        results.pop(0)  # Remove the oldest result

    # Clear the result area and display the last 10 results
    result_text.delete(1.0, tk.END)
    for res in results:
        result_text.insert(tk.END, res + "\n")

    # Update the current status
    status_label.config(text="Test completed at {}.".format(formatted_datetime))


def toggle_test():
    global running
    if not running:
        running = True
        start_button.config(text="Stop Test", command=stop_test)
        start_test()
    else:
        stop_test()


def start_test():
    if running:
        get_internet_speed()

        # Schedule the test to run again after 5 seconds (5000 milliseconds)
        root.after(5000, start_test)


def stop_test():
    global running
    running = False
    start_button.config(text="Start Test", command=toggle_test)


def on_close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


# Create a GUI window
root = tk.Tk()
root.title("Internet Speed Test")

# Create labels for displaying information
status_label = tk.Label(
    root, text="Click 'Start' to begin the speed test", font=("Helvetica", 14)
)
status_label.pack(pady=10)

# Text widget to display the last 10 results
result_text = tk.Text(root, height=10, width=80, font=("Helvetica", 12))
result_text.pack(pady=5)

# Create a button to start/stop the test
start_button = tk.Button(
    root, text="Start Test", command=toggle_test, font=("Helvetica", 12)
)
start_button.pack(pady=20)

# Handle the window close event
root.protocol("WM_DELETE_WINDOW", on_close)

# Start the GUI event loop
root.mainloop()
