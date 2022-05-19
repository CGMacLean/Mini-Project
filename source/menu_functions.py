import os
import time
from Logo import *

def refresh_screen():
    os.system('cls')
    print_logo()


def exit_to_menu():
    print('return to main menu')


def print_list_dict(item_list):
    for i, dict in enumerate(item_list):
        print(i, dict)
