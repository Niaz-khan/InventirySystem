# InventirySystem

## Overview

This Python script implements a basic inventory management system using SQLite3 for data storage. The system consists of two primary classes:

Item: Represents an individual item with attributes for name, price, and quantity.
Inventory: Manages a collection of items, providing functionalities to add items, update stock, display inventory, and check stock levels.
## Key Features:

Adds items to the inventory with details like name, price, and quantity.
Updates item details (name, price, quantity) based on item ID.
Displays a list of all items with their details.
Checks inventory levels and provides alerts for low stock items.
Uses SQLite3 for persistent data storage.
## Dependencies:

## sqlite3
### How to Use:

Ensure you have Python and the sqlite3 library installed.
Run the Python script.
Follow the on-screen prompts to add items, update stock, display inventory, or check stock levels.
## Database:

The script creates a SQLite database named Inventory.db to store item information. The database schema includes an Items table with columns for Item_ID, it_name, it_price, and it_quantity.

## Limitations:

Basic functionality without advanced features like user authentication, search, or reporting.
Limited error handling.
Does not handle item removal or deletion.
## Future Improvements:

Implement user authentication and authorization.
Add search functionality for items.
Include features for generating reports and analytics.
Enhance error handling and user feedback.
Consider using a more robust database system for larger-scale applications.
## Contributing:

Contributions are welcome! Feel free to fork the repository and submit pull requests.

### License:
MIT
## Contact:
### Niaz khan
momandniazkhan@gmail.com
