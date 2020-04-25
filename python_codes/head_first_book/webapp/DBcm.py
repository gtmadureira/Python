"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



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



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6jlaIACgkQBXQppWFa
stmrsw/+P01+r3UCzs+sApdLwjtjYNIBzvTXzPeNi3Ip0iBDIvkEdX4JkemGbFrD
zWG64I4Bxsavn8cRbuapIJW8O7MvOiGHKWPFqnCSEUkCEhE4+974nz+Hz/flphre
egbJDLsUD92khh5K2GOYgm6QX/N8H9kFwmiOnkfsOQnpZts1wKR2zkMRbBhD2GTN
qtxd4+GymwI+vMKNCCqRDgaHKXi3KOmdd+wmfF3fl51goI0vsqnUuMs8RzzMetEK
cex+ub+MBHHumhS6kX8FHsU9sWUMyKQrD3l2EgiTAjRzovApW7IjPH+LkQLvKHTi
56m/NKvwomhUUGsezd7315D2Ye2cpsXAwQtepSNRKDnHD4CCbl72SKnVGUfpC9tR
8wt32leOFrJFEsepwiHBv3dOR2e4m7z5rgeWvPOtkxVj3ohuRt7ojLgODUh7vqTv
K7baOS+ctRGN5TvyqPzmWY5hQF7sDvm62YWEQECrtRBqiMsDIutoWoJ+ynqyfine
C5txpo/NL9Opq7yhByMuAVKZaNAOVerNN3XSWPbJx2XKQowIBdviQt9g9mYDkG94
tl3xtJnF/8OjZryZp9vj0JHdJVBOnyMPsFBySZjekT1Y6hjUH9BaedzzB8TNirLb
UHQXdKtddNdjsgiAg71YiwzV2xbe+4CVzBlP1QibTwUQtBEKpgU=
=k0/Y
-----END PGP SIGNATURE-----

"""
