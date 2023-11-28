import sys
import sqlite3
try:
        connection = sqlite3.connect("digitalStore" + ".sql")

        print("Successful connection.")

except:
        print("Failed connection.")

            ## exits the program if unsuccessful
        sys.exit()
cursor = connection.cursor()
cursor.execute('''

CREATE TABLE IF NOT EXISTS Inventory (
    ISBN VARCHAR(255) PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Genre VARCHAR(255),
    Pages VARCHAR(255),
    ReleaseDate VARCHAR(255),
    Stock INT
);''')
connection.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Email VARCHAR(255),
    Password VARCHAR(255),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(50),
    Zip VARCHAR(20),
    Payment VARCHAR(50)
);''')
connection.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Cart (
    UserID INT,
    ISBN VARCHAR(20),
    Quantity INT,
    PRIMARY KEY (UserID, ISBN),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ISBN) REFERENCES Inventory(ISBN)
);''')
connection.commit()

cursor.close()
connection.close()

