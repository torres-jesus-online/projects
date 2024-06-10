import os
import pypyodbc as podbc   
import pandas as pd 
import numpy as np 
import warnings

warnings.filterwarnings('ignore')

# Connecting to local server.
DRIVER_NAME = 'ODBC Driver 18 for SQL Server'
SERVER_NAME = 'THE-FATHER\SQLEXPRESS'
DATABASE_NAME = 'MMA-Stats'
connection_string =f"""
            Driver={{{DRIVER_NAME}}};
            SERVER={SERVER_NAME};
            DATABASE={DATABASE_NAME};
            Trusted_Connection=yes;
            TrustServerCertificate=yes;"""
connection = podbc.connect(connection_string)

cursor = connection.cursor() 
cursor.execute('SELECT TOP 3 * FROM [dbo].[ufc-fighters-statistics]')
for row in cursor.fetchall():
    print(row)

print(connection)


# SQL_Query = pd.read_sql_query('''SELECT TOP 3 * FROM [dbo].[ufc-fighters-statistics]''', connection)


# SQL_Query.head()