import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt

class BloodRequestWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blood Request")
        self.setGeometry(500, 200, 500, 600)
        self.setStyleSheet("background-color: white;")

        layout = QVBoxLayout()

        # Header
        header = QLabel("🚨 Emergency Blood Request")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 20px; font-weight: bold; color: red;")
        layout.addWidget(header)

        # --- Critical Core with Buttons ---
        layout.addWidget(QLabel("Select Blood Group:"))
        blood_groups = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
        bg_layout = QHBoxLayout()
        for bg in blood_groups:
            btn = QPushButton(bg)
            btn.clicked.connect(lambda _, g=bg: self.show_selection("Blood Group", g))
            bg_layout.addWidget(btn)
        layout.addLayout(bg_layout)

        layout.addWidget(QLabel("Select Component Needed:"))
        components = ["Whole Blood", "Platelets", "Plasma", "RBCs"]
        comp_layout = QHBoxLayout()
        for comp in components:
            btn = QPushButton(comp)
            btn.clicked.connect(lambda _, c=comp: self.show_selection("Component", c))
            comp_layout.addWidget(btn)
        layout.addLayout(comp_layout)

        layout.addWidget(QLabel("Units Required:"))
        units_layout = QHBoxLayout()
        for i in [1, 2, 3, 4, 5]:
            btn = QPushButton(f"{i} Units")
            btn.clicked.connect(lambda _, u=i: self.show_selection("Units", str(u)))
            units_layout.addWidget(btn)
        layout.addLayout(units_layout)

        layout.addWidget(QLabel("Urgency Level:"))
        urgency_layout = QHBoxLayout()
        for urgency in ["Emergency", "Urgent", "Planned"]:
            btn = QPushButton(urgency)
            btn.clicked.connect(lambda _, u=urgency: self.show_selection("Urgency", u))
            urgency_layout.addWidget(btn)
        layout.addLayout(urgency_layout)

        # --- Action Buttons ---
        call_button = QPushButton("📞 Call Coordinator")
        share_button = QPushButton("📤 Share to WhatsApp")
        navigate_button = QPushButton("🗺️ Navigate to Hospital")

        call_button.clicked.connect(lambda: self.quick_action("Calling Coordinator..."))
        share_button.clicked.connect(lambda: self.quick_action("Sharing request to WhatsApp..."))
        navigate_button.clicked.connect(lambda: self.quick_action("Opening hospital location..."))

        layout.addWidget(call_button)
        layout.addWidget(share_button)
        layout.addWidget(navigate_button)

        # Disclaimer
        disclaimer = QLabel("⚠️ Please do not pay anyone for blood donation. It is a voluntary act.")
        disclaimer.setAlignment(Qt.AlignCenter)
        disclaimer.setStyleSheet("font-size: 12px; color: gray;")
        layout.addWidget(disclaimer)

        self.setLayout(layout)

    def show_selection(self, category, value):
        QMessageBox.information(self, "Selection Made", f"{category}: {value}")

    def quick_action(self, message):
        QMessageBox.information(self, "Action", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BloodRequestWindow()
    window.show()
    sys.exit(app.exec_())