import customtkinter as ctk


"""PAGE 1 = OPTIONS PAGE"""

class Page1_Options(ctk.CTkFrame):
    def __init__(self, master, switch_page_callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.switch_page_callback = switch_page_callback
        # self.label = ctk.CTkLabel(self, text="Select an option:")
        # self.label.pack(anchor="w" ,padx=40, pady=35)
        self.pg1_tabs()
        self.page_buttons()


    def pg1_tabs(self):
        tabs = ctk.CTkTabview(self)
        tabs.pack(pady=10, padx=10)

        tabs.add("Tab 1")  # First tab
        tabs.add("Tab 2")  # Second tab

    def page_buttons(self):
        self.options_button()

    def options_button(self):
        self.option_button = ctk.CTkButton(self, text="Go to Page 2", command=self.goto_page2)
        self.option_button.pack(padx=20, pady=10)

    def goto_page2(self):
        self.switch_page_callback("Page 2 - Inventory")  # Call the callback to switch to Page 2

        