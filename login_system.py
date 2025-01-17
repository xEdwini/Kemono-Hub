import sqlite3
from pathlib import Path
import database

def insert_test_values():
    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()

    test_data = [
        ('U001', database.hashing_algorithm('mypass'), 'student', 'covCV3uni'),
        ('U002', database.hashing_algorithm('safepassword%'), 'teacher', 'covCV3uni'),
        ('U003', database.hashing_algorithm('password000'), 'admin', 'covCV3uni'),
        ('U004', database.hashing_algorithm('admin123'), 'principle', 'covCV3uni'),
        ('U005', database.hashing_algorithm('publicPass'), 'public', 'Null'),
    ]

    for data in test_data:
        cursor.execute("INSERT INTO User VALUES (?, ?, ?, ?)", data)

    conn.commit()
    conn.close()

def check_db():
    fileName = Path('account.db')
    if not(fileName.is_file()):
        #conn = sqlite3.connect('account.db') # if it can't find, will create new file
        #cursor = conn.cursor()
        '''cursor.execute(''''''CREATE TABLE User
                    (userID string PRIMARY KEY, password string, userType string, organisationNumber string)
                    '''''')'''
        #print("Table created successfully")
        #insert_test_values()            
        database.start_program()  
        #conn.commit()
        #conn.close()

def login(userID, password, organisationNumber='Null'):
    print(userID, password, organisationNumber) 
    password = database.hashing_algorithm(password)
    print(userID, password, organisationNumber) 
    conn = sqlite3.connect('account.db')
    cursor = conn.cursor()
    row = cursor.execute("SELECT * FROM User WHERE UserID = ?", (userID,),).fetchone()
    print(row)
    if row == None:
        print("Invalid Credentials: Cannot Find User. Are you sure you are a member?")
    elif row[2] != 'public':
        if row[1] == password and row[3] == organisationNumber:
            print("Login Successful")
            return True
        else:
            print("Invalid Password or Organisation Number")
    elif row[2] == 'public':
        if row[1] == password:
            print("Login Successful")
            return True
        else:
            print("Invalid Password")
    else:
        print("Incorrect Login Details")
    conn.close()
    return False
    

# Error handling, ensures input data are string
def take_inputs():
    while True:
        try:
            userID = str(input("Enter your ID: \n"))
            password = str(input("Enter your Password: \n"))
            organisationCode = str(input("Enter if applicable else press Enter\n"))
            if organisationCode == "":
                organisationCode = None
            else:
                pass
            break
        except:
            print("Invalid Data type - try again\n")
    return(userID, password, organisationCode)