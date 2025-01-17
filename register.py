import sqlite3
import sys
import hashlib
from PyQt5.QtWidgets import *
import random

def db_connect():
    connection = sqlite3.connect("account.db")
    cursor = connection.cursor() #Represents cursor to execute SQL queries
    return (connection, cursor)

#Inserting new users into users table
def adding_user(userID, password, usertype, orgCode):
    connection, cursor = db_connect()
    #Check if username already exists
    cursor.execute(f"SELECT * FROM User WHERE UserID = '{userID}'")#Query to check names
    existing_name = cursor.fetchone()

    if existing_name:
        #Display message if username exists
        print("Username already exists. Please choose a different one.")
        return False
    
    if usertype == "public":
        orgCode = None

    #No existing user with the same name or email, proceed with registration
    print(password)
    hashed_password = hashlib.md5(password.encode()).hexdigest()#Hash with SHA-256 for privacy
    print(hashed_password)
    cursor.execute('''
    INSERT INTO User(UserID, password, userType, organisationCode)
    VALUES(?, ?, ?, ?)
    ''', (userID, hashed_password, usertype, orgCode))

    
    # Insert details to appropriate table
    '''
    match usertype:
        case "Student":
            pass
        case "Teacher":
            pass
        case "Principle":
            pass
        case "Admin":
            pass
    '''
    #Commit changes to database
    connection.commit()
    return True

#Checks if user is already in users table
def check_user(email, password):
    connection, cursor = db_connect()
    hashed_password = hashlib.md5(password.encode()).hexdigest()#Hash with md5 for privacy
    cursor.execute(f'''
    SELECT * FROM User
    WHERE organisationCode = '{email}' AND password = '{hashed_password}'
    ''')
    return cursor.fetchone()

#Generate a Unique Special Access Code for Login
def generateCode():
    #Letters and Numbers to use for code
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"

    word = letters + numbers
    length = 6
    code = "".join(random.sample(word, length))#Combines string and length function to make code

    print("The Unique Special Access code is: "+ code.upper())#Outputs code uppercase when called 

#Closes database connection
def close_db():
    connection, cursor = db_connect()
    connection.close()

#PyQt5 GUI
class RegisterApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("User Registration")#Title for window
        self.resize(750, 400)
        self.initUI()

    #Isolate button UIs for readability
    def initUI(self):
        self.layout = QVBoxLayout()#Layout will be verticle box

        #User Type Drop Down Button
        self.combo_userType = QComboBox()
        self.combo_userType.addItems(["Public", "Student", "Teacher", "Principal", "Admin"])#Add 5 options in drop box
        self.label_userType = QLabel("User Type:")#QLabel is for button name

        #Name Box
        self.label_name = QLabel("Name:")#QLabel is for button name
        self.editName = QLineEdit()#QLineEdit creates imput box

        #Email Box
        self.label_email = QLabel("Email:")#QLabel is for button name
        self.editEmail = QLineEdit()#QLineEdit creates imput box

        #Password Box
        self.label_password = QLabel("Password:")#QLabel is for button name
        self.editPassword = QLineEdit()#QLineEdit creates imput box
        self.editPassword.setEchoMode(QLineEdit.Password)#To make password appear hidden

        #Back to Login Button
        self.BackButton = QPushButton("Back to Login")#QPushButton is for interactive buttons
        self.BackButton.clicked.connect(self.backToLogin)#If clicked send signal to backToLogin function

        #Register Button
        self.register = QPushButton("Register")#QPushButton is for interactive buttons
        self.register.clicked.connect(self.registerUser)#If clicked send signal to registerUser function

        #Consent Tickbox
        self.tickbox = QCheckBox("I consent to the use of my data ")#The text next to the checklist box
        self.tickbox.setChecked(False)#Set the initial tickbox as false

        #Layout for all buttons
        self.layout.addWidget(self.label_userType)#Label for combo box
        self.layout.addWidget(self.combo_userType)#Adding combo box to select option

        self.layout.addWidget(self.label_name)#Name Box
        self.layout.addWidget(self.editName)#QLineEdit to enter name

        self.layout.addWidget(self.label_email)#Email Box
        self.layout.addWidget(self.editEmail)#QLineEdit to enter email

        self.layout.addWidget(self.label_password)#Password Box
        self.layout.addWidget(self.editPassword)#QLineEdit to enter password

        self.layout.addWidget(self.tickbox)#Adds the checkbox for consent

        self.layout.addWidget(self.register)#Register Button

        self.layout.addWidget(self.BackButton)#Back to Login Button

        self.setLayout(self.layout)#Sets main layout of Qwidget to other self.layout

    #Going Back to Login Button
    def backToLogin(self):
        print("Goodbye")
        self.close()

    #Registering User
    def registerUser(self):
        #Local variables
        name = self.editName.text()
        email = self.editEmail.text()
        password = self.editPassword.text()
        usertype = self.combo_userType.currentText()# 
        consent = self.tickbox.isChecked()#Check if box is checked

        # Validate input and add user to the database
        if name and email and password and usertype and consent:#If all fields are filled continue
            if name[0].upper() == 'U':#Must start with a U 
                if adding_user(name, email, password, usertype):#call adding_user function
                    print("User registered successfully!")
                else:
                    print("Registration failed.")
            else:
                print("Username must start with 'U'.")
        else:
            print("Please fill in all fields and give consent")
            

if __name__ == "__main__":#If condiction is met

    app = QApplication(sys.argv)#Uses QApplication class from library to manage main settings

    registerationApp = RegisterApp()#Creates current model of main window
    registerationApp.show()#Display registration window
    sys.exit(app.exec_())#Exit whole system


