import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        self.time_label = tk.Label(root, text="Enter time (hh:mm:ss):")
        self.time_label.pack()
        
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()
        
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack()
        
        self.resume_button = tk.Button(root, text="Resume Timer", command=self.resume_timer, state=tk.DISABLED)
        self.resume_button.pack()
        
        self.clear_button = tk.Button(root, text="Clear Timer", command=self.clear_timer)
        self.clear_button.pack()
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()
        
        self.time_display = tk.Label(root, text="", font=('Arial', 24))
        self.time_display.pack()
        
        self.time_left = 0
        self.paused = False
    
    def start_timer(self):
        try:
            time_str = self.time_entry.get()
            h, m, s = map(int, time_str.split(':'))
            self.time_left = h * 3600 + m * 60 + s
            if self.time_left <= 0:
                raise ValueError("Time must be greater than zero.")
            self.paused = False
            self.update_timer()
            self.resume_button.config(state=tk.DISABLED)
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
    
    def update_timer(self):
        if self.time_left > 0 and not self.paused:
            hours = self.time_left // 3600
            minutes = (self.time_left % 3600) // 60
            seconds = self.time_left % 60
            self.time_display.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.time_display.config(text="Time's Up!")
            messagebox.showinfo("Countdown Timer", "Time's Up!")
    
    def resume_timer(self):
        self.paused = False
        self.update_timer()
        self.resume_button.config(state=tk.DISABLED)
    
    def clear_timer(self):
        self.paused = True
        self.time_left = 0
        self.time_display.config(text="")
        self.time_entry.delete(0, tk.END)
        self.resume_button.config(state=tk.DISABLED)
    
    def pause_timer(self):
        self.paused = True
        self.resume_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
