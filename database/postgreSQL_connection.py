from psycopg2 import pool


class Database:
    """Create a database connection with arguments given to the initialise method:
    Database.initialise(database=database_name,
                        user=user_name,
                        password=user_password,
                        host=host_name,
                        port=5432)
    """
    __connection_pool = None

    @staticmethod
    def initialise(**kwargs):
        """database, user, password, host, port arguments should be given.
        10 connections wil be available"""
        Database.__connection_pool = pool.SimpleConnectionPool(1, 10, **kwargs)

    @staticmethod
    def get_connection():
        return Database.__connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        Database.__connection_pool.putconn(connection)

    @staticmethod
    def close_all_connections():
        Database.__connection_pool.closeall()


class CursorFromConnectionPool:
    """A class that create a cursor from the connection pool, execute it if there is no error and close it after."""
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = Database.get_connection()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:
            self.conn.rollback()
        else:
            self.cursor.close()
            self.conn.commit()
        Database.return_connection(self.conn)
