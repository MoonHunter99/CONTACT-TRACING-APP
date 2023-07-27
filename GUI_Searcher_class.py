# import customtkinter
import customtkinter as ctk
# import csv
import csv
# create a class for the searching segment
class SearcherGUI:
    # create a constructor of a gui to use for getting the information of registration
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
    # create a method for starting the mainloop of the window
    # create a method of getting the information and searching it in a created excel file