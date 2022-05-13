import json
import os
import time
# import yaml


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


def refresh_screen():
    os.system('cls')
    print_logo()


def exit_to_menu():
    print('return to main menu')


def get_item_list(file_location):
    with open(file_location, 'r', newline='') as file:
        lines = [line.rstrip() for line in file.readlines()]
        return lines


def print_list(item_list):
    for i, words in enumerate(item_list):
        print(i, words)


def add_item(file_location, item_name):
    with open(file_location, 'a+') as file:
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


def load_json(item_list):
    with open(item_list, 'r') as file:
        contents = json.loads(file.read())

    return contents


def add_order_list(item_list, order_list, item_name):
    with open(item_list, 'a+') as file:
        new_item = input(f'What {item_name} do you want to add?:').title()
        order_list.append(new_item)
        file.write(f'{new_item}\n')
        file.close()
        return new_item


# contents = load_json('order_list.json')


def print_order_list(contents):
    print(contents)


def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data


def input_new_order(order_list, courier_list):
    new_orders = {}
    new_orders['customer_name'] = input('type the customer name:')
    new_orders['customer_address'] = input('type customer address:')
    new_orders['customer_phone'] = input('type customer number:')
    print_list(courier_list)
    courier_index = int(input('pick the number of the courier:'))
    new_orders['courier'] = int(courier_index)
    new_orders['status'] = 'preparing'
    return order_list.append(new_orders)


def update_json(data, entry):
    data.append(entry)


def save_orders(lists, filename):
    with open(filename,  "w") as file:
        file.write(json.dumps(lists, indent=4))


# edit value of key in dict
def pick_order(order_list):
    print_list(order_list)
    order_index = int(input('pick the number of the order:'))
    picked_order = order_list[order_index]
    return picked_order


def edit_order_status(picked_order):
    refresh_screen()
    print(f'"status":{picked_order["status"]}')
    status_options = ['preparing', 'out for delivery', 'complete']
    print_list(status_options)
    picked_status = int(
        input('press the number of the update you want to apply:'))
    status_value = status_options[picked_status]
    picked_order["status"] = status_value
    print(f'Status has now changed to \n"status":{status_value}')
    time.sleep(3)
    refresh_screen()
    return picked_order


def edit_dict(picked_order, courier_list):
    refresh_screen()
    while True:
        key_list = ['customer_name', 'customer_address',
                    'customer_phone', 'courier', 'status']
        print_list(key_list)

        order_key_index = int(
            input('pick the number of the option you want to edit:'))
        key_choice = key_list[order_key_index]
        key_value = picked_order[key_choice]
        if order_key_index == 3:
            print(f'{key_choice}:{key_value}')
            print_list(courier_list)
            courier_index = int(
                input('pick the number of the courier you would like to replace with?:'))
            picked_order['courier'] = courier_index
            print(f'{key_choice}:{key_value}')
            return picked_order
        elif order_key_index == 4:
            edit_order_status(picked_order)
            return picked_order
        elif order_key_index == 0 or 1 or 2:
            refresh_screen()
            print(f'{key_choice}:{key_value}')
            picked_order[key_choice] = input(
                'what would you like to replace with?:')
            return picked_order
        return picked_order


def delete_order(order_list):
    print_list(order_list)
    order_index = int(input('pick the number of the order:'))
    del order_list[order_index]
    # list.pop(order_index)
    return
    # return order_list.remove(order_index)

    # order_index = int(input('pick the number of the option you want to edit:'))
    # # new_edit = picked_order[order_index]
    # picked_order.append()
    # print(new_edit)

    # return new_edit


# courier_index = int(input('pick the number of the courier:'))
# new_orders['courier'] = courier_list[courier_index]
