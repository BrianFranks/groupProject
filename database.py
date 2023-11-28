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


-- Inventory Table
CREATE TABLE Inventory (
    ISBN VARCHAR(255) PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    Genre VARCHAR(255),
    Pages VARCHAR(255),
    ReleaseDate VARCHAR(255),
    Stock INT
);

-- User Table
CREATE TABLE User (
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
);


-- Cart Table
CREATE TABLE Cart (
    UserID INT,
    ISBN VARCHAR(20),
    Quantity INT,
    PRIMARY KEY (UserID, ISBN),
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (ISBN) REFERENCES Inventory(ISBN)
);''')

cursor.close()
connection.close()

