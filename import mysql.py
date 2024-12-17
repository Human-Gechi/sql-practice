import mysql.connector
conn = mysql.connector.connect(
    host="*****",
    user="*****",
    password=input("Enter your MySQL password: "),
    database="AKINTOLAHALL2023_2024SESSION"
)
cur_sor = conn.cursor()
def create_table():
    cur_sor.execute('''
        CREATE TABLE IF NOT EXIST akintolahall20232024session(
        block_name VARCHAR(255),
        floor_number VARCHAR(255),
        room_number VARCHAR(3),
        occupant_name VARCHAR(255),
        occupant_bed_no INT(1),
        occupant_phone_number VARCHAR(13),
        status VARCHAR(15),        
        faculty varchar(255),
        department varchar(255)
)
''')
def input_data():
    block_name = input("Enter block name here: ").title()
    floor_number = input("Enter floor name here: ").upper()
    room_number = int(input("Enter room number here: "))
    occupant_name = input("Enter name here: ").title()
    occupant_bed_no = int(input("Enter bed number here: "))
    occupant_phone_number = input("Enter occupant phone number here: ")
    status = input("PAID or NOT PAID: ").upper()
    faculty = input("enter faculty name here please:").title()
    department = input("Enter department name here:").title()
    query = """
    INSERT INTO akintolahall20232024session (block_name, floor_number, room_number, occupant_name, occupant_bed_no, occupant_phone_number, status,faculty,department)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
    """
    data = (block_name, floor_number, room_number, occupant_name, occupant_bed_no, occupant_phone_number, status,faculty,department)
    cur_sor.execute(query, data)
    conn.commit()
    print("Data updated successfully")
def search_data():
    query = "SELECT * FROM akintolahall20232024session WHERE occupant_name LIKE %s"
    occupantname = '%' + input("Enter occupant name:") +'%'
    cur_sor.execute(query,(occupantname,))
    result = cur_sor.fetchall()
    for row in result:
        print(f"Block_name:{row[0]}\nFloor_number:{row[1]}\nRoom_number:{row[2]}\nOccupant_name:{row[3]}\nOccupant_bed_no:{row[4]}\nOccupant_phonenumber{row[5]}\nStatus:{row[6]}")
def delete_data():
    block_name = input("Enter block name here: ").title()
    floor_number = input("Enter floor name here: ").upper()
    room_number = int(input("Enter room number here: "))
    occupant_name = input("Enter name here: ").title()
    occupant_bed_no = int(input("Enter bed number here: "))
    occupant_phone_number = input("Enter occupant phone number here: ")
    status = input("PAID or NOT PAID: ").upper()
    faculty = input("Enter your faculty name here:")
    department = input("Enter the name of your department here:")
    query = """
    DELETE FROM akintolahall20232024session WHERE block_name = %s AND floor_number= %s AND room_number=%s AND occupant_name = %s AND occupant_bed_no= %s AND occupant_phone_number = %s AND status=%s AND fauculty = %s AND department = %s
   """
    data = (block_name, floor_number, room_number, occupant_name, occupant_bed_no, occupant_phone_number, status,faculty,department)
    cur_sor.execute(query,data)
    conn.commit()
    print("Rows deleted successfully")
choice = input("WHAT DO YOU WANT TO DO (1:UPDATE,2:SEARCH, 3:DELETE)")
if choice == '1':
    input_data()
elif choice == '2':
    search_data()
elif choice == '3':
    delete_data()
else:
    print("That ends it")