# import customtkinter
import customtkinter as ctk
from tkinter import messagebox as msgb
# import csv
import csv
# create a class for the searching segment
class SearcherGUI:
    # create a constructor of a gui to use for getting the information of registration
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.hanap = ctk.CTk()
        self.hanap.geometry("850x400")
        self.hanap.resizable(width=False, height=False)
        self.hanap.title("Contact searcher")
    def ui_hanap(self):
        self.frame1= ctk.CTkScrollableFrame(master= self.hanap)
        self.frame1.pack(fill=ctk.BOTH,expand="yes",padx= 60 , pady=20)
        label_Title = ctk.CTkLabel(master= self.frame1, text="Neil's Contact Tracing Application", font=("Times New Roman", 40), text_color="#7DF9FF")
        label_Title.pack(padx=10 , pady=12)
        label_Title_name = ctk.CTkLabel(master= self.frame1, text="Search information", font=("Times New Roman", 30), text_color="#7DF9FF")
        label_Title_name.pack(padx=10 , pady=12)
        label_name = ctk.CTkLabel(master= self.frame1, text="Full Name", font=("Times New Roman", 20), text_color="orange")
        label_name.pack(padx=10 , pady=10)
        self.name = ctk.CTkEntry(master=self.frame1, placeholder_text="Full Name")
        self.name.pack(pady=10, padx=10, )
        srch_btn = ctk.CTkButton(master=self.frame1, text="Search", font=("Times New Roman",12)).pack(pady=10,padx=12)
    # create a method for starting the mainloop of the window
    def mainloops(self):
        self.hanap.mainloop()
    # create a method of getting the information and searching it in a created excel file