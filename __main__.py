"""Main page"""
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFormLayout, QGroupBox, QVBoxLayout, QHBoxLayout, QLineEdit
import button_functions


class Window(QWidget):
    """Main window attributes"""
    def __init__(self):
        super().__init__()
        self.title = "Password Keeper"
        self.icon = 'Login.png'
        self.top = 400
        self.left = 800
        self.width = 300
        self.height = 150
        self.init_window()

    def init_window(self):
        """User form Label creation"""
        u_label = QLabel('<font size="4">Username</font>')
        p_label = QLabel('<font size="4">Password</font>')
        self.u_lineedit = QLineEdit()
        self.p_lineedit = QLineEdit()
        # User form layout
        form_layout = QFormLayout()
        form_layout.addRow(u_label, self.u_lineedit)
        form_layout.addRow(p_label, self.p_lineedit)
        # Groupbox the user form"
        group_box = QGroupBox()
        group_box.setTitle("Login or sign up below")
        group_box.setLayout(form_layout)
        # Register and Login button creation
        self.register_button = QPushButton("Register")
        self.login_button = QPushButton("Login")
        # Register and Login button connection
        self.register_button.clicked.connect(self.click_register)
        self.login_button.clicked.connect(self.click_login)
        # Register and Login button layout
        h_box = QHBoxLayout()
        h_box.addWidget(self.login_button)
        h_box.addWidget(self.register_button)
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addStretch(0)
        main_layout.addWidget(group_box)
        main_layout.addStretch(0)
        main_layout.addLayout(h_box)
        self.setLayout(main_layout)
        # Pass in Window attributes
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))  # Why doesn't this work?
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def click_login(self):
        """Set login function"""
        button_functions.LOGINCHECK.login()

    def click_register(self):
        """Set register function"""


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    STYLE = '/Users/xavierchu/Documents/Coding/VScode/Python/Python/Projects/Password_keeper/resources/main_window_style.css'
    with open(STYLE, "r") as fh:
        APP.setStyleSheet(fh.read())
    WINDOW = Window()
    sys.exit(APP.exec())
