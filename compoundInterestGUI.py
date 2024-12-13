import tkinter as tk
from tkinter import messagebox

class CompoundInterestCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Compound Interest Calculator")
        
        # Principal
        self.principal_label = tk.Label(root, text="Principal Amount:")
        self.principal_label.grid(row=0, column=0)
        self.principal_entry = tk.Entry(root)
        self.principal_entry.grid(row=0, column=1)
        
        # Rate
        self.rate_label = tk.Label(root, text="Interest Rate (%):")
        self.rate_label.grid(row=1, column=0)
        self.rate_entry = tk.Entry(root)
        self.rate_entry.grid(row=1, column=1)
        
        # Time
        self.time_label = tk.Label(root, text="Time (years):")
        self.time_label.grid(row=2, column=0)
        self.time_entry = tk.Entry(root)
        self.time_entry.grid(row=2, column=1)
        
        # Calculate Button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_interest)
        self.calculate_button.grid(row=3, column=0, columnspan=2)
        
        # Result
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2)
    
    def calculate_interest(self):
        try:
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get())
            time = int(self.time_entry.get())
            
            if principal <= 0 or rate <= 0 or time <= 0:
                raise ValueError("All values must be greater than zero.")
            
            total = principal * pow((1 + rate / 100), time)
            self.result_label.config(text=f"Balance after {time} year(s): ${total:.2f}")
        
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CompoundInterestCalculator(root)
    root.mainloop()
