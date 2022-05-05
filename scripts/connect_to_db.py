import pyodbc

# Connect to database, can be exported into any function that needs 
def db_connect():

    # Test Data Base
    # print('Connecting to database...')
    # pr_conn = pyodbc.connect('Driver={SQL Server};'
    #                          'Server=NWERP-SQL01\LOGOSTST;'
    #                          'Database=LogosTest;'
    #                          'Trusted_Connection=yes;')
    # print('Connected to database')
    # return pr_conn

    # # Production Data Base
    print('Connecting to database...')
    pr_conn = pyodbc.connect('Driver={SQL Server};'
                             'Server=NWERP-SQL01\LOGOSPRD;'
                             'Database=LogosDB;'
                             'Trusted_Connection=yes;')
    print('Connected to database')
    return pr_conn