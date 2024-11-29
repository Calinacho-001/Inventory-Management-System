import customtkinter as ctk
from page_1 import Page1
from page_2 import Page2

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Inventory Management System")
        # Create a dictionary to hold pages
        self.pages = {}
        
        # Add pages to dictionary
        self.pages["Page1"] = Page1(self, self.switch_page)
        self.pages["Page2"] = Page2(self)

        # Show the first page
        self.pages["Page1"].pack(fill="both", expand=True)
         
    def switch_page(self, page_name):
        """Switch between pages by packing the new page and hiding the current one."""
        for page in self.pages.values():
            page.pack_forget()  # Hide all pages

        self.pages[page_name].pack(fill="both", expand=True)  # Show the selected page

