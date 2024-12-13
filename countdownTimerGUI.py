import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        self.time_label = tk.Label(root, text="Enter time in seconds:")
        self.time_label.pack()
        
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()
        
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack()
        
        self.time_display = tk.Label(root, text="", font=('Arial', 24))
        self.time_display.pack()
        
        self.time_left = 0
    
    def start_timer(self):
        try:
            self.time_left = int(self.time_entry.get())
            if self.time_left <= 0:
                raise ValueError("Time must be greater than zero.")
            self.update_timer()
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
    
    def update_timer(self):
        if self.time_left > 0:
            hours = self.time_left // 3600
            minutes = (self.time_left % 3600) // 60
            seconds = self.time_left % 60
            self.time_display.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.time_display.config(text="Time's Up!")
            messagebox.showinfo("Countdown Timer", "Time's Up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
