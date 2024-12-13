import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), command=self.clear).grid(row=row_val, column=0)
    
    def click_event(self, key):
        if key == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            self.entry.insert(tk.END, key)
    
    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
