import json
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


def load_order_list(item_list):
    with open(item_list, 'r') as file:
        contents = json.loads(file.read())

        return contents


contents = load_order_list('order_list.json')


def print_order_list(contents):
    print(contents)


print_order_list(contents)
