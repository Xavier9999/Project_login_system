"""Register Page"""
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QFormLayout, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox
import button_functions


class RWindow(QDialog):
    """Register window attributes"""
    def __init__(self):
        super().__init__()
        self.title = "Register"
        self.left = 800
        self.top = 400
        self.width = 300
        self.height = 300
        self.setFixedSize(self.width, self.height)
        self.init__register()

    def init__register(self):
        """Set window contents"""
        # Label content creation
        u_label = QLabel('<font size="4">Username</font>')
        e_label = QLabel('<font size="4">Email</font>')
        p_label = QLabel('<font size="4">Password</font>')
        # Lineedit creation
        self.u_lineedit = QLineEdit()
        self.e_lineedit = QLineEdit()
        self.p_lineedit = QLineEdit()
        # Hide password input
        self.p_lineedit.setEchoMode(QLineEdit.Password)
        # Create form layout
        form_layout = QFormLayout()
        # Form layout contents
        form_layout.setFormAlignment(QtCore.Qt.AlignCenter)
        form_layout.addRow(u_label, self.u_lineedit)
        form_layout.addRow(e_label, self.e_lineedit)
        form_layout.addRow(p_label, self.p_lineedit)
        # Create group box
        group_box = QGroupBox()
        group_box.setTitle("Fill in below")
        group_box.setLayout(form_layout)
        # Create buttons
        self.submit_button = QPushButton("Submit")
        self.login_button = QPushButton("Login")
        self.close_button = QPushButton("Close")
        # Connect button functions
        self.submit_button.clicked.connect(self.submit)
        self.close_button.clicked.connect(self.close_window)
        # Create horizontal layout
        h_layout = QHBoxLayout()
        # Horizontal layout contents
        h_layout.addWidget(self.submit_button)
        h_layout.addWidget(self.close_button)
        # Window layout contents
        win_layout = QVBoxLayout()
        win_layout.addWidget(group_box)
        win_layout.addLayout(h_layout)
        # Set window layout
        self.setLayout(win_layout)
        # Set window attributes
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def submit(self):
        """Submit button"""
        username = self.u_lineedit.text()
        password = self.p_lineedit.text()
        email = self.e_lineedit.text()
        values = (username, password, email)
        button_functions.XAVIER_DB.submit_db(values)
        results = button_functions.XAVIER_DB.fetch_db()
        print(results[-1])
        self.close()

    def close_window(self):
        """Close button"""
        self.close()
