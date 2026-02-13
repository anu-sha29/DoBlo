import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QProgressBar, QLineEdit, QToolTip, QMessageBox
)
from PyQt5.QtCore import Qt

class ChoiceScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose an Option")
        self.setGeometry(500, 200, 400, 300)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()

        label = QLabel("Please choose an option:")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: black;")
        layout.addWidget(label)

        donation_button = QPushButton("Donation Request")
        donor_button = QPushButton("Donor Registration")

        donation_button.setStyleSheet("font-size: 16px; padding: 10px;")
        donor_button.setStyleSheet("font-size: 16px; padding: 10px;")

        donation_button.clicked.connect(self.open_donation_request)
        donor_button.clicked.connect(self.open_donor_registration)

        layout.addWidget(donation_button)
        layout.addWidget(donor_button)

        self.setLayout(layout)

    def open_donation_request(self):
        self.close()
        self.new_window("Donation Request Screen")

    def open_donor_registration(self):
        self.close()
        self.registration = DonorRegistrationScreen()
        self.registration.show()

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


class DonorRegistrationScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Donor Registration")
        self.setGeometry(500, 200, 400, 400)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()

        # Progress bar (shows steps left)
        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        # Quick Eligibility Quiz (deal-breaker questions)
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter your Age")
        layout.addWidget(self.age_input)

        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Enter your Weight (kg)")
        # Tooltip explaining why weight matters
        self.weight_input.setToolTip("Weight is required for safety during donation.")
        layout.addWidget(self.weight_input)

        self.last_donation_input = QLineEdit()
        self.last_donation_input.setPlaceholderText("Enter date of last donation (YYYY-MM-DD)")
        self.last_donation_input.setToolTip("Helps ensure safe intervals between donations.")
        layout.addWidget(self.last_donation_input)

        # Submit button
        submit_button = QPushButton("Check Eligibility")
        submit_button.clicked.connect(self.check_eligibility)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def check_eligibility(self):
        try:
            age = int(self.age_input.text())
            weight = int(self.weight_input.text())
            last_donation = self.last_donation_input.text()

            # Simple eligibility rules
            if age < 18:
                QMessageBox.warning(self, "Not Eligible", "You must be at least 18 years old.")
                return
            if weight < 50:
                QMessageBox.warning(self, "Not Eligible", "Minimum weight is 50 kg for safety.")
                return
            if not last_donation:
                QMessageBox.information(self, "Eligible", "You are eligible to register!")
            else:
                QMessageBox.information(self, "Eligible", "You are eligible to register!")

            # Update progress bar
            self.progress.setValue(100)

        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers for age and weight.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChoiceScreen()
    window.show()
    sys.exit(app.exec_())