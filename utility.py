import os
import sys
import pandas as pd





def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        os.system('clear')