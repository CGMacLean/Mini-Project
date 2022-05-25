
from menu_functions import refresh_screen, display_timer, exit_to_menu
import os
import pymysql
import csv
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


# create table
# def create_table():
#     cursor = connection.cursor()
#     Table_name = input('Name of the table:')
#     Primary_Key = input('Name of Primary Key, ie Order_ID:')
#     Column_name = input('Name of first column:')
#     sql = f"CREATE TABLE {Table_name} ({Primary_Key} int PRIMARY KEY AUTO_INCREMENT, {Column_name} varchar(255))"
#     cursor.execute(sql)
#     connection.commit()
#     cursor.close()
# create_table()


# print database
def db_print_all_from(fieldnames):
    cursor = connection.cursor()
    # select everything from table given
    cursor.execute(f"SELECT * FROM {fieldnames[0]}")
    result = cursor.fetchall()
    for row in result:
            print(row)
    connection.commit()
    cursor.close()
    
def db_print_row_by_id(fieldnames, item_ID):
    cursor = connection.cursor()
    # slelect row from table where ID matches input
    cursor.execute(f"SELECT * FROM {fieldnames[0]} WHERE {fieldnames[1]} = {item_ID}")
    result = cursor.fetchall()
    for row in result:
            print(row)
    connection.commit()
    cursor.close()
    

def db_print_lat_row(fieldnames):
    cursor = connection.cursor()
    # selects everything but sorts (order by) decending by ID and limits by one
    cursor.execute(f"SELECT * FROM {fieldnames[0]} ORDER BY {fieldnames[1]} DESC LIMIT 1")
    result = cursor.fetchall()
    for row in result:
            print(row)
    connection.commit()
    cursor.close()
    
def db_print_specific(fieldnames, column_index , ID_value):
    cursor = connection.cursor()
    # takes the table column index and print at the correspoding id 
    cursor.execute(f"SELECT  {fieldnames[column_index]} FROM {fieldnames[0]} WHERE {fieldnames[1]} = {ID_value};")
    retrieved = cursor.fetchone()
    retrieved_item = retrieved[0]
    print(retrieved_item)
    connection.commit()
    cursor.close()

    
def add_to_DB(fieldnames):
    while True:
        refresh_screen()
        # ask for the name of the itme to be added
        item_name = input(f'What {fieldnames[0]} do you wanna add?, or press 0 to exit:')
        # proving an exit path
        if item_name == '0':
            print('back to menu')
            break
        else:
            while True:
                # ask for a nuber value for Price or tel_no in this case depending on th feildname
                item_value = float(input(f'What {fieldnames[3]} should it be, or press 0 to exit:')) 
                if item_value == 0:
                    print('back to menu')
                    display_timer(2)
                    break
                else:
                    # connect to DB and set the cursor
                    cursor = connection.cursor()
                    # slq is the command to run and val are the values to be added at the column header with of feildnames
                    sql = f"INSERT INTO {fieldnames[0]} ({fieldnames[2]},{fieldnames[3]}) VALUES ( %s, %s)"
                    val = item_name, item_value
                    cursor.execute(sql, val)
                    connection.commit()
                    cursor.close()
                    return item_name
                        
                        

def update_item_in_DB(fieldnames):
    while True:
        refresh_screen()
        # GET all coloumns entrys from feildnames table and print
        db_print_all_from(fieldnames)
        # ask which entry to be updated
        item_ID = int(input(f'What is the {fieldnames[1]} you want to update?, or press 0 to exit:'))
        if item_ID == 0:
            break
        else:
            while True:
                refresh_screen()
                db_print_row_by_id(fieldnames,item_ID)
                # print the options avalible for update exculding Table name
                print_list(fieldnames[1:])
                update_choice = int(input('Press the index of the contect you will like to update or 0 to exit:'))
                if update_choice == 0:
                    break
                elif update_choice == 1:
                    # GET user input for new ID and update database
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
                    # GET user input for new name and update database
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
                    # GET user input for new number 
                    # this only works for both because they both have numbers output in the same position in feildnames
                    cursor = connection.cursor()
                    item_number = float(input(f'What {fieldnames[3]} should it be:'))
                    cursor.execute(f'''
                                UPDATE {fieldnames[0]}
                                SET {fieldnames[3]} = {item_number}
                                WHERE {fieldnames[1]} = {item_ID}
                                ''')
                    connection.commit()
                    cursor.close()
            
            
            
def delete_item_in_DB(fieldnames):
    while True:
        cursor = connection.cursor()
        item_ID = int(input(f'What is the {fieldnames[1]} you want to delete?:'))
        if item_ID == 0:
            break
        else:
            cursor.execute(f'''
                                DELETE FROM {fieldnames[0]}
                                WHERE {fieldnames[1]} = {item_ID}
                                ''')
            connection.commit()
            cursor.close()
            print('The item has been deleted')
            return
            
            
