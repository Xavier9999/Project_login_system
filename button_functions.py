"""SQL database functions"""
import MySQLdb as mysql
from login_failed import LoginFailed
from register_page import RWindow


class ButtonClicked:
    """Set button class"""
    def __init__(self, login_db):
        self.host = "localhost"
        self.user = "root"
        self.passwd = "Yaoming229"
        self.login_db = login_db
        self.failed_ui = None
        self.register_ui = None
        self.main_page = None

    def conn_db(self, values):
        """Database fetch function"""
        conn = mysql.Connect(host=self.host, user=self.user, passwd=self.passwd, db=self.login_db)
        cursor = conn.cursor()
        command = "INSERT INTO Login_info VALUES (%s, %s, %s, %s)"
        cursor.execute(command, values)

    def fetch_db(self):
        """Database fetch function"""
        conn = mysql.Connect(host=self.host, user=self.user, passwd=self.passwd, db=self.login_db)
        cursor = conn.cursor()
        # Executing with cursor
        cursor.execute("SELECT * FROM Login_info")
        # Get all the info from the table
        results = cursor.fetchall()
        return results

    def failed_window(self):
        """Login button for main page"""
        self.failed_ui = LoginFailed()
        self.failed_ui.show()

    def register_window(self):
        """Register button"""
        self.register_ui = RWindow()
        self.register_ui.show()


XAVIER_DB = ButtonClicked("Xavier")
