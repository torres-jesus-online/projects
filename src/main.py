import os
import pypyodbc as podbc   
import pandas as pd 
import warnings
warnings.filterwarnings('ignore')

# Connecting to local server.
con = podbc.connect("Driver={ODBC Driver 18 for SQL Server};"
                    "SERVER=THE-FATHER\SQLEXPRESS;"
                    "DATABASE=MMA-Stats;"
                    "Trusted_Connection=yes;"
                    "TrustServerCertificate=yes")

SQL_Query = pd.read_sql_query('''SELECT * FROM [dbo].[ufc-fighters-statistics]''', con)

SQL_Query.head()