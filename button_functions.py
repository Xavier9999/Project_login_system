"""SQL database functions"""
import MySQLdb as mysql
from login_failed import LoginFailed


class ButtonClicked:
    """Set button class"""
    def __init__(self, login_db):
        self.host = "localhost"
        self.user = "root"
        self.passwd = "Yaoming229"
        self.login_db = login_db
        self.failed_ui = None

    def connect_db(self):
        conn = mysql.Connect(host=self.host, user=self.user, passwd=self.passwd, db=self.login_db)
        cursor = conn.cursor()
        # Executing with cursor
        cursor.execute("SELECT * FROM Login_info")
        # Get all the info from the table
        results = cursor.fetchall()
        return results

    def login_failed(self):
        """Login button for main page"""
        self.failed_ui = LoginFailed()
        self.failed_ui.show()


XAVIER_DB = ButtonClicked("Xavier")
