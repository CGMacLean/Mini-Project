import os
import time

from File_functions import *

PRODUCTS = 'product_list.txt'
COURIERS = 'courier_list.txt'
ORDERS = 'order_list.json'


def refresh_screen():
    os.system('cls')
    print_logo()


product_list = get_item_list(PRODUCTS)
courier_list = get_item_list(COURIERS)
# boot while loop
while True:
    refresh_screen()
    user_input = input(
        "press 0 to save and exit: \npress 1 to view products: \npress 2 to view couriers: \npress 3 to view orders:")
    if user_input == '0':
        save(PRODUCTS, product_list)
        save(COURIERS, courier_list)
        break
    elif user_input == '1':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu \npress 1 to view products \npress 2 add a product \npress 3 to edit product list \npress 4 to delete product:')
            if user_menu_input == '0':
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                print_list(product_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '2':
                print_list(product_list)
                new_item = add_item(PRODUCTS, 'products')
                product_list.append(new_item)
                print_list(product_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '3':
                product_list = update_item(PRODUCTS, product_list, 'products')
                save(PRODUCTS, product_list)
                refresh_screen()
            elif user_menu_input == '4':
                delete_item(PRODUCTS, product_list, 'products')
                save(PRODUCTS, product_list)
                refresh_screen()
    elif user_input == '2':
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu \npress 1 to view couriers \npress 2 add a courier \npress 3 to edit courier list \npress 4 to delete courier:')
            if user_menu_input == '0':
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                print_list(courier_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '2':
                print_list(courier_list)
                new_item = add_item(COURIERS, 'courier')
                courier_list.append(new_item)
                print_list(courier_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '3':
                courier_list = update_item(COURIERS, courier_list, 'courier')
                save(COURIERS, courier_list)
                refresh_screen()
            elif user_menu_input == '4':
                delete_item(COURIERS, courier_list, 'courier')
                save(COURIERS, courier_list)
                refresh_screen()
    elif user_input == '3':
        refresh_screen
        while True:
            user_menu_input = input(
                'press 0 to go to main menu \npress 1 to view orders \npress 2 add a order \npress 3 to edit order status \npress 4 to update order: \npress 5 to delete order:')
            if user_menu_input == '0':
                exit_to_menu()
                refresh_screen()
                break
            if user_menu_input == '1':
                print_order_list(ORDERS)
