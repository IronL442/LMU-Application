import tkinter as tk  # Import the tkinter library for GUI creation.
from tkinter import messagebox, simpledialog  # Import messagebox and simpledialog for user interaction dialogs.
import random  # Import random for generating random numbers.

class Product:
    def __init__(self, id, name, quantity, purchase_price, selling_price):
        self.id = id  # Unique identifier for the product.
        self.name = name  # Name of the product.
        self.quantity = quantity  # Current stock quantity of the product.
        self.purchase_price = purchase_price  # Purchase price of the product.
        self.selling_price = selling_price  # Selling price of the product.

class InventorySystem:
    def __init__(self, master):
        self.master = master  # The master tkinter widget.
        self.products = []  # List to hold all products.
        self.transactions = []  # List to log all transactions.
        self.total_revenue = 0  # Total revenue initialized to 0.
        self.total_costs = 0  # Total costs initialized to 0.
        self._initialize_products()  # Initialize the product list.
        self._create_widgets()  # Create the GUI widgets.

    def _initialize_products(self):
        for i in range(1, 11):  # Loop to create 10 initial products.
            quantity = random.randint(1, 500)  # Generate a random quantity for the product.
            purchase_price = random.randint(1, 10)  # Generate a random purchase price.
            selling_price = random.randint(10, 50)  # Generate a random selling price.
            self.products.append(Product(i, f"Product {i}", quantity, purchase_price, selling_price))  # Create a new Product and add to the list.

    def _create_widgets(self):
        self.listbox = tk.Listbox(self.master, height=12, width=100)  # Create a Listbox to show inventory and transactions.
        self.listbox.pack(pady=10)  # Pack the Listbox into the GUI.
        operations = [
            ("Show Inventory", self.show_inventory),
            ("Add Product", self.add_product),
            ("Sell Product", self.sell_product),
            ("Restock Product", self.restock_product),
            ("Show Transactions", self.show_transactions),
            ("Calculate Totals", self.prompt_for_calculation),
            ("Show Product Value", self.show_product_value)
        ]  # List of operations with corresponding methods.
        for text, command in operations:  # Loop through the operations.
            tk.Button(self.master, text=text, command=command).pack(side=tk.LEFT, padx=10)  # Create buttons for each operation and pack them.

    def show_inventory(self):  # Method to show the inventory.
        self.listbox.delete(0, tk.END)  # Clear the Listbox.
        for product in self.products:  # Loop through each product.
            self.listbox.insert(tk.END, f"ID: {product.id}, Name: {product.name}, Quantity: {product.quantity}, Purchase: ${product.purchase_price}, Selling: ${product.selling_price}")  # Insert product details into the Listbox.

    def add_product(self):  # Method to add a new product.
        name = simpledialog.askstring("Input", "Enter product name", parent=self.master)  # Prompt user for product name.
        quantity = simpledialog.askinteger("Input", "Enter quantity", parent=self.master)  # Prompt user for quantity.
        purchase_price = simpledialog.askfloat("Input", "Enter purchase price", parent=self.master)  # Prompt user for purchase price.
        selling_price = simpledialog.askfloat("Input", "Enter selling price", parent=self.master)  # Prompt user for selling price.
        if name and quantity and purchase_price and selling_price:  # Check if all inputs are valid.
            new_id = len(self.products) + 1  # Generate a new ID.
            new_product = Product(new_id, name, quantity, purchase_price, selling_price)  # Create a new product.
            self.products.append(new_product)  # Add the new product to the list.
            self.transactions.append(f"Added {quantity} of {name}")  # Log the transaction.
            self.total_costs += purchase_price * quantity  # Update the total costs.
            messagebox.showinfo("Update", "Product added successfully!")  # Show success message.

    def sell_product(self):  # Method to sell a product.
        product_id = simpledialog.askinteger("Input", "Enter product ID", parent=self.master)  # Prompt user for product ID.
        quantity = simpledialog.askinteger("Input", "Enter quantity to sell", parent=self.master)  # Prompt user for quantity to sell.
        product = next((p for p in self.products if p.id == product_id), None)  # Find the product by ID.
        if product and quantity <= product.quantity:  # Check if product exists and quantity is sufficient.
            product.quantity -= quantity  # Deduct the sold quantity from stock.
            self.transactions.append(f"Sold {quantity} of {product.name}")  # Log the transaction.
            self.total_revenue += product.selling_price * quantity  # Update the total revenue.
            messagebox.showinfo("Update", "Product sold successfully!")  # Show success message.
        else:
            messagebox.showerror("Error", "Invalid product ID or insufficient stock")  # Show error message if the sale cannot be completed.

    def restock_product(self):  # Method to restock a product.
        product_id = simpledialog.askinteger("Input", "Enter product ID", parent=self.master)  # Prompt user for product ID.
        quantity = simpledialog.askinteger("Input", "Enter quantity to restock", parent=self.master)  # Prompt user for restock quantity.
        purchase_price = simpledialog.askfloat("Input", "Enter purchase price", parent=self.master)  # Prompt user for purchase price.
        product = next((p for p in self.products if p.id == product_id), None)  # Find the product by ID.
        if product:  # Check if the product exists.
            product.quantity += quantity  # Add the restocked quantity to stock.
            self.transactions.append(f"Restocked {quantity} of {product.name} at purchase price ${purchase_price}")  # Log the transaction.
            self.total_costs += purchase_price * quantity  # Update the total costs.
            messagebox.showinfo("Update", "Product restocked successfully!")  # Show success message.
        else:
            messagebox.showerror("Error", "Invalid product ID")  # Show error message if the product ID is invalid.

    def show_transactions(self):  # Method to show transactions.
        self.listbox.delete(0, tk.END)  # Clear the Listbox.
        for transaction in self.transactions:  # Loop through each transaction.
            self.listbox.insert(tk.END, transaction)  # Insert transaction details into the Listbox.

    def prompt_for_calculation(self):  # Method to prompt user for a financial calculation.
        options = {"1": "Total Revenue", "2": "Total Costs", "3": "Inventory Value", "4": "Total Profit"}  # Dictionary of calculation options.
        option = simpledialog.askstring("Input", "Choose calculation:\n1: Total Revenue\n2: Total Costs\n3: Inventory Value\n4: Total Profit")  # Prompt user to choose a calculation.
        if option in options:  # Check if the option is valid.
            if option == "1":
                messagebox.showinfo("Calculation", f"Total Revenue: ${self.total_revenue}")  # Display total revenue.
            elif option == "2":
                messagebox.showinfo("Calculation", f"Total Costs: ${self.total_costs}")  # Display total costs.
            elif option == "3":
                total_value = sum(p.purchase_price * p.quantity for p in self.products)  # Calculate total inventory value.
                messagebox.showinfo("Calculation", f"Inventory Value: ${total_value}")  # Display inventory value.
            elif option == "4":
                total_profit = self.total_revenue - self.total_costs  # Calculate total profit.
                messagebox.showinfo("Calculation", f"Total Profit: ${total_profit}")  # Display total profit.
        else:
            messagebox.showerror("Error", "Invalid Option")  # Show error message if the option is invalid.

    def show_product_value(self):  # Method to show the inventory value of a specific product.
        product_id = simpledialog.askinteger("Input", "Enter product ID", parent=self.master)  # Prompt user for product ID.
        product = next((p for p in self.products if p.id == product_id), None)  # Find the product by ID.
        if product:  # Check if the product exists.
            inventory_value = product.purchase_price * product.quantity  # Calculate inventory value of the product.
            messagebox.showinfo("Product Value", f"Inventory Value for {product.name}: ${inventory_value}")  # Display inventory value.
        else:
            messagebox.showerror("Error", "Invalid product ID")  # Show error message if the product ID is invalid.

if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window.
    root.title("Inventory System")  # Set the window title.
    app = InventorySystem(root)  # Instantiate the InventorySystem class with the main window.
    root.mainloop()  # Start the Tkinter event loop.