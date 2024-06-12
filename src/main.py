import os
import pypyodbc as podbc   
import pandas as pd 
import numpy as np 
import warnings
from IPython.display import display

warnings.filterwarnings('ignore')
def main():
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


    SQL_Query = pd.read_sql_query('''SELECT TOP 3 * FROM [dbo].[ufc-fighters-statistics]''', connection)
    SQL_Query.head()

    display(SQL_Query)

    connection.close()

if __name__ == "__main__":
    main()
