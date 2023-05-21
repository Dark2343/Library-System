import Database as db
import Person as prs
import sys

class Authenticator:
    def __init__(self):
        
        # object of person Class
        self.pr = None
        
        # object of the database Class
        self.database = db.Database()
        self.database.connectToDataBase()

        # retrieved query (default query)
        self.rows = self.database.executeQuery("SELECT * FROM person")
        
        # all of the person attributes names 
        self.column_names = [desc[0] for desc in self.database.getCursor().description]


    def isAuth(self, email, password):
        email_index = self.column_names.index("email")
        password_index = self.column_names.index("passwordHash")
       
        for row in self.rows:
            if row[email_index] == email:
                if row[password_index] == password:
                    return True
        return False

# Make a function here that returns the data of the student if the email and password are correct
    def returnPersonData(self, email, password):
        if self.isAuth(email, password):
            id_index          = self.column_names.index("personID")
            Fname_index       = self.column_names.index("firstName")
            Lname_index       = self.column_names.index("lastName")
            phone_index       = self.column_names.index("phoneNumber")
            sex_index         = self.column_names.index("sex")
            isAdmin_index     = self.column_names.index("isAdmin")
            dateOfBirth_index = self.column_names.index("dateOfBirth")
            email_index       = self.column_names.index("email")
            password_index    = self.column_names.index("passwordHash")
                
            for row in self.rows:
                if row[email_index] == email:
                    if row[password_index] == password:
                        self.pr = prs.Person(
                            row[id_index],
                            row[Fname_index],
                            row[Lname_index],
                            row[phone_index],
                            row[sex_index],
                            row[isAdmin_index],
                            row[dateOfBirth_index],
                            row[email_index],
                            row[password_index]
                        )
        return self.pr

    def addStudent(self , newStudent: prs.Person):
        # this print statements for testing
        print("---ADD STUDENT FUNCTION IN AUTHOR. CLASS---")
        print("student id: ",newStudent.id)
        print("student email: ",newStudent.email)
        print("student phone: ",newStudent.phone)
        query = f"INSERT INTO PERSON(firstName, lastName, phoneNumber, dateOfBirth, sex, isAdmin, email, passwordHash) Values({newStudent.id})"
        self.database.executeQuery("")
