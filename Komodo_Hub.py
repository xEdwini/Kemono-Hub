import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QMenu, QAction, QTextBrowser
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont, QIcon
from PyQt5.QtCore import Qt, QPoint
from report_sights import SightingReportForm
from learn_about import letslearn
from quiz_with_gui import questions_data,QuizWindow
from resource_screen import ResourceScreen

class KomodoHubGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Sets up the main window and size of the default size of the GUI 
        self.setWindowTitle("Komodo Hub")
        self.setGeometry(0, 0, 1920, 1080) # Sets Screen Sizr of window

        # Sets the background image 
        self.set_background_image("Images/bg_img.jpg")

        # Creating Label for GUI heading 
        heading_title = QLabel("KOMODO HUB", self)
        heading_title.setStyleSheet("font-size: 58px; font-family: 'Arial Black'; font-weight: bold; color: white;")

        # Creating the box layout for the heading label
        heading_layout = QVBoxLayout()
        heading_layout.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        heading_layout.addWidget(heading_title)

        # Creating the clickable buttons
        report_sightings_button = QPushButton(self)
        learning_button = QPushButton(self)
        quiz_button = QPushButton(self)
        community_button = QPushButton(self)
        resource_button = QPushButton(self)  

        # Defining the style for these buttons
        button_style = "font-size: 24px; padding: 20px;"

        # Alotting style and setting the size of the buttons
        button_size = 250  
        report_sightings_button.setFixedSize(button_size, button_size)
        learning_button.setFixedSize(button_size, button_size)
        quiz_button.setFixedSize(button_size, button_size)
        community_button.setFixedSize(button_size, button_size)
        resource_button.setFixedSize(button_size, button_size)  

        report_sightings_button.setStyleSheet(button_style)
        learning_button.setStyleSheet(button_style)
        quiz_button.setStyleSheet(button_style)
        community_button.setStyleSheet(button_style)
        resource_button.setStyleSheet(button_style)  

        # Setting the images for each of these buttons
        self.set_button_image(report_sightings_button, "Images/pic1.jpg")
        self.set_button_image(learning_button, "Images/pic2.jpg")
        self.set_button_image(quiz_button, "Images/pic3.jpg")
        self.set_button_image(community_button, "Images/pic4.jpg")
        self.set_button_image(resource_button, "Images/pic5.png")  

        report_sightings_button.clicked.connect(self.open_report_sight_screen)
        learning_button.clicked.connect(self.open_learn_screen)
        quiz_button.clicked.connect(self.open_quiz_screen)
        community_button.clicked.connect(self.open_community_screen)
        resource_button.clicked.connect(self.open_resource_screen)

        # Defining the Labels for the buttons 
        label1 = QLabel("Report Sightings", self)
        label2 = QLabel("Let's Learn", self)
        label3 = QLabel("QUIZ Zone", self)
        label4 = QLabel("Community", self)
        label5 = QLabel("Resource Hub", self) 

        # Setting the style for the labels
        label_style = "font-size: 34px; font-family: 'Arial'; color: white; text-decoration: underline;"
        label1.setStyleSheet(label_style)
        label2.setStyleSheet(label_style)
        label3.setStyleSheet(label_style)
        label4.setStyleSheet(label_style)
        label5.setStyleSheet(label_style)  

        # Creating a box layout to pair the boxes with respective labels 
        layouts1 = QVBoxLayout()
        layouts1.addWidget(report_sightings_button)
        layouts1.addWidget(label1)
        layouts1.setAlignment(Qt.AlignCenter)

        layouts2 = QVBoxLayout()
        layouts2.addWidget(learning_button)
        layouts2.addWidget(label2)
        layouts2.setAlignment(Qt.AlignCenter)

        layouts3 = QVBoxLayout()
        layouts3.addWidget(quiz_button)
        layouts3.addWidget(label3)
        layouts3.setAlignment(Qt.AlignCenter)

        layouts4 = QVBoxLayout()
        layouts4.addWidget(community_button)
        layouts4.addWidget(label4)
        layouts4.setAlignment(Qt.AlignCenter)

        layouts5 = QVBoxLayout()  
        layouts5.addWidget(resource_button)
        layouts5.addWidget(label5)
        layouts5.setAlignment(Qt.AlignCenter)  

        # Definning the spaces in between the buttons 
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.addLayout(layouts1)
        button_layout.addSpacing(40)  
        button_layout.addLayout(layouts2)
        button_layout.addSpacing(40)
        button_layout.addLayout(layouts3)
        button_layout.addSpacing(40)
        button_layout.addLayout(layouts4)
        button_layout.addSpacing(40)  
        button_layout.addLayout(layouts5)  

        # Defining a main layout and add the heading and button layout
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(heading_layout)
        main_layout.addStretch()  
        main_layout.addLayout(button_layout)
        main_layout.addStretch()  # adding another stretch for better spacing

        # Creating the Profile button 
        the_profile_button = QPushButton("Profile", self)
        the_profile_button.setIconSize(QPixmap(30, 30).rect().size())  # Setting size
        the_profile_button.setStyleSheet("border-radius: 15px; background-color: white; font-size: 18px; padding: 10px;")
        the_profile_button.setToolTip("Click for Profile Menu")  # Adding the Tooltip content
        the_profile_button.clicked.connect(self.show_profile_menu)

        # Creating the Help (readme) button 
        readme_button = QPushButton(self)
        readme_button.setIcon(QIcon("Images/help_icon.png"))
        readme_button.setIconSize(QPixmap(30, 30).rect().size())  # Set icon size for the button
        readme_button.setStyleSheet("background-color: transparent;")  # Transparent background
        readme_button.clicked.connect(self.open_readme_file)

        # Positioning the button in the bottom right corner
        readme_layout = QHBoxLayout()
        readme_layout.addStretch(1)
        readme_layout.addWidget(readme_button)
        main_layout.addLayout(readme_layout)

    def open_report_sight_screen(self):
        self.repScreen = SightingReportForm()
        self.repScreen.showMaximized()

    def open_learn_screen(self):
        self.lscreen = letslearn()
        self.lscreen.showMaximized()

    def open_quiz_screen(self):
        self.qScreen = QuizWindow(questions_data)
        self.qScreen.showMaximized()

    def open_community_screen(self):
        print("Community Screen")

    def open_resource_screen(self):
        self.rScreen = ResourceScreen()
        self.rScreen.showMaximized()

    # Loading and scaling the image for the button
    def set_button_image(self, button, image_path):
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(button.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        button.setIcon(QIcon(pixmap))
        button.setIconSize(button.size())

    # Creating the menu for the profile button
    def show_profile_menu(self):
        menu = QMenu(self)
        # Adding some font styles and spacing to the screen
        menu.setStyleSheet("QMenu { font-size: 18px; }"
                           "QMenu::item { padding: 10px; }")

        user_action = QAction("User: John", self)
        progress_action = QAction("Progress: 75%", self)
        profile_action = QAction("Profile", self)

        # Adding the action items to the menu 
        menu.addAction(user_action)
        menu.addAction(progress_action)
        menu.addAction(profile_action)

        # Retructures the format of screen
        menu_size = menu.sizeHint()
        menu_size.setWidth(menu_size.width() + 20)  
        menu_size.setHeight(menu_size.height() + 20)
        menu.setFixedSize(menu_size)

        global_pos = self.mapToGlobal(QPoint(0, 0))
        menu.exec_(global_pos)

    # Setup the background image and scalling the image to fit
    def set_background_image(self, image_path):
        # Set up background image
        pixmap = QPixmap(image_path)
        image = pixmap.scaled(self.size(), aspectRatioMode=0)
        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

    # Function for opening the readMe txt file
    def open_readme_file(self):
        # Opens the "readME.txt" file using the default text editor
        subprocess.Popen(["notepad.exe", "readME.txt"])

# Starting the Application 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    komodo_hub = KomodoHubGUI()
    komodo_hub.showMaximized()  # Sets the screen to be maximised 
    sys.exit(app.exec_())
