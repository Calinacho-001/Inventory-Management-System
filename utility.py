import os
import sys
import pandas as pd
import random


def generate_unique_random_number(used_numbers):
    """Generates a unique 4 digit random number."""
    while True:
        random_number = random.randint(1000, 9999)
        if random_number not in used_numbers:
            return random_number


def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        os.system('clear')