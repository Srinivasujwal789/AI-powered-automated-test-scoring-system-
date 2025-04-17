from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class ScoringGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Scoring System")
        self.setGeometry(100, 100, 800, 600)

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Display USN and marks
        self.usn_label = QLabel("USN: Not Detected")
        self.marks_label = QLabel("Marks: Not Detected")
        self.total_label = QLabel("Total: Not Detected")
        self.status_label = QLabel("Status: Ready")

        # Edit button
        self.edit_button = QPushButton("Edit Marks")
        self.edit_button.clicked.connect(self.edit_marks)

        # Add widgets to layout
        self.layout.addWidget(self.usn_label)
        self.layout.addWidget(self.marks_label)
        self.layout.addWidget(self.total_label)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.edit_button)

    def update_display(self, usn, marks, total, status):
        self.usn_label.setText(f"USN: {usn}")
        self.marks_label.setText(f"Marks: {marks}")
        self.total_label.setText(f"Total: {total}")
        self.status_label.setText(f"Status: {status}")
        self.status_label.setStyleSheet("color: green" if status == "Valid" else "color: red")

    def edit_marks(self):
        # Placeholder for mark editing logic
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScoringGUI()
    window.show()
    sys.exit(app.exec_())
