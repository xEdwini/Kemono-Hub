import sys
import sqlite3
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)

# Initialize the database and create tables if they don't exist
def init_db():
    with sqlite3.connect('account.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Sightings (
                UserID TEXT PRIMARY KEY,
                AnimalSpotted TEXT,
                Location TEXT,
                NumberSpotted INTEGER
            )
        ''')
        conn.commit()

# Report a sighting into the database
def report_sighting(user_id, animal_spotted, location, number_spotted):
    try:
        with sqlite3.connect('account.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Sightings (UserID, AnimalSpotted, Location, NumberSpotted)
                VALUES (?, ?, ?, ?)
            ''', (user_id, animal_spotted, location, number_spotted))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False

# PyQt5 Form for reporting sightings
class SightingReportForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.user_id_input = QLineEdit(self)
        self.animal_spotted_input = QLineEdit(self)
        self.location_input = QLineEdit(self)
        self.number_spotted_input = QLineEdit(self)

        self.submit_button = QPushButton('Submit Sighting', self)
        self.submit_button.clicked.connect(self.submit_sighting)

        layout.addWidget(QLabel('User ID:'))
        layout.addWidget(self.user_id_input)
        layout.addWidget(QLabel('Animal Spotted:'))
        layout.addWidget(self.animal_spotted_input)
        layout.addWidget(QLabel('Location:'))
        layout.addWidget(self.location_input)
        layout.addWidget(QLabel('Number Spotted:'))
        layout.addWidget(self.number_spotted_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_sighting(self):
        user_id = self.user_id_input.text()
        animal_spotted = self.animal_spotted_input.text()
        location = self.location_input.text()
        number_spotted = self.number_spotted_input.text()

        if not user_id or not animal_spotted or not location or not number_spotted.isdigit():
            QMessageBox.warning(self, 'Error', 'Please fill all fields correctly.')
            return

        success = report_sighting(user_id, animal_spotted, location, int(number_spotted))
        if success:
            QMessageBox.information(self, 'Success', 'Sighting reported successfully.')
            self.close()
        else:
            QMessageBox.critical(self, 'Error', 'Failed to report sighting.')

# Main function to run the application
def main():
    init_db()  # Initialize the database and create tables if they don't exist
    app = QApplication(sys.argv)
    form = SightingReportForm()
    form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
