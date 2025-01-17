# Import Modules:
 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from register import RegisterApp
import sys
from Komodo_Hub import KomodoHubGUI
import login_system


# Create Class for the screen
class Screen(QWidget):
    
    # Class initaliser

    def __init__(self):
        super().__init__()
        dimension = self.get_dimension()
        self.setGeometry(0,0, dimension.width(), dimension.height()) # Sets the window size
        self.setWindowTitle("Komodo Hub")
        self.initUI()

    # Create method to retrieve the dimesion of the device

    def get_dimension(self):
        screen_dimensions = QApplication.primaryScreen()
        return screen_dimensions.size()

    # Create the screen initaliser

    def initUI(self):
        # Make Vbox
        layout = QVBoxLayout(self)

        # Create Font style for labels

        TitleFont = QFont()
        TitleFont.setPointSize(36)
        TitleFont.setBold(True)

        LabelFont = QFont()
        LabelFont.setPointSize(18)

        placeholder_font = QFont()
        placeholder_font.setPointSize(16)

        # Create labels

        title_label = QLabel('Welcome to Komodo Hub', self)
        title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter) # Alligns title to the top and center of screen
        title_label.setFont(TitleFont)

        user_label = QLabel('User ID: ', self)
        user_label.setFont(LabelFont)
        self.userID_inp = QLineEdit(self) # Input box
        self.userID_inp.setPlaceholderText('Enter UserID...') # Placeholder text
        self.userID_inp.setFont(placeholder_font)
        
        password_label = QLabel('Password: ', self)
        password_label.setFont(LabelFont)
        self.password_inp = QLineEdit(self)
        self.password_inp.setPlaceholderText('Enter Password...')
        self.password_inp.setFont(placeholder_font)
        
        organisation_label = QLabel('Organisation Access Code: ', self)
        organisation_label.setFont(LabelFont)
        self.organisationNumber_inp = QLineEdit(self)
        self.organisationNumber_inp.setPlaceholderText('For Organisation Members...')
        self.organisationNumber_inp.setFont(placeholder_font)

        button_font = QFont()
        button_font.setPointSize(14)

        login_button = QPushButton("Login", self)
        login_button.clicked.connect(self.try_login) # Goes to method try_login
        login_button.setFont(button_font)

        register_button = QPushButton("Register", self)
        register_button.clicked.connect(self.register_account) # Goes to method register_account
        register_button.setFont(button_font)

        # Add widgets to the layout
        layout.addWidget(title_label)
        layout.addWidget(user_label)
        layout.addWidget(self.userID_inp)
        layout.addWidget(password_label)
        layout.addWidget(self.password_inp)
        layout.addWidget(organisation_label)
        layout.addWidget(self.organisationNumber_inp)

        # Create a horizontal layout for buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(login_button)
        button_layout.addWidget(register_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        # Set size policies
        title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        user_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.userID_inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        password_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.password_inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        organisation_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.organisationNumber_inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        register_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Set alignment to center
        layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

    # Calls login function in login_system file
    def try_login(self):
        userID = self.userID_inp.text()
        password = self.password_inp.text()
        orgNum = self.organisationNumber_inp.text()
        print("Here:", userID, password, orgNum)
        success = login_system.login(userID, password, orgNum)
        print("here")
        print(success)
        if success:
            print("reach here")
            self.close()  # Close the login screen
            self.show_app()
        else:
            pass
        return success
    
    def register_account(self):
        self.close() # Close current screen
        self.reg = RegisterApp() # Create new screen
        self.reg.show()
        self.close()
        self.newScreen = Screen() # Reopen login screen
        self.newScreen.show()

    def show_app(self):
        print("Reaches")
        self.main_app = KomodoHubGUI()
        self.main_app.showMaximized()
        

if __name__ == '__main__':
    login_system.database.check_data()
    app = QApplication(sys.argv)
    form = Screen()
    form.show()
    sys.exit(app.exec_())
    
    