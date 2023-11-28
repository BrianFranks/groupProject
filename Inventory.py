import sqlite3
import sys
#everything above can be deleted later

class Inventory:
    def __init__(self, databaseName='', tableName=''):
        self.databaseName = databaseName
        self.tableName = tableName
        #self.inventoryContents = '???'

    #prints inventory
    def viewInventory(self):
        try:
            connection = sqlite3.connect(self.databaseName + ".sql")

            print("Successful connection.")

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
            sys.exit()

        print() ## spacing's sake

        ## cursor to send queries through
        cursor = connection.cursor()

        ## sends query and grabs data
        ## SELECT queries return a tuple for each row contained in a list
        ## --> a list of tuples
        cursor.execute("SELECT * FROM "+ self.tableName)

        ## only needed if you're running a SELECT
        ## this actually grabs the data
        result = cursor.fetchall()

        ## illustrates what unformatted results look like
        #print("Entire result set: ", result, sep="\n", end="\n\n\n")

        for x in result:
            ## you can print the entire tuple --> print(x)
            ## or you can print items from it using indices
            ## first item --> x[0]
            ## second item --> x[1]
            ## etc... (for however many columns a result has)

            print("Entire row:", x, "\n") ## all

            print("Row broken down into each column: ")
            for y in x:
                print(y)
            print()

            print("ISBN:", x[0]) ## only the ISBN
            print("Title:", x[1], "\tAuthor:", x[2])
            print("\n\n")
            cursor.close()
            connection.close()

    #finds and prints specific item
    def searchInventory(self):
        try:
            connection = sqlite3.connect(self.databaseName + ".sql")

            print("Successful connection.")

        except:
            print("Failed connection.")

            ## exits the program if unsuccessful
            sys.exit()
        cursor = connection.cursor()
        selection = input("Title:  ")
        print("Specific column select: ")

        cursor.execute("SELECT "+ selection +" FROM "+ self.tableName)
        result = cursor.fetchall()

        ## because of the SELECT query
        ## 0 --> Title
        ## 1 --> Author
        ## if not selecting ALL columns, numbering is based on query order
        for x in result:
            print(x[0], "by", x[1])

        ## selecting a specific column of a specific row
        ## goal: shows how it'd work even if you're only selecting one specific item
        ## even though you're only grabbing on item, it's still in a list of tuples
        print("\n\n\nSpecific column/row select:")
        '''
        cursor.execute("SELECT Title FROM "+ self.tableName +" WHERE ISBN='978-0307265432'")
        result = cursor.fetchall()

        print("Unformatted result:", result)

        title = result[0][0] ## grabs the single item
        print("Title you grabbed:", title)
        '''
        cursor.close()
        connection.close()

    #decreases inventory at a certain point
    def decrementInventory(self, ISBN):
         try:
            connection = sqlite3.connect(self.databaseName + ".sql")

            print("Successful connection.")
         except:
             print("Failed connection.")

             ## exits the program if unsuccessful
             sys.exit()
         cursor = connection.cursor()
         if ISBN not in self.inventoryContents:
            print("ISBN not found in inventory")
         else:
            print("ISBN found")
            cursor.execute("SELECT Stock FROM "+ self.tableName +" WHERE ISBN='" + str(ISBN) + "'")
            result = cursor.fetchall()
            result = int(result)
            print("Original stock: " + str(result))
            if result <= 1:
                #remove ISBN row from table
                cursor.execute("DELETE FROM "+ self.tableName +" WHERE ISBN='" + str(ISBN) + "'")
            else:
                #decrement value and return to table
            
                cursor.execute("UPDATE "+ self.tableName +" SET Stock='"+ str(result - 1) +"' WHERE ISBN='"+ str(ISBN) +"'")
                print("Decremented stock: " + str(result))
            cursor.close()
            connection.close()


