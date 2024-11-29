import customtkinter as ctk

class Page1(ctk.CTkFrame):
    def __init__(self, master, switch_page_callback):
        super().__init__(master)
        self.switch_page_callback = switch_page_callback
        
        # Add buttons for navigating to Page 2
        self.label = ctk.CTkLabel(self, text="Select an option:")
        self.label.pack(padx=20, pady=20)

        self.option_button1 = ctk.CTkButton(self, text="Go to Page 2", command=self.goto_page2)
        self.option_button1.pack(padx=20, pady=10)

    def goto_page2(self):
        self.switch_page_callback("Page2")  # Call the callback to switch to Page 2

        