from connect_to_db import db_connect
import csv
# What we need

# Create fieldnames for CSV file
def create_fieldnames():
    fieldnames = ['OrgGroupCodeDesc', 'ContractNumber1', 'CentralNameLname1', 'CentralNameFname',
              'ContractTitle1', 'CurrentContractStartDate', 'CurrentContractEndDate', 'CurrentContractAmount']
    return fieldnames

# Create and open CSV File and Writer
def create_csv_file():
    report_csv = open('report.csv', 'w', newline='')
    report_writer = csv.DictWriter(report_csv, fieldnames=create_fieldnames)
    report_writer.writeheader()


# Connect to the Database
db_conn = db_connect()
db_conn_cursor = db_conn.cursor()

# Get all from Org Group
db_conn_cursor.execute("SELECT * FROM dbo.OrgGroup")
groups = db_conn_cursor.fetchall()
groups_col = [column[0] for column in db_conn_cursor.description]

# Get all from Org Structures
db_conn_cursor.execute("SELECT * FROM dbo.OrgStructure")
structures = db_conn_cursor.fetchall()
structures_col = [column[0] for column in db_conn_cursor.description]

# Get all from Contracts
db_conn_cursor.execute("SELECT * FROM dbo.Contract")
contracts = db_conn_cursor.fetchall()
contracts_col = [column[0] for column in db_conn_cursor.description]

# Get all from Vendor Contracts
db_conn_cursor.execute('SELECT * FROM dbo.VendorContract')
vendor_contracts = db_conn_cursor.fetchall()
vendor_contracts_col = [column[0] for column in db_conn_cursor.description]

# Get all from Vendor
db_conn_cursor.execute("SELECT * FROM dbo.Vendor")
vendors = db_conn_cursor.fetchall()
vendors_col = [column[0] for column in db_conn_cursor.description]

# Get All From Central Name
db_conn_cursor.execute("SELECT * FROM dbo.CentralName")
central_names = db_conn_cursor.fetchall()
central_names_col = [column[0] for column in db_conn_cursor.description]


# Get Level One and Two Information Functions
def get_level_two_information(structure):
    for group in groups:
        if structure[2] == group[0]:
            level_2 = str(structure[2])
            org_group_code = str(group[3])
            org_group_code_desc = str(group[4])
            return level_2, org_group_code, org_group_code_desc


def get_level_one_information(structure):
    for group in groups:
        if structure[1] == group[0]:
            level_1 = str(structure[1])
            org_group_code = str(group[3])
            org_group_desc = str(group[4])
            return level_1, org_group_code, org_group_desc


# Get All Contracts
def get_all_contracts_to_csv():
    for contract in contracts:
        for structure in structures:
            # Get level 2 variables
            if structure[2] is not None:
                two_id, two_code, two_code_desc = get_level_two_information(structure)
            # Get level 1 variables
            one_id, one_code, one_code_desc = get_level_one_information(structure)
            try:
                concat_name = str(one_code) + '-' + str(two_code) + \
                    ' ' + one_code_desc + ',' + two_code_desc
            except:
                concat_name = str(one_code) + '-' + \
                    str(one_code_desc) + ' ' + one_code_desc
            if contract[7] == structure[0]:
                report_writer.writerow({
                    'OrgGroupCodeDesc': concat_name,
                    'ContractNumber1': contract[2],
                    'CentralNameLname1': 'Central Name',
                    'CentralNameFname': 'Central Name 2',
                    'ContractTitle1': contract[3],
                    'CurrentContractStartDate': contract[13],
                    'CurrentContractEndDate': contract[14],
                    'CurrentContractAmount': contract[15]
                })
