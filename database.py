# Imports: 
import sqlite3              # Database Module 
from pathlib import Path    # Module to find file in folder
import hashlib

def hashing_algorithm(value):
    hash_val = hashlib.md5(value.encode())
    hash_val = hash_val.hexdigest()
    return(hash_val)
'''
Function that checks if the database has been made:
- If the database file exists then the code will continue
- If the database file cannot be found or does not exist, 
  the function will create the database file
'''

def start_program():
    conn = sqlite3.connect('account.db') # If it can't find, will create new file
    cursor = conn.cursor()            # Object to access database
    create_tables(conn, cursor)       # Calls create_table() function
    insert_test_values(conn, cursor)  # Calls insert_test_values function
    conn.close()

def check_data():
    fileName = Path('account.db')
    if not(fileName.is_file()):
        conn = sqlite3.connect('account.db') # If it can't find, will create new file
        cursor = conn.cursor()            # Object to access database
        create_tables(conn, cursor)       # Calls create_table() function
        insert_test_values(conn, cursor)  # Calls insert_test_values function
        conn.close()                      # Closes connection

# Function that will create the tables in the database
def create_tables(conn, cursor):
    # Create Queries

    cursor.execute('''CREATE TABLE User
                    (UserID STRING PRIMARY KEY NOT NULL, 
                    password STRING, 
                    userType STRING, 
                    organisationCode STRING);
                ''')
    
    cursor.execute('''CREATE TABLE Student
                    (StudentID STRING PRIMARY KEY NOT NULL,  
                    FirstName STRING, 
                    LastName STRING, 
                    DOB DATE,
                    FOREIGN KEY(StudentID) REFERENCES User(UserID));
                ''')
    
    cursor.execute('''CREATE TABLE Teacher
                    (TeacherID STRING PRIMARY KEY NOT NULL,
                    FirstName STRING, 
                    LastName STRING, 
                    AccessLvl INTEGER,
                    FOREIGN KEY(TeacherID) REFERENCES User(UserID));
                ''')
    
    cursor.execute('''CREATE TABLE Principle
                    (PrincipleID STRING PRIMARY KEY NOT NULL,
                    FirstName STRING, 
                    LastName STRING, 
                    AccessLvl INTEGER,
                    FOREIGN KEY(PrincipleID) REFERENCES User(UserID));
                ''')

    cursor.execute('''CREATE TABLE Admin
                    (AdminID STRING PRIMARY KEY NOT NULL,
                    FirstName STRING, 
                    LastName STRING, 
                    AccessLvl INTEGER,
                    FOREIGN KEY(AdminID) REFERENCES User(UserID));
                ''')
    
    cursor.execute('''CREATE TABLE Class
                    (ClassID STRING NOT NULL, 
                    StudentID STRING,
                    TeacherID STRING,
                    PRIMARY KEY(ClassID, StudentID),
                    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
                    FOREIGN KEY(TeacherID) REFERENCES Teacher(TeacherID));
            ''')
    
    cursor.execute('''CREATE TABLE Course
                    (CourseID STRING PRIMARY KEY NOT NULL, 
                    CourseName STRING);
                ''')

    cursor.execute('''CREATE TABLE Enrol
                    (StudentID STRING, 
                    CourseID STRING,
                    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
                    FOREIGN KEY(CourseID) REFERENCES Course(StudentID));
                ''')
    
    """
    cursor.execute('''CREATE TABLE SchoolManagementMember
                    (TeacherID STRING, 
                    PrincipleID STRING,
                    AdminID STRING,
                    PRIMARY KEY(TeacherID, PrincipleID, AdminID));
                ''')   
                
    """ 
    # Note: Not Needed
    #Can use the query below to achieve this data: 
    # SELECT TeacherID, PrincipleID, AdminID WHERE organisationCode = <some value>;

    conn.commit()
    print("Tables created successfully")

# Function that inserts test values for the database
def insert_test_values(conn, cursor):
    # Test data

    test_data_user = [
        ('U001', hashing_algorithm('mypass'), 'student', 'covCV3uni'),
        ('U002', hashing_algorithm('safepassword%'), 'teacher', 'covCV3uni'),
        ('U003', hashing_algorithm('password000'), 'admin', 'covCV3uni'),
        ('U004', hashing_algorithm('admin123'), 'principle', 'covCV3uni'),
        ('U005', hashing_algorithm('publicPass'), 'public', 'Null'),
    ]
        
    test_data_student = [
        ('U001', 'Lor', 'Em', '2000-11-30'),
        ('U002', 'Ip', 'Sum', '2001-5-13'),
        ('U003', 'Man', 'Pan', '2000-09-16'),
    ]

    test_data_teacher = [
        ('U004', 'Kim', 'Lee', 2)
    ]

    test_data_principle = [
        ('U006', 'Joe', 'Han', 3)
    ]
    
    test_data_admin = [
        ('U005', 'Ma', 'Doe', 4)
    ]

    test_data_class = [
        ('CL001', 'U001', 'U004'),
        ('CL001', 'U002', 'U004'),
        ('CL001', 'U003', 'U004'),
    ]

    test_data_course = [
        ('CO001', 'Learning About Sumatran Tigers'),
        ('CO002', 'Learning About Javan Rhinos'),
    ]

    test_data_enrol = [
        ('U001', 'CO001'),
        ('U002', 'CO001'),
        ('U003', 'CO002')
    ]

    # Insert test data into database tables

    for row in test_data_user:
        cursor.execute("INSERT INTO User VALUES(?, ?, ?, ?)", row)

    for row in test_data_student:
        cursor.execute("INSERT INTO Student VALUES(?, ?, ?, ?)", row)

    for row in test_data_teacher:
        cursor.execute("INSERT INTO Teacher VALUES(?, ?, ?, ?)", row)
    
    for row in test_data_principle:
        cursor.execute("INSERT INTO Principle VALUES(?, ?, ?, ?)", row)
    
    for row in test_data_admin:
        cursor.execute("INSERT INTO Admin VALUES(?, ?, ?, ?)", row)
    
    for row in test_data_class:
        cursor.execute("INSERT INTO Class VALUES(?, ?, ?)", row)
    
    for row in test_data_course:
        cursor.execute("INSERT INTO Course VALUES(?, ?)", row)
    
    for row in test_data_enrol:
        cursor.execute("INSERT INTO Enrol VALUES(?, ?)", row)

    conn.commit()
    conn.close()

    print("Inserted Values")

