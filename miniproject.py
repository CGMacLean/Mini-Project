import os
import time
from Main_function import *

PRODUCTS = 'product_list.csv'
COURIERS = 'courier_list.csv'
ORDERS = 'order_list.json'
ORDER_STATUS = 'order_status.json'


product_list = open_csv(PRODUCTS)
print(product_list)
# print(print_list(product_list))
courier_list = open_csv(COURIERS)
order_list = load_json(ORDERS)
# order_status = load_json(ORDER_STATUS)

# courier_by_index = {print_list(courier_list)}

print_logo()


# boot while loop
while True:
    # refresh_screen()
    user_input = input(
        "press 0 to save and exit: \npress 1 to view products: \npress 2 to view couriers: \npress 3 to view orders:")
    if user_input == '0':
        save(PRODUCTS, product_list)
        save(COURIERS, courier_list)
        save_orders(order_list, ORDERS)
        break
    elif user_input == '1':
        # product menu
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
                print(print_list(product_list))
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '2':
                # CREATE new product
                print_list(product_list)
                new_item = add_item(PRODUCTS, 'products')
                product_list.append(new_item)
                print_list(product_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '3':
                # UPDATE existing product
                product_list = update_item(PRODUCTS, product_list, 'products')
                save(PRODUCTS, product_list)
                refresh_screen()
            elif user_menu_input == '4':
                # DELETE product
                delete_item(PRODUCTS, product_list, 'products')
                save(PRODUCTS, product_list)
                refresh_screen()
    elif user_input == '2':
        # courier menu
        refresh_screen()
        while True:
            user_menu_input = input(
                'press 0 to go to main menu: \npress 1 to view couriers: \npress 2 add a courier: \npress 3 to edit courier list: \npress 4 to delete courier:')
            if user_menu_input == '0':
                # RETURN to main menu
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                # PRINT couriers list
                print_list(courier_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '2':
                # CREATE new courier
                print_list(courier_list)
                new_item = add_item(COURIERS, 'courier')
                courier_list.append(new_item)
                print_list(courier_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '3':
                # UPDATE existing courier
                courier_list = update_item(COURIERS, courier_list, 'courier')
                save(COURIERS, courier_list)
                refresh_screen()
            elif user_menu_input == '4':
                # delete courier
                delete_item(COURIERS, courier_list, 'courier')
                save(COURIERS, courier_list)
                refresh_screen()
    elif user_input == '3':
        # order menu
        refresh_screen()
        while True:
            refresh_screen()
            user_menu_input = input(
                'press 0 to go to main menu \npress 1 to view orders \npress 2 add a order \npress 3 to edit order status \npress 4 to update order: \npress 5 to delete order:')
            if user_menu_input == '0':
                # exit to menu
                exit_to_menu()
                refresh_screen()
                break
            elif user_menu_input == '1':
                # print orders
                print_order_list(order_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '2':
                # add new order
                input_new_order(order_list, courier_list)
                save_orders(order_list, ORDERS)
                print_order_list(order_list)
                time.sleep(3)
                refresh_screen()
            elif user_menu_input == '3':
                picked_order = pick_order(order_list)
                edit_order_status(picked_order)
                save_orders(order_list, ORDERS)
                refresh_screen()
            elif user_menu_input == '4':
                refresh_screen()
                picked_order = pick_order(order_list)
                # print_list(picked_order)
                edit_dict(picked_order, courier_list)
                # new_edit = edit_dict(picked_order)
                save_orders(order_list, ORDERS)
                refresh_screen()
            elif user_menu_input == '5':
                delete_order(order_list)
                save_orders(order_list, ORDERS)
                refresh_screen()
