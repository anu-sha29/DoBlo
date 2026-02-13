import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class ChoiceScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose an Option")
        self.setGeometry(500, 200, 400, 300)
        self.setStyleSheet("background-color: white;")

        # Layout
        layout = QVBoxLayout()

        # Title Label
        label = QLabel("Please choose an option:")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: black;")
        layout.addWidget(label)

        # Buttons
        donation_button = QPushButton("Donation Request")
        donor_button = QPushButton("Donor Registration")

        # Style buttons
        donation_button.setStyleSheet("font-size: 16px; padding: 10px;")
        donor_button.setStyleSheet("font-size: 16px; padding: 10px;")

        # Connect actions
        donation_button.clicked.connect(self.open_donation_request)
        donor_button.clicked.connect(self.open_donor_registration)

        # Add buttons to layout
        layout.addWidget(donation_button)
        layout.addWidget(donor_button)

        self.setLayout(layout)

    def open_donation_request(self):
        self.close()
        self.new_window("Donation Request Screen")

    def open_donor_registration(self):
        self.close()
        self.new_window("Donor Registration Screen")

    def new_window(self, title):
        self.next_window = QWidget()
        self.next_window.setWindowTitle(title)
        self.next_window.setGeometry(500, 200, 400, 300)
        self.next_window.setStyleSheet("background-color: white;")
        label = QLabel(title, self.next_window)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: black;")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.next_window.setLayout(layout)
        self.next_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChoiceScreen()
    window.show()
    sys.exit(app.exec_())