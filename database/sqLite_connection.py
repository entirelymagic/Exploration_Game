import sqlite3


# it is not going to be used
class DatabaseConnectionsSQLite:
    """Create a Database Connection Object that take a host as a database and return the connection"""

    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_type or exc_val:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

