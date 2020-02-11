"""Login failed pop-up page"""
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class LoginFailed(QDialog):
    """Dialog attributes"""
    def __init__(self):
        super().__init__()
        self.title = "Message"
        self.left = 800
        self.top = 400
        self.width = 300
        self.height = 150
        self.setFixedSize(300, 150)
        self.init_dialog()

    def init_dialog(self):
        """Dialog content creation"""
        # Create text
        label = QLabel('<font size="6">Login failed</font>')
        label.setAlignment(QtCore.Qt.AlignCenter)
        # Create buttons
        self.register_button = QPushButton("Register")
        self.close_button = QPushButton("Close")
        # Register and close button connection
        self.register_button.clicked.connect(self.click_register)
        self.close_button.clicked.connect(self.click_close)
        # Create button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.register_button)
        button_layout.addWidget(self.close_button)
        # Create dialog layout
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)
        dialog_layout.addLayout(button_layout)
        # Setting the dialog layout
        self.setLayout(dialog_layout)
        # Setting dialog attributes
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def click_register(self):
        """Set register function"""
        pass

    def click_close(self):
        """Set close function"""
        self.close()


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    WIN = LoginFailed()
    sys.exit(APP.exec())
