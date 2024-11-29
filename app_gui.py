import customtkinter as ctk
from config import APP_TITLE, APP_VERSION
from pg1_options import Page1_Options
from pg2_inventory import Page2_Inventory


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title(f"{APP_TITLE} {APP_VERSION}")
        # Create a dictionary to hold pages
        self.pages = {}
        
        # Add pages to dictionary
        self.pages["Page 1 - Options"] = Page1_Options(self, self.switch_page)
        self.pages["Page 2 - Inventory"] = Page2_Inventory(self, self.switch_page)

        # Show the first page
        self.pages["Page 1 - Options"].pack(fill="both", expand=True)
         
    def switch_page(self, page_name):
        """Switch between pages by packing the new page and hiding the current one."""
        for page in self.pages.values():
            page.pack_forget()  # Hide all pages

        self.pages[page_name].pack(fill="both", expand=True)  # Show the selected page

