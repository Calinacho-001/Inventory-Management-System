from pyfiglet import Figlet
import os
import sys
import json
from tabulate import tabulate
from simple_colors import *  # type: ignore
from simple_colors import red, cyan, yellow, green, blue  # type: ignore
import random


ff = Figlet(font='doom')
ff2 = Figlet(font='slant')
ff3 = Figlet(font='big')


def main():

    json_file = "products_data.json"

    product_data = load_json_data(json_file)
    checks(json_file, product_data)
    main_menu_screen()
    clear_screen()
    app_options(json_file, product_data)


def app_options(json_file, product_data):
    while True:
        options = input(yellow("Please choose an option from below:\n"
                               "[1] Add Product;\n"
                               "[2] Display Table;\n"
                               "[3] Delete Product From inventory;\n"
                               "[4] Delete all Products | Items From Inventory;\n"
                               "[5] Exit IMS;\n >>> ", ['underlined']))
        clear_screen()
        if options == "1":
            add_item(json_file, product_data)
            product_data = load_json_data(json_file)
            display_table(product_data, json_file)
        elif options == "2":
            display_table(product_data, json_file)
        elif options == "3":
            display_table(product_data, json_file)
            delete_item(json_file, product_data)
            product_data = load_json_data(json_file)
            display_table(product_data, json_file)
        elif options == "4":
            delete_all_items(json_file, product_data)
            product_data = []
        elif options == "5":
            custom_text = ff.renderText("Goodbye!")
            custom_colored_text = cyan(custom_text)
            print(custom_colored_text)
            break
        else:
            print(red("Invalid Option", ['bold']))


def main_menu_screen():
    # custom_main_menu = ff2.renderText("Welcome to!")
    custom_main_menu_version = ff2.renderText("IMS v1.0")
    # custom_colored_text_menu = blue(custom_main_menu)
    custom_colored_text_version = yellow(custom_main_menu_version)
    clear_screen()
    # print(custom_colored_text_menu)
    print(custom_colored_text_version)
    custom_main_menu_key = ff3.renderText("Press any key \nto continue.")
    custom_main_menu_key = green(custom_main_menu_key)
    print(custom_main_menu_key)
    input()


def display_table(product_data, json_file):
    header = [yellow("ID", ['bold']), yellow("Product Name", ['bold']), yellow("Price", ['bold'])]
    table_data = []

    for product in product_data:
        unique_number = product.get("UniqueNumber")
        table_data.append([cyan(unique_number), product.get("Name", ""), product.get("Price", "")])

    checks(json_file, product_data)

    if product_data:
        try:
            colalign = ["center"] * len(table_data[0])
            data_table = tabulate(table_data, headers=header,
                                  colalign=colalign, tablefmt="fancy_outline")
            print(data_table)
        except Exception:
            print(green("Item added successfully! Press [2] to view the table.", ['bold']))
    else:
        print(red("No products to display.", ['bold']))


def add_item(json_file, product_data):
    new_product = {}
    new_product["Name"] = input("Enter product name: ")

    while True:
        price_input = input("Enter product price: ")
        try:
            new_product["Price"] = int(price_input)
            break
        except ValueError:
            print(red("Price needs to be a valid number. Please try again."))

    used_numbers = [product.get("UniqueNumber", None) for product in product_data]
    new_product["UniqueNumber"] = generate_unique_random_number(used_numbers)

    product_data.append(new_product)
    save_json_data(json_file, product_data)
    print(green("Product added successfully!"))


def jsonfile_empty(product_data):
    return len(product_data) == 0


def checks(json_file, product_data):
    if jsonfile_empty(product_data):
        print(red("Inventory is empty! Add product / item:"))
        add_item(json_file, product_data)


def delete_all_items(json_file, product_data):
    custom_warning = ff.renderText("WARNING!")
    custom_colored_text = red(custom_warning)
    print(custom_colored_text)
    print(red("\nThis will delete all the items in the list. Are you sure you want to proceed? "))

    delete_all_items_from_list = input("y/n: ")

    if delete_all_items_from_list.lower() == "y":
        product_data.clear()

        with open(json_file, 'w') as file:
            json.dump(product_data, file)

        clear_screen()
        print(green("All items deleted successfully."))

    elif delete_all_items_from_list.lower() == "n":
        clear_screen()
        print(green("Returned to the main menu."))
        display_table(product_data, json_file)

    else:
        clear_screen()
        print(red("Not a valid choice. Returned to the main menu."))
        display_table(product_data, json_file)


def delete_item(json_file, product_data):
    try:
        item_id_del = input("Enter the ID of the product/item you want to delete: ")
        filtered_data = [items for items in product_data if items.get(
            "UniqueNumber") == int(item_id_del)]
        if filtered_data:
            product_data = [items for items in product_data if items.get(
                "UniqueNumber") != int(item_id_del)]
            save_json_data(json_file, product_data)
            clear_screen()
            print(green(f"Product with ID {item_id_del} deleted successfully."))
        else:
            print(red("Product not found with the specified ID."))

    except ValueError:
        print(red("Choice was not a number, please choose an ID from the List."))


def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        os.system('clear')


def generate_unique_random_number(used_numbers):
    while True:
        random_number = random.randint(1000, 9999)  # Generating a random four-digit number
        if random_number not in used_numbers:
            return random_number


def load_json_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def save_json_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
