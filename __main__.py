"""Main page"""
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QFormLayout, QGroupBox, QVBoxLayout, QHBoxLayout, QLineEdit
import button_functions


class Window(QDialog):
    """Main window attributes"""
    def __init__(self):
        super().__init__()
        self.title = "Login System"
        self.icon = 'Login.png'
        self.left = 800
        self.top = 400
        self.width = 300
        self.height = 300
        self.setFixedSize(self.width, self.height)
        self.init_window()

    def init_window(self):
        """Main window widgets creation"""
        # Label content creation
        u_label = QLabel('<font size="4">Username</font>')
        p_label = QLabel('<font size="4">Password</font>')
        # Line edit creation
        self.u_lineedit = QLineEdit()
        self.p_lineedit = QLineEdit()
        # Hide password input
        self.p_lineedit.setEchoMode(QLineEdit.Password)
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
        # Retrieve username and password from input
        username = self.u_lineedit.text()
        password = self.p_lineedit.text()
        # Call the Login check functions from button_functions.py
        results = button_functions.XAVIER_DB.connect_db()
        for i in results:
            if username in i and password == i[2]:
                print("Login succesfull!")
                break
            else:
                button_functions.XAVIER_DB.failed_window()

    def click_register(self):
        """Set register function"""
        button_functions.XAVIER_DB.register_window()


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    STYLE = 'resources/main_window_style.css'
    with open(STYLE, "r") as fh:
        APP.setStyleSheet(fh.read())
    WINDOW = Window()
    sys.exit(APP.exec())