def Add_to_basket(product_fieldnames):
    item_list = []
    while True:
        refresh_screen()
        db_print_all_from(product_fieldnames)
        print(f'your items are {item_list}')
        basket = input('Pick a products by ID when your happy just press enter or press 0 only to exit:')
        item_list.append(basket)
        if basket == '0':
            print('back to menu')
            return
        elif basket == '':
            if len(item_list) == 0:
                print('No items in basket')
            else:
                # remove last enter input forcing a comma
                del item_list[-1]
                # join basket items to Items for DB
                Items = ', '.join(item_list)
                print(Items)
                return Items
        else:
            print('Add another? or press enter to continue')
            
        
            
def Add_customer_name():
    while True:
        Customer_name = input('Please add your name?, or press 0 to exit:')
        if Customer_name == '0':
            print('back to menu')
            break
        else:
            return Customer_name
        
        
def Add_Customer_Address():
    while True:
        Customer_Address = input('What should the delivery address be?, or press 0 to exit:')
        if Customer_Address == '0':
            print('back to menu')
            display_timer(2)
            break
        else:
            return Customer_Address
           

def Add_customer_Phone():
    while True:
        Customer_Phone = int(input('What phone number should we use?, or enter 0 only to exit:'))
        if Customer_Phone == '0':
            print('back to menu')
            display_timer(2)
            return
        else:
            return Customer_Phone
        
        
def Pick_A_Courier(courier_fieldnames):
    db_print_all_from(courier_fieldnames)
    couriers = int(input('Pick courier by ID, or 0 to exit'))   
    if couriers == 0:
            print('back to menu')
            display_timer(2)
            return
    else:
        return couriers
        
def add_order_to_database(order_fieldnames,product_fieldnames,courier_fieldnames):
    while True:
        Customer_name = Add_customer_name()
        Customer_Address = Add_Customer_Address()
        Customer_Phone = Add_customer_Phone()
        Items = Add_to_basket(product_fieldnames)
        Couriers = Pick_A_Courier(courier_fieldnames)
        Order_Status = 1
        cursor = connection.cursor()
        sql = f"INSERT INTO {order_fieldnames[0]} ({order_fieldnames[2]},{order_fieldnames[3]},{order_fieldnames[4]},{order_fieldnames[5]},{order_fieldnames[6]},{order_fieldnames[7]}) VALUES ( %s , %s , %s , %s , %s , %s)"
        val = Customer_name, Customer_Address, Customer_Phone, Couriers,Order_Status, Items
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()
        return print(f'Your itmes are {Items}, we are preparing them now, Have a Great Day :)')


def update_order_status_in_DB(order_fieldnames,Order_Status_feildnames):
    refresh_screen()
    # GET all orders from orders table and print
    db_print_all_from(order_fieldnames)
    # GET user input for order ID
    input_order_ID = int(input('Pick order by ID or press 0 to exit:'))
    while True:
        refresh_screen()
        if input_order_ID == 0:
            break
        else:
            # GET all order statuses from order_status table and print
            db_print_all_from(Order_Status_feildnames)
            cursor = connection.cursor()
             # GET user input for the updated order status ID
            new_ID = int(input('Pick a new order by ID:'))
            cursor.execute(f'''
                        UPDATE Orders
                        SET Order_Status = {new_ID}
                        WHERE OrderID = {input_order_ID}
                        ''')
            connection.commit()
            cursor.close()
            return print(f'Your itmes order new ID is {new_ID}, Have a Great Day :)')


