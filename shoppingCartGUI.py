import tkinter as tk
from tkinter import messagebox

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart")
        
        self.foods = []
        self.prices = []
        
        self.food_label = tk.Label(root, text="Enter a food to buy:")
        self.food_label.pack()
        
        self.food_entry = tk.Entry(root)
        self.food_entry.pack()
        
        self.price_label = tk.Label(root, text="Enter the price of the food:")
        self.price_label.pack()
        
        self.price_entry = tk.Entry(root)
        self.price_entry.pack()
        
        self.add_button = tk.Button(root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack()
                
        self.cart_button = tk.Button(root, text="Show Cart", command=self.show_cart)
        self.cart_button.pack()
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()
        
        self.total_label = tk.Label(root, text="")
        self.total_label.pack()
    
    def add_to_cart(self):
        food = self.food_entry.get()
        try:
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid price.")
            return
        
        self.foods.append(food)
        self.prices.append(price)
        
        self.food_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
    
    def show_cart(self):
        cart_details = "-----------------YOUR CART---------------\n"
        total = 0
        
        for food, price in zip(self.foods, self.prices):
            cart_details += f"{food}: ${price:.2f}\n"
            total += price
        
        cart_details += f"\nYour total is: ${total:.2f}"
        self.total_label.config(text=cart_details)

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
