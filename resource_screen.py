# Imports:

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
import sys

# Create Resources Screen
class ResourceScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resource Hub")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.initUI() # initialise UI

    # Method to open the link
    def open_link(self, link):
        QDesktopServices.openUrl(QUrl(link))

    # Method to create the links
    def create_link_label(self, text, url):
        label = QLabel(f"<a href='{url}'>{text}</a>", self.central_widget) # Format string to input parameters
        label.setOpenExternalLinks(True)
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        label.setFont(self.LabelFont)
        label.linkActivated.connect(lambda: self.open_link(url)) # Creates Signal to QWidget when activated
        return label

    # Method to create subheadings
    def create_subheading(self, text):
        label = QLabel(text, self.central_widget)
        label.setAlignment(Qt.AlignLeft)
        label.setFont(self.SubheadingFont)
        return label
    
    # Method to initialise
    def initUI(self):

        # Create Vbox Structure Layout 
        layout = QVBoxLayout(self.central_widget)

        # Create Font styles
        TitleFont = QFont()
        TitleFont.setPointSize(36)
        TitleFont.setBold(True)

        self.LabelFont = QFont()
        self.LabelFont.setPointSize(18)

        self.SubheadingFont = QFont()
        self.SubheadingFont.setPointSize(24)
        self.SubheadingFont.setBold(True)
        
        # Title Label
        title_label = QLabel("Komodo's Resource Hub", self.central_widget)
        title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        title_label.setFont(TitleFont)
        layout.addWidget(title_label)
        layout.addSpacing(10)

        # Current subheadings with links
        subheadings = {
            "Sumatran Tigers": [                                                                                # Subheading
                ("WWF: Sumatran Tigers", 'https://www.worldwildlife.org/species/sunda-tiger'),                  # Links with display text
                ("London Zoo: Sumatran Tigers", 'https://www.londonzoo.org/whats-here/animals/sumatran-tiger')
            ],
            "Javan Rhinoceros": [
                ("WWF: Javan Rhinoceros", 'https://www.worldwildlife.org/species/javan-rhino')
            ],
            "Komodo Dragon": [
                ("London Zoo: Komodo Dragon", 'https://www.londonzoo.org/whats-here/animals/komodo-dragon'),
                ("WWF: Komodo Dragon", 'https://www.worldwildlife.org/photos/best_of_indonesia_part_1_komodo_drage_travel_8-15-2012'),
                ("Smithsonian's National Zoo: Komodo Dragon", 'https://nationalzoo.si.edu/animals/komodo-dragon')
            ],
            "Komodo Foundation": [
                ("Click here to find out more...", 'https://komododragon.org/')
            ]
        }

        # Traverses through dictionary to create subheadings and links
        for subheading, links in subheadings.items():
            # Create Subheading
            layout.addWidget(self.create_subheading(subheading))
            for text, url in links:
            # Create Link
                layout.addWidget(self.create_link_label(text, url))
            layout.addSpacing(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    resource = ResourceScreen()
    resource.showMaximized()
    sys.exit(app.exec_())
