"""Register Page"""
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QFormLayout, QPushButton, QHBoxLayout, QVBoxLayout


class RWindow(QDialog):
    """Register window attributes"""
    def __init__(self):
        super().__init__()
        self.title = "Register"
        self.left = 800
        self.top = 250
        self.width = 300
        self.height = 600
        self.setFixedSize(300, 600)
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
        form_layout.addRow(u_label, self.u_lineedit)
        form_layout.addRow(e_label, self.u_lineedit)
        form_layout.addRow(p_label, self.p_lineedit)
        # Create buttons
        self.submit_button = QPushButton("Submit")
        self.login_button = QPushButton("Login")
        self.close_button = QPushButton("Close")
        # Connect button functions
        self.submit_button.clicked.connect(self.submit)
        self.login_button.clicked.connect(self.login_window)
        self.close_button.clicked.connect(self.close)
        # Create horizontal layout
        h_layout = QHBoxLayout()
        # Horizontal layout contents
        h_layout.addWidget(self.submit_button)
        h_layout.addWidget(self.login_button)
        h_layout.addWidget(self.close_button)
        # Window layout contents
        win_layout = QVBoxLayout()
        win_layout.addLayout(form_layout)
        win_layout.addLayout(h_layout)
        # Set window layout
        self.setLayout(win_layout)
        # Set window attributes
        self.setWindowTitle(self.title)
        self.setGeometry(800, 250, 300, 600)
        self.show()

    def submit(self):
        """Submit button"""
        pass

    def login_window(self):
        """Login button"""
        pass

    def close(self):
        """Close button"""
        self.close()
