import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

def update_time():
    try:
        selected_timezone = timezone_var.get()
        tz = pytz.timezone(selected_timezone)
        time_now = datetime.now(tz)
        formatted_time = time_now.strftime('%I:%M:%S %p')  # 12-hour with AM/PM
        formatted_date = time_now.strftime('%A, %d %B %Y')
        time_label.config(text=formatted_time)
        date_label.config(text=formatted_date)
    except Exception as e:
        time_label.config(text="Error")
        date_label.config(text=str(e))
    root.after(1000, update_time)

# Create main window
root = tk.Tk()
root.title("World Clock")
root.geometry("700x400")
root.configure(bg='black')

# Title label
title_label = tk.Label(root, text="World Clock", font=('Arial', 32, 'bold'), fg='white', bg='black')
title_label.pack(pady=10)

# Dropdown for selecting timezone
timezone_var = tk.StringVar()
timezone_dropdown = ttk.Combobox(root, textvariable=timezone_var, width=50, font=('Arial', 12))
timezone_dropdown['values'] = pytz.all_timezones
timezone_dropdown.current(pytz.all_timezones.index('Asia/Kolkata'))  # Default timezone
timezone_dropdown.pack(pady=10)

# Time label
time_label = tk.Label(root, font=('Arial', 48), fg='cyan', bg='black')
time_label.pack(pady=10)

# Date label
date_label = tk.Label(root, font=('Arial', 20), fg='white', bg='black')
date_label.pack(pady=5)

# Start clock
update_time()

# Run GUI
root.mainloop()