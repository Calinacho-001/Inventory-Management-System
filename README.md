# Inventory Management System (IMS)

## Overview

Welcome to the Inventory Management System (IMS), a robust and user-friendly application designed to help you manage your inventory effectively. This system is entirely command-line interface (CLI) based, making it lightweight and easily accessible without the need for a graphical user interface (GUI). The IMS is perfect for small businesses, hobbyists, or anyone needing a straightforward way to keep track of their products.

## Key Features

### Unique Product ID
One of the standout features of the IMS is the assignment of a unique Product ID to each item added to the inventory. This functionality ensures that products with the same name do not overwrite each other, providing a reliable way to manage similar items.

### Real-Time Updates
With the IMS, any changes made to your inventory are reflected instantly. Whether you are adding new products or removing existing ones, the inventory table updates in real time. This feature ensures that you always have the most accurate information at your fingertips.

### Bulk Deletion
Managing large inventories can often lead to the need for bulk deletions. The IMS allows you to delete all items in your inventory quickly and easily. This feature is particularly useful in scenarios where a significant number of products have been sold or disposed of, enabling users to clear their inventory with a single command.

### Customizability
The IMS is designed to be highly customizable. Users can modify or extend its functionality to suit their specific needs. By default, the application creates a single inventory file, but this can be adjusted according to user preferences, making it adaptable to various inventory management scenarios.

## Getting Started

To start using the Inventory Management System, simply clone the repository and run the main script. The system initializes by loading any existing product data from a JSON file named `products_data.json`. If this file does not exist, the application will create it automatically.

### Installation Requirements
Make sure you have Python installed on your machine, as well as the following libraries:
- `tabulate`
- `simple_colors`

### Functionality Breakdown
## Main Menu
Upon starting the application, you'll see a main menu with options to add products, display the inventory table, delete individual products, or clear all items. The application employs simple text prompts, making it easy to navigate.

## Adding Products
When you choose to add a product, you will be prompted to enter the product name and price. The application checks that the price is a valid number and assigns a unique ID before saving the new product to your inventory.

## Displaying Inventory
Selecting the option to display the inventory presents you with a neatly formatted table showing all products, their unique IDs, names, and prices. This visual representation makes it easy to track and manage your inventory at a glance.

## Deleting Products
If you need to remove a product from your inventory, simply input its unique ID, and the IMS will handle the deletion for you. Additionally, you can opt to delete all products at once if necessary.

## Error Handling
The IMS is designed to handle errors gracefully. If a user inputs an invalid option or provides incorrect data, the application will alert the user and prompt them to try again, ensuring a smooth user experience.

## Conclusion
The Inventory Management System is a powerful tool for anyone needing to keep track of products efficiently. With its command-line interface, real-time updates, and customizable features, it provides an effective solution to inventory management without unnecessary complexity. 

