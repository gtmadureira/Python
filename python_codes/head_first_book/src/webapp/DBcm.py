"""
The UseDatabase context manager for working with MySQL/MariaDB.

Simple example usage:

    from DBcm import UseDatabase

    dbconfig = { 'host': '127.0.0.1',
                 'user': 'myUserid',
                 'password': 'myPassword',
                 'database': 'myDB' }

    with UseDatabase(dbconfig) as cursor:
        vSQL = "select * from log"
        cursor.execute(vSQL)
        data = cursor.fetchall()
        for row in data:
            print(row)

Python 3 only, due to type hints and new syntax.
"""

##############################################################################
#        Context manager for connecting/disconnecting to a database          #
##############################################################################

import mysql.connector


class UseDatabase:

    def __init__(self, config: dict) -> None:
        """Add the database configuration parameters to the object.

        This class expects a single dictionary argument which needs to assign
        the appropriate values to (at least) the following keys:

            host - the IP address of the host running MySQL/MariaDB.
            user - the MySQL/MariaDB username to use.
            password - the user's password.
            database - the name of the database to use.

        For more options, refer to the mysql-connector-python documentation."""
        self.configuration = config

    def __enter__(self) -> 'cursor':
        """Connect to database and create a DB cursor.

        Return the database cursor to the context manager."""
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        """Destroy the cursor as well as the connection (after committing)."""
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
