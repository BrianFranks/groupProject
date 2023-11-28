import sqlite3
import sys
import Inventory
import User2
import Cart
import database

#DATABASE SETUP

invInst = Inventory.Inventory("digitalStore", "Inventory")
UserInst = User2.User("digitalStore", "")
CartInst = Cart.Cart()



invInst.viewInventory()

choice = -1
while choice != 0:
    if not(User2.User.getLoggedIn()):
        choice = input("Would you like to \n 0: exit program\n1: login\n2: create account")
        if choice == "1":
            User2.User.getLoggedIn()
        if choice == "2":
            User2.User.createAccount()
    if User2.User.getLoggedIn():
        choice



#databaseName = input("Database Name: ")
#tableName = input("Table Name: ")
