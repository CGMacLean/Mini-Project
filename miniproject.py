import os
import time


PRODUCTS = 'product_list.txt'
COURIERS = 'courier_list.txt'


def print_logo():
    print('''          
          _.._..,_,_
         (          )
          ]~,"-.-~~[
        .=])' (;  ([
        | ]:: '    [
        '=]): .)  ([
          |:: '    |
           ~~----~~
    Callum Maclean Drinks
    ''')


def exit_to_menu():
    print('return to main menu')
    screen_refresh()


def get_item_list(file_location):
    with open(file_location, 'r', newline='') as file:
        lines = [line.rstrip() for line in file.readlines()]
        return lines


def print_list(item_list):
    for i, words in enumerate(item_list):
        print(i, words)


def add_product(file_location, item_name):
    file = open(file_location, 'a+')
    new_item = input(f'What {item_name} do you want to add?:').title()
    file.write(f'{new_item}\n')
    file.close()
    return new_item


def update_item(file_location, item_list, item_name):
    with open(file_location, 'r+', newline='') as file:
        lines = [line.rstrip() for line in file.readlines()]
        for i, words in enumerate(lines):
            print(i, words)
        user_edit_input = int(
            input(f"press the number of the {item_name} you want to edit?"))
        user_replace_input = input(
            'what do you want to replace with?:').title()
        item_list[user_edit_input] = user_replace_input
        screen_refresh()
        return item_list


def save(file_location, lists):
    with open(file_location, "w") as file:
        for i in lists:
            file.write(f"{i}\n")


def delete_item(file_location, item_list, item_name):
    with open(file_location, 'r+', newline='') as file:
        lines = [line.rstrip() for line in file.readlines()]
        for i, words in enumerate(lines):
            print(i, words)
        user_delete_input = (
            int(input(f"press the number of the {item_name} you want to delete?")))
        del item_list[user_delete_input]

    screen_refresh()


def screen_refresh():
    os.system('cls')


print_logo()
product_list = get_item_list(PRODUCTS)
courier_list = get_item_list(COURIERS)
# boot while loop
while True:
    user_input = input(
        "press 0 to save and exit \npress 1 to view products \npress 2 to view couriers:")
    if user_input == '0':
        save(PRODUCTS, product_list)
        save(COURIERS, courier_list)
        break
    elif user_input == '1':
        screen_refresh()
        while True:
            print_logo()
            user_menu_input = input(
                'press 0 to go to main menu \npress 1 to view products \npress 2 add a product \npress 3 to edit product list \npress 4 to delete product:')
            if user_menu_input == '0':
                exit_to_menu()
                break
            elif user_menu_input == '1':
                print_list(product_list)
                time.sleep(3)
                screen_refresh()
            elif user_menu_input == '2':
                new_item = add_product(PRODUCTS, 'products')
                product_list.append(new_item)
                print_list(product_list)
                time.sleep(3)
            elif user_menu_input == '3':
                product_list = update_item(PRODUCTS, product_list, 'products')
                save(PRODUCTS, product_list)
            elif user_menu_input == '4':
                delete_item(PRODUCTS, product_list, 'products')
                save(PRODUCTS, product_list)
    elif user_input == '2':
        screen_refresh()
        while True:
            print_logo()
            user_menu_input = input(
                'press 0 to go to main menu \npress 1 to view couriers \npress 2 add a courier \npress 3 to edit courier list \npress 4 to delete courier:')
            if user_menu_input == '0':
                exit_to_menu()
                break
            elif user_menu_input == '1':
                print_list(courier_list)
                time.sleep(3)
                screen_refresh()
            elif user_menu_input == '2':
                new_item = add_product(COURIERS, 'courier')
                courier_list.append(new_item)
                print_list(courier_list)
                time.sleep(3)
            elif user_menu_input == '3':
                courier_list = update_item(COURIERS, courier_list, 'courier')
                save(COURIERS, courier_list)
            elif user_menu_input == '4':
                delete_item(COURIERS, courier_list, 'courier')
                save(COURIERS, courier_list)
