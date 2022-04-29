from connect_to_db import db_connect

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

def get_level_two_information():
    for group in groups:
            if structure[2] == group[0]:
                level_2 = str(structure[2]) 
                org_group_code = str(group[3]) 
                org_group_code_desc = str(group[4])
                return level_2, org_group_code, org_group_code_desc

def get_level_one_information():
    for group in groups:
            if structure[1] == group[0]:
                level_1 = str(structure[1])
                org_group_code = str(group[3])
                org_group_desc = str(group[4])
                return level_1, org_group_code, org_group_desc


for structure in structures:
    # Get level 2 variables
    if structure[2] is not None:
        two_id, two_code, two_code_desc = get_level_two_information()
    # Get level 1 variables
    one_id, one_code, one_code_desc = get_level_one_information()
    try:
        concat_name = str(one_code) + '-' + str(two_code) + ' ' + one_code_desc + ',' + two_code_desc 
    except:
        concat_name = str(one_code) + '-' + str(one_code_desc) + ' ' + one_code_desc
    print(concat_name)






# Check titles imported properly
# for group in groups_col:
#     print(group)

# for structure in structures_col:
#     print(structure)

# OrgGroup 
# [0][0] OrgGroupID Equivalent to Level1ID or Level2ID
# [0][3] OrgGroupcode
# [0][4] OrgGroupCodeDesc

# OrgStructure 
# [0][0] = OrgStructureID
# [0][1] = Level1ID
# [0][2] = Level2ID
# [0][3] = Level3ID
# [0][4] = Level4ID
# [0][5] = Level5ID
# [0][6] = Level6ID