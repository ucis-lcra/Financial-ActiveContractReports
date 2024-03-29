from datetime import datetime
import csv
import pandas as pd

from scripts.connect_to_db import db_connect

def create_fieldnames():
    fieldnames = ['OrgGroupCode', 'OrgGroupCodeDesc', 'ContractNumber1', 'CentralNameLname1', 'CentralNameFname',
                  'ContractTitle1', 'CurrentContractStartDate', 'CurrentContractEndDate', 'CurrentContractAmount']
    return fieldnames


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
def get_all_contracts_to_csv(start_date, end_date):

    # Search through the Database with the given dates and get all the contracts within the required times
    db_conn_cursor.execute("SELECT * FROM dbo.Contract WHERE ProcessStatus = '2' AND CurrentContractStartDate <= '" + start_date + "' AND CurrentContractEndDate > '" + end_date + "'")
    contracts = db_conn_cursor.fetchall()

    # Create TimeStamp
    time = datetime.now()
    time_stamp = time.strftime("%Y-%m-%d-%H-%M")

    # Create CSV File
    report_csv = open('./static/data/report-'+time_stamp+'.csv', 'w', newline='')
    report_path = './static/data/report-'+time_stamp+'.csv'
    report_writer = csv.DictWriter(report_csv, fieldnames=create_fieldnames())
    report_writer.writeheader()

    for contract in contracts:
        for structure in structures:
            # Get level 2 variables
            if structure[2] is not None:
                two_id, two_code, two_code_desc = get_level_two_information(
                    structure)
                one_id, one_code, one_code_desc = get_level_one_information(
                structure)
                concat_name = str(one_code) + '-' + str(two_code) + \
                    ' ' + one_code_desc + ',' + two_code_desc
            # Get level 1 variables
            else:
                one_id, one_code, one_code_desc = get_level_one_information(structure)
                concat_name = str(one_code) + '-' + str(one_code_desc)
            if contract[7] == structure[0]:
                # Now we need to get the first and last name from CentralName Table
                name_key = int(contract[18])
                db_conn_cursor.execute(
                    "(SELECT dbo.CentralName.LastName, dbo.CentralName.FirstName FROM dbo.CentralName WHERE dbo.CentralName.CentralNameID = (SELECT dbo.Vendor.CentralNameID FROM dbo.Vendor WHERE dbo.Vendor.VendorID = '" + str(name_key) + "'))")
                vendors = db_conn_cursor.fetchall()
                for row in vendors:
                    last_name = str(row[0])
                    first_name = str(row[1])
                    if first_name == 'None':
                        first_name = ' '
                    else:
                        first_name = str(row[1])
                        
                # Formate Date Correctly
                start_date = contract[13].strftime('%m/%d/%Y')
                end_date = contract[14].strftime('%m/%d/%Y')
                contract_amount = '$' + str(contract[15])
                report_writer.writerow({
                    'OrgGroupCode': one_code_desc,
                    'OrgGroupCodeDesc': concat_name,
                    'ContractNumber1': contract[2],
                    'CentralNameLname1': last_name,
                    'CentralNameFname': first_name,
                    'ContractTitle1': contract[3],
                    'CurrentContractStartDate': start_date,
                    'CurrentContractEndDate': end_date,
                    'CurrentContractAmount': contract_amount
                })

    csv_sort = pd.read_csv(report_path, encoding= 'unicode_escape')
    csv_sort.sort_values(by=['OrgGroupCode','OrgGroupCodeDesc','ContractNumber1'], inplace=True)
    csv_sort.to_csv(report_path, index=False)

    return report_path

