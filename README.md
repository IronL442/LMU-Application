# Inventory Management System

## Overview
This Inventory Management System is a simple GUI-based application developed in Python using the Tkinter library. It allows users to manage a basic inventory of products including adding new products, selling products, restocking products, and viewing transactions. The system also provides financial calculations like total revenue, total costs, inventory value, and total profit.

## Features
- Add new products to the inventory.
- Sell products and update inventory accordingly.
- Restock products with updated purchase costs.
- View all transactions related to sales and restocking.
- Calculate total revenue, total costs, inventory value, and total profit.
- Display the value of inventory for a specific product.

## Prerequisites

- **Python**: This application requires Python 3.x. Make sure you have a Python distribution installed that includes `tkinter`. This is typically included by default in many Python installations, but if you encounter issues with `tkinter`, you may need to install it manually:
  - On Ubuntu: `sudo apt-get install python3-tk`
  - On Fedora: `sudo dnf install python3-tkinter`


## Installation
1. Clone this repository or download the source code.
2. Ensure Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

Alternatively, you can also setup a Virtual Environment.

### Setting up a Python Virtual Environment
You can set up a virtual environment by running:
```bash
python3 -m venv venv
source venv/bin/activate # On Windows use 'venv\Scripts\activate'
```

### Cloning the repository
To clone the repository to your local machine open a terminal and run the following command:
```bash
cd your-local-save-location
git clone https://github.com/IronL442/LMU-Application.git
cd LMU-Application
```

## Running the Application
If you are a Windows user, just start the app.exe file to run this application.

Alternatively, to run this application, navigate to the directory containing the script and run the following command:
```bash
python inventory_system.py
```

## How to Use
Start the application following the steps specified above.
Use the GUI buttons to interact with the inventory system:
- Show Inventory: Displays current inventory.
- Add Product: Adds a new product to the inventory.
- Sell Product: Sells a specified quantity of a product.
- Restock Product: Restocks a specified quantity of a product.
- Show Transactions: Displays a log of all transactions.
- Calculate Totals: Allows selection from several financial calculations.
- Show Product Value: Displays the inventory value of a specified product.

### Acknowledgements
- This project uses the Tkinter library for the GUI implementation, which is part of Python's standard library.
- Random data generation for initial inventory setup is achieved using Python's random module.
