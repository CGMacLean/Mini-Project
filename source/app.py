import os
import time
from File_functions import *

PRODUCTS = 'product_list.csv'
COURIERS = 'courier_list.csv'
ORDERS = 'order_list.csv'
ORDER_STATUS = 'order_status.csv'


product_list = open_csv(PRODUCTS)
print(product_list)
courier_list = open_csv(COURIERS)
order_list = open_csv(ORDERS)

print_logo()


# boot while loop
while True:
    # refresh_screen()
    user_input = input(
        "press 0 to save and exit: \npress 1 to view products: \npress 2 to view couriers: \npress 3 to view orders:")
    if user_input == '0':
        # save_csv(PRODUCTS)
        # save_csv(COURIERS)
        # save_csv(ORDERS)
        break
    # product menu
    elif user_input == '1':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu: \npress 1 to view products: \npress 2 add a product: \npress 3 to edit product list: \npress 4 to delete product:')
            if user_menu_input == '0':
                # RETURN to main menu
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                # PRINT products list
                print_list_dict(product_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '2':
                # CREATE new product
                print_list_dict(product_list)
                new_item = add_item(PRODUCTS, 'product')
                product_list.append(new_item)
                print_list_dict(product_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '3':
                # UPDATE existing product
                product_list = update_item(PRODUCTS, product_list, 'products')
                save(PRODUCTS, product_list)
                refresh_screen()
    # courier menu
    elif user_input == '2':
        print(courier_list)
    # order menu
    elif user_input == '3':
        print(order_list)
