import customtkinter as ctk

class Page2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Page 2 content
        self.label = ctk.CTkLabel(self, text="Welcome to Page 2. Here are your options:")
        self.label.pack(padx=20, pady=20)

        self.option_button2 = ctk.CTkButton(self, text="Option 1", command=self.option1_logic)
        self.option_button2.pack(padx=20, pady=10)

    def option1_logic(self):
        print("Option 1 Logic Executed")
