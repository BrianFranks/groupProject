class User:
    def __init__(self, databaseName = "", tableName = "", password = ""):
      self._loggedIn = False
      self._userID = ""
      self.firstName = ""
      self.lastName = ""
      self.address = ""
      self.city = ""
      self.state = ""
      self.zipCode = ""
      self.payment = ""

    def User(self):
      pass
   
    def User(self,databaseName, tableName, email, address, city, state, zipCode, firstName, lastName, payment):
      self.name = databaseName
      self.email = email
      self.table = tableName
      self.address = address
      self.city = city
      self.state = state
      self.zipCode = zipCode
      self.firstName = firstName
      self.lastName = lastName
      self.payment = payment

    def login(self):
      if not self._loggedIn:
         enteredEmail = input("Enter your email address: ")
         enteredPassword = input("Enter your password: ")
        
         while not self.verify_credentials(enteredEmail, enteredPassword):
          print("Invalid email or password. Please try again.")
          enteredEmail = input("Enter your email address: ")
          enteredPassword = input("Enter your password: ")

      self.userID = input("Enter your user ID: ")
    
      self.loggedIn = True
      
      print("Login successful.")
     
      return self._loggedIn

      
    def logout(self):
      if self._loggedIn:
         self._userID = ""
         self.loggedIn = False
         print("Logout successful. ")

      else:
         print("You are not logged in. ")
      
      return not self._loggedIn
   
    def createAccount(self):
        if not self.loggedIn:
            newEmail = input("Enter your email address: ")
            newPassword = input("Enter your password: ")
            confirmedPassword = input("Confirm your password: ")
            userZip = input("Enter your zip code: ")
            userCity = input("Enter your city: ")
            userState = input("Enter your state: ")
            userfirstName = input("Enter your first name: ")
            userlastName = input("Enter your last name: ")
            userAddress = input("Enter your address: ")
            userPayment = input("Enter your payment (Visa, Mastercard, Discover, etc): ")
            
            # Verification loop for password matching
            while newPassword != confirmedPassword:
                print("Passwords do not match. Please try again.")
                newPassword = input("Enter your password: ")
                confirmedPassword = input("Confirm your password: ")

            self.email = newEmail
            self.password_hash = self._hash_password(newPassword)
            self.address = userAddress
            self.city = userCity
            self.state = userState
            self.zipCode = userZip
            self.firstName = userfirstName
            self.lastName = userlastName
            self.payment = userPayment

            print("Account created successfully.")
            
                
        else:
            print("You are already logged in. No need to create another account.")

    def viewAccountInformation(self):
        if self._loggedIn:
            print(f"User ID: {self._userID}")
            print(f"Database Name: {self._databaseName}")
            print(f"Table Name: {self._tableName}")
        else:
            print("You need to be logged in to view account information.")


  
         

    def getLoggedIn(self):
        return self._loggedIn

    def getUserID(self):
        return self._userID
