import pyodbc

# Connect to database, can be exported into any function that needs 
def db_connect():
    print('Connecting to database...')
    pr_conn = pyodbc.connect('Driver={SQL Server};'
                             'Server=NWERP-SQL01\LOGOSTST;'
                             'Database=LogosTest;'
                             'Trusted_Connection=yes;')
    print('Connected to database')
    return pr_conn
