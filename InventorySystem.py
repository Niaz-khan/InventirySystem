"""
Inventory Management System
- Develop an `Item` class with attributes for name, price, and stock quantity.
- Create an `Inventory` class that can add items, update stock, and display all items.
- Include methods for checking stock levels and generating restock alerts.
"""
import sqlite3 as sql
import Item


class Inventory:
    def __init__(self):
        self.con = sql.connect("Inventory.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("""
        create table if not exists Items(Item_ID integer primary key autoincrement,
        it_name text,
        it_price real,
        it_quantity integer)""")
        self.stock = []

    def add_item(self, item):
        self.cursor.execute("""
        insert into Items(it_name, it_price, it_quantity) values (?, ?, ?)""",
                            (item.item_name, item.price, item.quantity))
        self.con.commit()

    def update_stock(self):
        if self.stock:
            print("1 --> update name of the item\n2 --> update price\n3 --> update "
                  "quantity.".title())
            choice = input(":) ")
            if choice == '1':
                name = input("what will be the name of item.")
                self.stock[0] = name
            elif choice == '2':
                price = float(input("enter the amount:) "))
                self.stock[1] = price
            elif choice == '3':
                quan = input("enter the quantity:) ")
                self.stock[2] = quan
            else:
                print("invalid input")

        else:
            print("you have nothing in the stock.".title())
        self.con.commit()

    def display_items(self):
        """this function fetch all the data from data base and print it."""

        self.cursor.execute("""
        select * from Items
        """)
        data_list = self.cursor.fetchall()
        print("Item_no\titem_name\titem_price\titem_quantity".upper())
        for row in data_list:
            print(f"|{row[0]}\t\t|{row[1]}\t\t|  {row[2]}\t\t|  {row[3]}")
        print("\n\n")

    def check_inventory_levels(self):
        if self.stock:
            if self.stock[2] <= 10:
                print("You have to add more quantity of item.")
            else:
                print("You have enough stock")
        else:
            print("Hurry you have nothing in inventory")


