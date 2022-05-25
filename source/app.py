from Data_base_manager import *
from menu_functions import refresh_screen,display_timer,exit_to_menu
from Logo import print_logo



product_fieldnames = ['Product','ProductID', 'Product_Name', 'Price']
courier_fieldnames = ['Courier','Courier_ID','Courier_name','Tel_No']
order_fieldnames =['Orders','OrderID', 'Customer_name','Customer_Address','Customer_Phone','Couriers','Order_Status','Items']
Order_Status_feildnames = ['Order_Status','Order_Status_id','Order_Status']

print_logo()


# boot while loop
while True:
    # refresh_screen()
    user_input = input(
     "press 0 to save and exit: \npress 1 to view products menu: \npress 2 to view couriers menu: \npress 3 to view orders menu:")
    if user_input == '0':
        save_DB_to_CSV(product_fieldnames)
        save_DB_to_CSV(courier_fieldnames)
        save_DB_to_CSV(order_fieldnames)
        print('Backup saved to csv. Thank you for shopping')
        connection.close()
        break
    # product menu
    elif user_input == '1':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu: \npress 1 to view products: \npress 2 add a product: \npress 3 to update product infomation: \npress 4 to delete product:')
            if user_menu_input == '0':
                # RETURN to main menu
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                # PRINT products list
                refresh_screen()
                db_print_all_from(product_fieldnames)
                display_timer(3)
                refresh_screen()
            elif user_menu_input == '2':
                # CREATE new product
                db_print_all_from(product_fieldnames)
                add_to_DB(product_fieldnames)
                db_print_all_from(product_fieldnames)
                display_timer(3)
                refresh_screen()
            elif user_menu_input == '3':
                # UPDATE existing product
                refresh_screen()
                db_print_all_from(product_fieldnames)
                update_item_in_DB(product_fieldnames)
                db_print_all_from(product_fieldnames)
                refresh_screen()
            elif user_menu_input == '4':
                # DELETE product
                refresh_screen()
                db_print_all_from(product_fieldnames)
                delete_item_in_DB(product_fieldnames)
                refresh_screen()
    # courier menu
    elif user_input == '2':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu: \npress 1 to view Couriers: \npress 2 add a Courier: \npress 3 to update Courier infomation: \npress 4 to delete Courier:')
            if user_menu_input == '0':
                # RETURN to main menu
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                # PRINT products list
                refresh_screen()
                db_print_all_from(courier_fieldnames)
                display_timer(3)
                refresh_screen()
            elif user_menu_input == '2':
                # CREATE new product
                db_print_all_from(courier_fieldnames)
                add_to_DB(courier_fieldnames)
                db_print_all_from(courier_fieldnames)
                display_timer(3)
                refresh_screen()
            elif user_menu_input == '3':
                # UPDATE existing product
                refresh_screen()
                db_print_all_from(courier_fieldnames)
                update_item_in_DB(courier_fieldnames)
                db_print_all_from(courier_fieldnames)
                refresh_screen()
            elif user_menu_input == '4':
                # DELETE product
                refresh_screen()
                db_print_all_from(courier_fieldnames)
                delete_item_in_DB(courier_fieldnames)
                refresh_screen()
    # order menu
    elif user_input == '3':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu: \npress 1 to view Orders: \npress 2 add a Order: \npress 3 to update Order status infomation: \npress 4 to update an Orders details: \npress 5 to delete an Orders')
            if user_menu_input == '0':
                # RETURN to main menu
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                # print all orders
                refresh_screen()
                db_print_all_from(order_fieldnames)
                display_timer(3)
                refresh_screen()
            elif user_menu_input == '2':
                # add an order to the order list
                refresh_screen()
                add_order_to_database(order_fieldnames,product_fieldnames,courier_fieldnames)
            elif user_menu_input == '3':
                refresh_screen()
                # update an existing orders status
                update_order_status_in_DB(order_fieldnames,Order_Status_feildnames)
                refresh_screen()
            elif user_menu_input == '4':
                refresh_screen()
                # update an existing order
                update_order_in_DB(order_fieldnames,Order_Status_feildnames,product_fieldnames)
                refresh_screen()
            elif user_menu_input == '5':
                refresh_screen()
                # delete an existing order 
                delete_order_in_DB(order_fieldnames)
                refresh_screen()
            elif user_menu_input == '6':
                refresh_screen()
                db_sort_by(order_fieldnames)
                
                