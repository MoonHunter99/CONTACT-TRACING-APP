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
        self.hanap.geometry("850x850")
        self.hanap.title("Contact searcher")
    def ui_hanap(self):
        self.frame1= ctk.CTkScrollableFrame(master= self.hanap , height=800, width=805)
        self.frame1.place(x=15, y=10)
        label_Title = ctk.CTkLabel(master= self.frame1, text="Neil's Contact Tracing Application", font=("Times New Roman", 40), text_color="#7DF9FF")
        label_Title.pack(pady=10 ,padx = 10)
    # create a method for starting the mainloop of the window
    def mainloops(self):
        self.hanap.mainloop()
    # create a method of getting the information and searching it in a created excel file