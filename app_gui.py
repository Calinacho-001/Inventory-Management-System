import customtkinter as ctk
from config import APP_TITLE, APP_VERSION
from pg1_options import Page1_Options
from pg2_inventory import Page2_Inventory


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resizable(False, False)
        self.geometry("450x350")
        self.title(f"{APP_TITLE} {APP_VERSION}")
        ctk.set_appearance_mode("dark")
        self.get_mouse_coordinates()
        
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


    def get_mouse_coordinates(self):
        """
        Binds a left mouse button click to get the coordinates of the click
        and prints the coordinates in the terminal.
        """
        def on_click(event):
            x, y = event.x, event.y
            print(f"Clicked at x: {x}, y: {y}")

        self.bind("<Button-1>", on_click)


    def run(self):
        self.mainloop()
