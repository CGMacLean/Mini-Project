from sqlite3 import Cursor
from menu_functions import refresh_screen
import pymysql
import os
from dotenv import load_dotenv


def print_list(list):
    for (i, item) in enumerate(list):
            print((i+1),item)

            
# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection

connection = pymysql.connect(
    host,
    user,
    password,
    database
    )

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
# cursor = connection.cursor()



# create table
# def create_table()
# cursor.execute(
# "CREATE TABLE Couriers (Courier_ID int PRIMARY KEY AUTO_INCREMENT, Courier_name varchar(255), Tel_No int)")



# print database
def DB_print(fieldnames):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {fieldnames[0]}")
    result = cursor.fetchall()
    for row in result:
        print(row)
    connection.commit()
    cursor.close()



# # insert into
def add_to_DB(fieldnames):
    cursor = connection.cursor()
    item_name = input(f'what {fieldnames[0]} do you wanna add?:')
    item_value = float(input(f'what {fieldnames[3]} should it be:'))
    sql = f"INSERT INTO {fieldnames[0]} ({fieldnames[2]},{fieldnames[3]}) VALUES ( %s, %s)"
    val = item_name, item_value
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()

def update_item_in_DB(fieldnames):
    while True:
        refresh_screen()
        DB_print(fieldnames)
        cursor = connection.cursor()
        item_ID = int(input(f'What is the {fieldnames[1]} you want to update?, or press 0 to exit:'))
        # product = input(f'what {fieldnames[0]} do you wanna add?:')
        if item_ID == 0:
            break
        else:
            while True:
                refresh_screen()
                DB_print(fieldnames)
                print_list(fieldnames[1:])
                update_choice = int(input('Press the index of the contect you will like to update or 0 to exit:'))
                if update_choice == 0:
                    break
                elif update_choice == 1:
                    cursor = connection.cursor()
                    new_ID = int(input('Pick a new id:'))
                    cursor.execute(f'''
                                UPDATE {fieldnames[0]}
                                SET {fieldnames[1]} = {new_ID}
                                WHERE {fieldnames[1]} = {item_ID}
                                ''')
                    connection.commit()
                    cursor.close()
                    item_ID = new_ID
                elif update_choice == 2:
                    cursor = connection.cursor()
                    new_name = input('What would should the name be?:')
                    cursor.execute(f'''
                                UPDATE {fieldnames[0]}
                                SET {fieldnames[2]} = '{new_name}'
                                WHERE {fieldnames[1]} = {item_ID}
                                ''')
                    connection.commit()
                    cursor.close()
                elif update_choice == 3:
                    cursor = connection.cursor()
                    item_number = float(input(f'what {fieldnames[3]} should it be:'))
                    cursor.execute(f'''
                                UPDATE {fieldnames[0]}
                                SET {fieldnames[3]} = {item_number}
                                WHERE {fieldnames[1]} = {item_ID}
                                ''')
                    connection.commit()
                    cursor.close()
            
            
            
def delete_item_in_DB(fieldnames):
    cursor = connection.cursor()
    item_ID = int(input(f'What is the {fieldnames[1]} you want to delete?:'))
    cursor.execute(f'''
                        DELETE FROM {fieldnames[0]}
                        WHERE {fieldnames[1]} = {item_ID}
                        ''')
    connection.commit()
    cursor.close()


# mycursor = mydb.cursor()

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")
    # UPDATE Customers
    # SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
    # WHERE CustomerID = 1;
# add_to_database(product_fieldnames)

# def add_couriers():
#     courier= input('what Courier do you wanna add?:')
#     tel_no = float(input('what number should it be:'))
    
#     sql = "INSERT INTO Courier ( Courier_name, Tel_No ) VALUES (%s, %s)"
#     val =courier,tel_no
#     cursor.execute(sql, val)
#     # '{0:.2f}'.format(2.5)
#     # fstring
    
# add_couriers()






# connection.commit()
# cursor.close()
# connection.close()


# cursor.execute(
#         "CREATE TABLE products (PersonID int PRIMARY KEY AUTO_INCREMENT, Customer_name varchar(255), Address varchar(255), Tel varchar(255), couriers varchar(255), order_status varchar(255))")