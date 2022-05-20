import os
import time
from File_functions import *
from file_manager2 import *
from menu_functions import *
from Logo import *

# PRODUCTS = 'product_list.csv'
# COURIERS = 'courier_list.csv'
# ORDERS = 'order_list.csv'
# ORDER_STATUS = ['Prepareing', 'Out for delivery','Complete']


# product_list = open_csv(PRODUCTS)
# courier_list = open_csv(COURIERS)
# order_list = open_csv(ORDERS)

product_fieldnames = ['Product','ProductID', 'Product_Name', 'Price']
courier_fieldnames = ['Courier','Courier_ID','Courier_name','Tel_No']
order_fieldnames =['PersonID', 'Customer_name','Customer _Address','Customer_Phone','couriers','order_status','Items']

print_logo()


# boot while loop
while True:
    # refresh_screen()
    user_input = input(
     "press 0 to save and exit: \npress 1 to view products menu: \npress 2 to view couriers menu: \npress 3 to view orders menu:")
    if user_input == '0':
        # save_csv(PRODUCTS)
        # save_csv(COURIERS)
        # save_csv(ORDERS)
        print('Thank you for shopping')
        connection.close()
        break
    # product menu
    elif user_input == '1':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu: \npress 1 to view products: \npress 2 add a product: \npress 3 to edit product infomation: \npress 4 to delete product:')
            if user_menu_input == '0':
                # RETURN to main menu
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                # PRINT products list
                refresh_screen()
                DB_print(product_fieldnames)
                display_timer(3)
                refresh_screen()
            elif user_menu_input == '2':
                # CREATE new product
                DB_print(product_fieldnames)
                add_to_DB(product_fieldnames)
                DB_print(product_fieldnames)
                display_timer(3)
                refresh_screen()
            elif user_menu_input == '3':
                # UPDATE existing product
                refresh_screen()
                DB_print(product_fieldnames)
                update_item_in_DB(product_fieldnames)
                DB_print(product_fieldnames)
                refresh_screen()
            elif user_menu_input == '4':
                # DELETE product
                refresh_screen()
                DB_print(product_fieldnames)
                delete_item_in_DB(product_fieldnames)
                refresh_screen()
    # courier menu
    elif user_input == '2':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu: \npress 1 to view Couriers: \npress 2 add a Courier: \npress 3 to edit Courier infomation: \npress 4 to delete Courier:')
            if user_menu_input == '0':
                # RETURN to main menu
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                # PRINT products list
                refresh_screen()
                DB_print(courier_fieldnames)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '2':
                # CREATE new product
                DB_print(courier_fieldnames)
                add_to_DB(courier_fieldnames)
                DB_print(courier_fieldnames)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '3':
                # UPDATE existing product
                refresh_screen()
                DB_print(courier_fieldnames)
                update_item_in_DB(courier_fieldnames)
                DB_print(courier_fieldnames)
                refresh_screen()
            elif user_menu_input == '4':
                # DELETE product
                refresh_screen()
                DB_print(courier_fieldnames)
                delete_item_in_DB(courier_fieldnames)
                refresh_screen()
    # order menu
    elif user_input == '3':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu: \npress 1 to view Orders: \npress 2 add a Order: \npress 3 to edit Order infomation: \npress 4 to delete an Order:')
            if user_menu_input == '0':
                # RETURN to main menu
                exit_to_menu()
                refresh_screen()
                break
            
            
