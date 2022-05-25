import os
import time
import sys
from Logo import *

def refresh_screen():
    os.system('cls')
    print_logo()
    
    
def display_timer(n):
    for remaining in range(n, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"Displaying for {remaining} seconds.")
        sys.stdout.flush()
        time.sleep(1)



def exit_to_menu():
    print('return to main menu')