def update_order_in_DB(fieldnames,Order_Status_feildnames,product_fieldnames):
    refresh_screen()
    # GET all orders from orders table and print
    db_print_all_from(fieldnames)
    # GET user input for order ID
    input_order_ID = int(input('Pick order by ID or press 0 to exit:'))
    while True:
        refresh_screen()
        # display options to edit excluding table name
        print_list(fieldnames[1:])
        # ask for input of the entry type to be updated
        update_choice = int(input('Press the index of the contect you will like to update or 0 to exit:'))
        if update_choice == 0:
            break
        elif update_choice == 1:
            # print existing entry
            db_print_specific(fieldnames, 1 , input_order_ID)
            # GET user input for new ID and update database
            cursor = connection.cursor()
            new_ID = int(input('Pick a new id:'))
            cursor.execute(f'''
                        UPDATE {fieldnames[0]}
                        SET {fieldnames[1]} = {new_ID}
                        WHERE {fieldnames[1]} = {input_order_ID}
                        ''')
            connection.commit()
            cursor.close()
            input_order_ID = new_ID
        elif update_choice == 2:
            # print existing entry
            db_print_specific(fieldnames, 2 , input_order_ID)
            # GET user input for new name and update database
            cursor = connection.cursor()
            new_name = input('What would should the name be?:')
            cursor.execute(f'''
                        UPDATE {fieldnames[0]}
                        SET {fieldnames[2]} = '{new_name}'
                        WHERE {fieldnames[1]} = {input_order_ID}
                        ''')
            connection.commit()
            cursor.close()
        elif update_choice == 3:
            # print existing entry
            db_print_specific(fieldnames, 3 , input_order_ID)
            # GET user input for new address and update database
            cursor = connection.cursor()
            new_address = input('What would should the address be?:')
            cursor.execute(f'''
                        UPDATE {fieldnames[0]}
                        SET {fieldnames[3]} = '{new_address}'
                        WHERE {fieldnames[1]} = {input_order_ID}
                        ''')
            connection.commit()
            cursor.close()
        elif update_choice == 4:
            # print existing entry
            db_print_specific(fieldnames, 4 , input_order_ID)
            cursor = connection.cursor()
            # GET new number to update
            customer_number = int(input(f'What {fieldnames[4]} should it be:'))
            cursor.execute(f'''
                        UPDATE {fieldnames[0]}
                        SET {fieldnames[4]} = {customer_number}
                        WHERE {fieldnames[1]} = {input_order_ID}
                        ''')
            connection.commit()
            cursor.close()
        elif update_choice == 5:
            # print existing entry
            db_print_specific(fieldnames, 5 , input_order_ID)
            cursor = connection.cursor()
            # GET new courier by ID and update
            courier_ID = int(input('Pick courier by ID would you like it to be:'))
            cursor.execute(f'''
                        UPDATE {fieldnames[0]}
                        SET {fieldnames[5]} = {courier_ID}
                        WHERE {fieldnames[1]} = {input_order_ID}
                        ''')
            connection.commit()
            cursor.close()
        elif update_choice == 6:
            # print existing entry
            db_print_specific(fieldnames, 6 , input_order_ID)
            # display order status options with id
            db_print_all_from(Order_Status_feildnames)
            cursor = connection.cursor()
            # GET new status by ID and update
            status_ID = int(input('Pick status by ID would you like it to be:'))
            cursor.execute(f'''
                        UPDATE {fieldnames[0]}
                        SET {fieldnames[6]} = {status_ID}
                        WHERE {fieldnames[1]} = {input_order_ID}
                        ''')
            connection.commit()
            cursor.close()
        elif update_choice == 7:
            # print existing entry
            print('The order is...')
            db_print_specific(fieldnames, 7 , input_order_ID)
            db_print_all_from(product_fieldnames)
            cursor = connection.cursor()
            # GET new orders by ID and update
            items_ID = input('Pick products from the list by ID seperated by a comma')
            cursor.execute(f'''
                        UPDATE {fieldnames[0]}
                        SET {fieldnames[7]} = '{items_ID}'
                        WHERE {fieldnames[1]} = {input_order_ID}
                        ''')
            connection.commit()
            cursor.close()
            
        
def delete_order_in_DB(order_fieldnames):
    db_print_all_from(order_fieldnames)
    order_id = input('Pick oder to be deleted by ID')
    cursor = connection.cursor()
    # takes the table name and deletes at the correspoding id
    cursor.execute(f"DELETE FROM {order_fieldnames[0]} WHERE {order_fieldnames[1]} = {order_id};")
    connection.commit()
    cursor.close()
    print('The order has been successfully deleted')


def save_DB_to_CSV(fieldnames):
    csv_file_path = f'{fieldnames[0]}.csv'
    cursor = connection.cursor()
    # selects everything from table provided
    sql = f"SELECT * FROM {fieldnames[0]}"
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    cursor.close()
    # Continue only if there are rows returned.
    if rows:
        # New empty list called 'result'. This will be written to a file.
        result = list()

        # The row name is the first entry for each entity in the description tuple.
        column_names = list()
        for i in cursor.description:
            column_names.append(i[0])

        result.append(column_names)
        for row in rows:
            result.append(row)

        # Write result to file.
        with open(csv_file_path, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in result:
                csvwriter.writerow(row)
    else:
        print(f"No rows found for query: {sql}")
        
        
        
def db_sort_by(fieldnames):
    cursor = connection.cursor()
    sort_options = ['order status','courier']
    print_list(sort_options)
    column_choice = int(input('Pick option to order by:'))
    # selects everything and sorts (order by) column_choice
    while True:
        if column_choice == 0:
            exit_to_menu()
            break
        elif column_choice == 1:
            # order by order status
            cursor.execute(f"SELECT * FROM {fieldnames[0]} ORDER BY {fieldnames[6]}")
            result = cursor.fetchall()
            for row in result:
                    print(row)
            connection.commit()
            cursor.close()
        elif column_choice == 2:
            # order by courier
            cursor.execute(f"SELECT * FROM {fieldnames[0]} ORDER BY {fieldnames[5]}")
            result = cursor.fetchall()
            for row in result:
                    print(row)
            connection.commit()
            cursor.close()