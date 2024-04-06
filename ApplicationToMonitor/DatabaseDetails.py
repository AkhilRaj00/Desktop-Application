# SQL Connection #
DRIVER = 'SQL Server'
SERVER_NAME = 'DESKTOP-PGJ98K8'
DATABASE_NAME = 'workProgress'

conn_string = f"""
            Driver={{{DRIVER}}};
            Server={SERVER_NAME};
            Database={DATABASE_NAME};
            Trust_Connection=yes;
        """