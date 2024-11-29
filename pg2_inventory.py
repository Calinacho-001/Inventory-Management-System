import customtkinter as ctk

"""PAGE 2 = INVENTORY PAGE"""


class Page2_Inventory(ctk.CTkFrame):
    def __init__(self, master, switch_page_callback):
        super().__init__(master)
        self.switch_page_callback = switch_page_callback
        self.label = ctk.CTkLabel(self, text="Welcome to Page 2. Here are your options:")
        self.label.pack(padx=20, pady=20)
        self.page_buttons()
        
    def page_buttons(self):
        self.inventory_button()
        self.go_back_button()

    def inventory_button(self):
        self.option_button = ctk.CTkButton(self, text="Option 1", command=self.option1_logic)
        self.option_button.pack(padx=20, pady=10)
        
    def go_back_button(self):
        self.option_button = ctk.CTkButton(self, text="Go back to page 1 ", command=self.go_back)
        self.option_button.pack(padx=20, pady=50)

    def option1_logic(self):
        print("Option 1 Logic Executed")

    def go_back(self):
        self.switch_page_callback("Page 1 - Options")  
