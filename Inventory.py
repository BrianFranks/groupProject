class Inventory:
    def __init__(self, databaseName='', tableName=''):
        self.databaseName = databaseName
        self.tableName = tableName
        self.inventoryContents = '???'

    #prints inventory
    def viewInventory(self):
        print(self.inventoryContents)

    #finds and prints specific item
    def searchInventory(self, ISBN):
        title = input("What are you looking for: ")
        if title not in self.inventoryContents:
            print("title not found in inventory")
        else:
            print("item and all its info")

    #decreases inventory at a certain point
    def decrementInventory(self, ISBN):
         if ISBN not in self.inventoryContents:
            print("ISBN not found in inventory")
         else:
            self.inventoryContents[ISBN] = self.inventoryContents[ISBN] + 1


