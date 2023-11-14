import hashlib

class User:
   def __init__(self, databaseName = "", tableName = "", password = "", email = ""):
      self._databaseName = databaseName
      self._tableName = tableName
      self._loggedIn = False
      self._userID = ""
      self.password_hash = self._hash_password(password)
      self.email = email

   def User(self):
      pass
   def User(self,databaseName, tableName):
      self.name = databaseName
      self.table = tableName
   
   def login(self):
      if not self._loggedIn:
         entered_email = input("Enter your email address: ")
         entered_password = input("Enter your password: ")
        
         while not self.verify_credentials(entered_email, entered_password):
          print("Invalid email or password. Please try again.")
          entered_email = input("Enter your email address: ")
          entered_password = input("Enter your password: ")

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
            new_email = input("Enter your email address: ")

            
            new_password = input("Enter your password: ")
            confirmed_password = input("Confirm your password: ")

            # Verification loop for password matching
            while new_password != confirmed_password:
                print("Passwords do not match. Please try again.")
                new_password = input("Enter your password: ")
                confirmed_password = input("Confirm your password: ")

            self.email = new_email
            self.password_hash = self._hash_password(new_password)
            print("Account created successfully.")
        else:
            print("You are already logged in. No need to create another account.")




  #TODO ADD THE VIEW ACCOUNT INFOMATION FUNCTION
  #TODO ADD THE GETTERS


   def verify_credentials(self, entered_email, entered_password):
        
        return (
            entered_email == self.email
            and self._hash_password(entered_password) == self.password_hash
        )
         
   
