import sqlite3
import sys
import Inventory
import User2
import Cart
#import database

#DATABASE SETUP

invInst = Inventory.Inventory("digitalStore", "Inventory")
UserInst = User2.User("digitalStore", "User")
CartInst = Cart.Cart("digitalStore", "Cart")



invInst.viewInventory()

choice = -1
while choice != 0:
    if not(UserInst.User.getLoggedIn()):
        choice = input("Would you like to \n 0: exit program\n1: login\n2: create account")
        if choice == "1":
            UserInst.User.getLoggedIn()
        if choice == "2":
            UserInst.User.createAccount()
    if UserInst.User.getLoggedIn():
        choice



