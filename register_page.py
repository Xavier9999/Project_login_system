"""Register Page"""
import sys
from PyQt5.QtWidgets import QWidget


class RWindow(QWidget):
    """Register window attributes"""
    def __init__(self):
        super().__init__()
        self.title = "Register"
        self.left = 800
        self.top = 250
        self.width = 300
        self.height = 600
        self.setMaximumSize(300, 600)
        self.init__widget()

    def init__widget(self):
        self.setGeometry(800, 250, 300, 600)
        self.show()
