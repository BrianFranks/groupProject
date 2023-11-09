#this is the main file and will connect everything
class inventory:
    items = []
    def addItem(self, itemAdded):
        self.items.append(itemAdded)
print("Hello World!")

#inventory class


#main
position = "employee"
storeInventory = inventory()
choice = input("Would you like to:\n0:Add a new item to inventory?\nChoice: ")
if choice == "0" and position == "employee":
    itemAdded = input("What would you like to add? ")
    storeInventory.addItem(itemAdded)