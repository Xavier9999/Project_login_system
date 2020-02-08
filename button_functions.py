"""SQL database functions"""
import MySQLdb as mysql


class ButtonClicked:
    """Set button class"""
    def __init__(self, host, user, passwd, login_db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.login_db = login_db

    def login(self):
        """Login button for main page"""
        conn = mysql.Connect(host=self.host, user=self.user, passwd=self.passwd, db=self.login_db)
        cursor = conn.cursor()
        # Executing with cursor
        cursor.execute("SELECT * FROM Login_info")
        # Get all the info from the table
        results = cursor.fetchall()
        print([i for i in results])
        conn.close()


LOGINCHECK = ButtonClicked("localhost", "root", "Yaoming229", "Password_keeper")
