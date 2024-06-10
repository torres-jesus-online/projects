import pypyodbc as podbc    

# Connecting to local server.
connection = podbc.connect("Driver={SQL Server native Client 11.0};"
                      "Server=THE-FATHER\SQLEXPRESS;"
                      "Database=MMA Stats;"
                      "Trusted_Connection=yes;")

