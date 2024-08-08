"""
Inventory Management System
- Develop an `Item` class with attributes for name, price, and stock quantity.
- Create an `Inventory` class that can add items, update stock, and display all items.
- Include methods for checking stock levels and generating restock alerts.
"""
import sqlite3 as sql


class Inventory:
    def __init__(self):
        self.con = sql.connect("Inventory.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("""
        create table if not exists Items(Item_ID integer primary key autoincrement,
        it_name text,
        it_price real,
        it_quantity integer)""")

    def add_item(self, item):
        try:
            self.cursor.execute(
                """ insert into Items(it_name, it_price, it_quantity) values (?, ?, ?)""",
                (item.item_name, item.price, item.quantity))
            self.con.commit()
        except sql.Error as e:
            print(f"Error: {e}")

    def update_stock(self):
        """
        this method will show all items if available  then update name, price and quantity of
        the item using item_ID
        """
        self.display_items()
        item_id = input("Enter the ID of the item to update:) ")
        name = input("Enter the new name (or press enter to skip):) ")
        price = input("Enter the new price (or press enter to skip):) ")
        quantity = input("Enter the new quantity (or press enter to skip):) ")

        if name:
            self.cursor.execute(""" update Items set it_name = ? where Item_ID = ?""",
                                (name, item_id))
        if price:
            self.cursor.execute(""" update Items set it_price = ? where Item_ID = ?""",
                                (price, item_id))
        if quantity:
            self.cursor.execute(""" update Items set it_quantity = ? where Item_ID = ?""",
                                (quantity, item_id))

        self.con.commit()

    def display_items(self):
        """
        this function fetch all the data from database and print it.
        """

        try:
            self.cursor.execute(""" select * from Items """)
            data_list = self.cursor.fetchall()
            print("Item_no\titem_name\titem_price\titem_quantity".upper())
            for row in data_list:
                print(f"|{row[0]}\t\t|{row[1]}\t\t| {row[2]}\t\t| {row[3]}")
            print("\n\n")
        except sql.Error as e:
            print(f"Error: {e}")

    def check_inventory_levels(self):
        try:
            self.cursor.execute(""" select * from Items """)
            data_list = self.cursor.fetchall()
            for row in data_list:
                if row[3] <= 10:
                    print(f"You have to add more quantity of {row[1]}.")
                else:
                    print(f"You have enough stock of {row[1]}.")
        except sql.Error as e:
            print(f"Error: {e}")
