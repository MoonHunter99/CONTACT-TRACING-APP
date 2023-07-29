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
        label_title = ctk.CTkLabel(master= self.frame1, text="Neil's Contact Tracing Application", font=("Times New Roman", 40), text_color="#7DF9FF")
        label_title.pack(padx=10 , pady=12)
        label_title_name = ctk.CTkLabel(master= self.frame1, text="Search information", font=("Times New Roman", 30), text_color="#7DF9FF")
        label_title_name.pack(padx=10 , pady=12)
        label_name = ctk.CTkLabel(master= self.frame1, text="Full Name", font=("Times New Roman", 20), text_color="orange")
        label_name.pack(padx=10 , pady=10)
        self.name = ctk.CTkEntry(master=self.frame1, placeholder_text="Full Name")
        self.name.pack(pady=10, padx=10, )
        # create a method of getting the information and searching it in a created excel file
        def hanap_info():
            name = self.name.get()
            information = []
            with open("respondent_information.csv","r") as readings:
                read = csv.reader(readings)
                heading = next(read)
                for row in read:
                    if name in row:
                        information.append(row)
                        break
            if information:
                pangalan = ctk.CTkLabel(master=self.frame1, text=f"Name: {row[0]}", font=("Arial", 20), text_color="orange")
                pangalan.pack(padx=10 , pady=12)
                phone_number = ctk.CTkLabel(master=self.frame1, text=f"Phone: 0{row[1]}", font=("Arial", 20), text_color="orange")
                phone_number.pack(padx=10 , pady=12)
                email = ctk.CTkLabel(master=self.frame1, text=f"Email: {row[2]}", font=("Arial", 20), text_color="orange")
                email.pack(padx=10 , pady=12)
                address = ctk.CTkLabel(master=self.frame1, text=f"Address: {row[3]}", font=("Arial", 20), text_color="orange")
                address.pack(padx=10 , pady=12)
                vaccine = ctk.CTkLabel(master=self.frame1, text=f"Vaccine: {row[4]}", font=("Arial", 20), text_color="orange")
                vaccine.pack(padx=10 , pady=12)
                symptoms = ctk.CTkLabel(master=self.frame1, text=f"Symptoms: {row[5]}", font=("Arial", 20), text_color="orange")
                symptoms.pack(padx=10 , pady=12)
                contact_covid = ctk.CTkLabel(master=self.frame1, text=f"Contact with Covid: {row[6]}", font=("Arial", 20), text_color="orange")
                contact_covid.pack(padx=10 , pady=12)
                covid_tested = ctk.CTkLabel(master=self.frame1, text=f"Covid Tested?: {row[7]}", font=("Arial", 20), text_color="orange")
                covid_tested.pack(padx=10 , pady=12)
            else:
                msgb.showerror("Wrong Name","The name you inputed is not on the data base")
        def exit():
            self.hanap.destroy()
        srch_btn = ctk.CTkButton(master=self.frame1, text="Search", font=("Times New Roman",12), command=hanap_info).pack(pady=10,padx=12)
        ext_btn = ctk.CTkButton(master=self.frame1, text="EXIT", font=("Times New Roman",12), command=exit).pack(padx=10 , pady=12)
    # create a method for starting the mainloop of the window
    def mainloops(self):
        self.hanap.mainloop()
    