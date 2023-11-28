try:
    cursor.execute(f"INSERT INTO user (Email, Password, firstName, LastName, Address, City, State, Zip, Payment) VALUES ('{user.email}', '{user.password}', '{user.firstName}', '{user.lastName}', '{user.address}', '{user.city}', '{user.state}', '{user.zipCode}', '{user.payment}')")

    connection.commit()
    print("Record inserted successfully.")
except sqlite3.Error as e:
    print("Error inserting record:", e)


   

try:
    connection = sqlite3.connect("database.db")

    print("Successful connection.")

except:
    print("Failed connection.")

    ## exits the program if unsuccessful
    sys.exit()

## cursor to send queries through
cursor = connection.cursor()
    
