import sys
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox, QProgressBar, QLineEdit
)
from PyQt5.QtCore import Qt, QTimer

# --- Splash Screen ---
class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blood Donation App")
        self.setGeometry(500, 200, 500, 400)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()
        label = QLabel("🩸 Blood Donation App")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 28px; font-weight: bold; color: red;")
        layout.addWidget(label)

        self.setLayout(layout)
        QTimer.singleShot(2000, self.open_choice)

    def open_choice(self):
        self.close()
        self.choice = ChoiceScreen()
        self.choice.show()

# --- Choice Screen ---
class ChoiceScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose Option")
        self.setGeometry(500, 200, 500, 400)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()
        label = QLabel("Please choose an option:")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(label)

        donor_btn = QPushButton("🧾 Donor Registration")
        donor_btn.setStyleSheet("font-size: 20px; padding: 15px;")
        donor_btn.clicked.connect(self.open_donor)
        layout.addWidget(donor_btn)

        request_btn = QPushButton("🚨 Blood Request")
        request_btn.setStyleSheet("font-size: 20px; padding: 15px;")
        request_btn.clicked.connect(self.open_request)
        layout.addWidget(request_btn)

        self.setLayout(layout)

    def open_donor(self):
        self.donor_window = DonorRegistration()
        self.donor_window.show()

    def open_request(self):
        self.request_window = BloodRequest()
        self.request_window.show()

# --- Donor Registration Window ---
class DonorRegistration(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Donor Registration")
        self.setGeometry(500, 200, 500, 400)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()
        label = QLabel("Donor Registration Form")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(label)

        # Input fields
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your Name")
        layout.addWidget(self.name_input)

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter your Age")
        layout.addWidget(self.age_input)

        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("Enter your Weight (kg)")
        layout.addWidget(self.weight_input)

        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        btn = QPushButton("Check Eligibility")
        btn.setStyleSheet("font-size: 18px; padding: 12px;")
        btn.clicked.connect(self.show_result)
        layout.addWidget(btn)

        self.setLayout(layout)

    def show_result(self):
        try:
            age = int(self.age_input.text())
            weight = int(self.weight_input.text())
            if age >= 18 and weight >= 50:
                self.progress.setValue(100)
                QMessageBox.information(self, "Eligibility Result", "✅ You are eligible to donate!")
            else:
                QMessageBox.warning(self, "Not Eligible", "❌ You do not meet the criteria.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers.")

# --- Blood Request Window ---
class BloodRequest(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blood Request")
        self.setGeometry(500, 200, 500, 500)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()
        label = QLabel("🚨 Emergency Blood Request")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 22px; font-weight: bold; color: red;")
        layout.addWidget(label)

        # Big buttons for quick access
        bg_btn = QPushButton("Blood Group: O+")
        bg_btn.setStyleSheet("font-size: 20px; padding: 15px;")
        comp_btn = QPushButton("Component: Platelets")
        comp_btn.setStyleSheet("font-size: 20px; padding: 15px;")
        units_btn = QPushButton("Units: 2")
        units_btn.setStyleSheet("font-size: 20px; padding: 15px;")
        urgency_btn = QPushButton("Urgency: Emergency")
        urgency_btn.setStyleSheet("font-size: 20px; padding: 15px;")

        layout.addWidget(bg_btn)
        layout.addWidget(comp_btn)
        layout.addWidget(units_btn)
        layout.addWidget(urgency_btn)

        notify_btn = QPushButton("📢 Notify Donors")
        notify_btn.setStyleSheet("font-size: 22px; padding: 20px; background-color: red; color: white;")
        notify_btn.clicked.connect(self.show_notifications)
        layout.addWidget(notify_btn)

        self.setLayout(layout)

    def show_notifications(self):
        donors = [
            {"name": "Arun", "blood_group": "O+", "phone": "999111222"},
            {"name": "Meera", "blood_group": "O-", "phone": "888222333"}
        ]
        message = "🚨 Donors Notified:\n\n"
        for d in donors:
            message += f"- {d['name']} ({d['blood_group']}) | Phone: {d['phone']}\n"
        message += "\nHospital: City Hospital\nUrgency: Emergency\nContact: +91-9876543210"
        QMessageBox.information(self, "Notifications Sent", message)

# --- Main Entry ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    sys.exit(app.exec_())