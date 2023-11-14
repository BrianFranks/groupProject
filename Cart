class Cart:
    def __init__(self, databaseName='', tableName=''):
        self.databaseName = databaseName
        self.tableName = tableName
        self.cart_contents = {}  #databases required

    def viewCart(self, userID, inventoryDatabase):
        # Requires inventory database
        # print the content of cart
        print(f"Cart for user {userID}: {self.cart_contents}")

    def addToCart(self, userID, ISBN):
        # Requires inventory database
        # add item to caet
        if ISBN not in self.cart_contents:
            self.cart_contents[ISBN] = 1
        else:
            self.cart_contents[ISBN] += 1
        print(f"Added ISBN {ISBN} to the cart for user {userID}")

    def removeFromCart(self, userID, ISBN):
        # Remove item from cart
        if ISBN in self.cart_contents:
            if self.cart_contents[ISBN] > 1:
                self.cart_contents[ISBN] -= 1
            else:
                del self.cart_contents[ISBN]
            print(f"Removed one instance of ISBN {ISBN} from the cart for user {userID}")
        else:
            print(f"ISBN {ISBN} not found in the cart for user {userID}")

    def checkOut(self, userID):
        # Requires inventory database
        # Adds the total number of items together to proceed with checkout, clears the cart, needs to call inventory class to change stock
        total_items = sum(self.cart_contents.values())
        print(f"Checked out {total_items} items from the cart for user {userID}")
        self.cart_contents.clear()  # Clear the cart after checkout

