# import customtkinter
import customtkinter as ctk
from tkinter import messagebox
# import csv
import csv
# create a class for the registration segment
class RegistrationGUI:
    # create a constructor of a gui to use for getting the information of registration
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.app = ctk.CTk()
        self.app.geometry("850x1000")
        self.app.resizable(width=False, height=False)
        self.app.title("Neil's Personal Contact Tracing Application")
    def registration(self):
        self.frame1= ctk.CTkScrollableFrame(master= self.app)
        self.frame1.pack(fill=ctk.BOTH,expand="yes",padx= 60 , pady=20)
        label_title = ctk.CTkLabel(master= self.frame1, text="Neil's Contact Tracing Application", font=("Times New Roman", 40), text_color="#7DF9FF")
        label_title.pack(padx=10 , pady=12)
        label_title_name = ctk.CTkLabel(master= self.frame1, text="Register Infromation", font=("Times New Roman", 30), text_color="#7DF9FF")
        label_title_name.pack(padx=10 , pady=12)
        label_first_name = ctk.CTkLabel(master= self.frame1, text="First Name", font=("Times New Roman", 20), text_color="orange")
        label_first_name.pack(padx=10 , pady=10)
        self.first_name = ctk.CTkEntry(master=self.frame1, placeholder_text="First Name")
        self.first_name.pack(pady=10, padx=10, )
        label_last_name = ctk.CTkLabel(master= self.frame1, text="Last Name", font=("Times New Roman", 20), text_color="orange")
        label_last_name.pack(padx=10 , pady=10)
        self.last_name = ctk.CTkEntry(master=self.frame1, placeholder_text="Last Name")
        self.last_name.pack(pady=10, padx=10,)
        phone_number_label = ctk.CTkLabel(master= self.frame1, text="Phone Number", font=("Times New Roman", 20), text_color="orange")
        phone_number_label.pack(padx=10 , pady=10)
        self.phone_number = ctk.CTkEntry(master=self.frame1, placeholder_text="09XXXXXXXXX")
        self.phone_number.pack(pady=10, padx=10, )
        label_email = ctk.CTkLabel(master= self.frame1, text="E-mail", font=("Times New Roman", 20), text_color="orange")
        label_email.pack(padx=10 , pady=10)
        self.email = ctk.CTkEntry(master=self.frame1, placeholder_text="E-mail")
        self.email.pack(pady=10, padx=10, )
        label_address = ctk.CTkLabel(master= self.frame1, text="Address", font=("Times New Roman", 20), text_color="orange")
        label_address.pack(padx=10 , pady=10)
        self.address = ctk.CTkEntry(master=self.frame1, placeholder_text="Address")
        self.address.pack(pady=10, padx=10,)
        label_vaccine = ctk.CTkLabel(master=self.frame1, text= "Vaccine", font=("Times New Roman", 20), text_color="orange")
        label_vaccine.pack(padx=12 , pady=10)
        self.vaccine_checkbox =ctk.StringVar() 
        ctk.CTkRadioButton(master= self.frame1, text="No Dose", font=("Times New Roman",12), variable=self.vaccine_checkbox, value="No Dose").pack()
        ctk.CTkRadioButton(master= self.frame1, text="1st Dose", font=("Times New Roman",12), variable=self.vaccine_checkbox, value="1st Dose").pack()
        ctk.CTkRadioButton(master= self.frame1, text="2nd Dose", font=("Times New Roman",12), variable=self.vaccine_checkbox, value="2nd Dose").pack()
        ctk.CTkRadioButton(master= self.frame1, text="1st Booster", font=("Times New Roman",12), variable=self.vaccine_checkbox, value="1st Booster").pack()
        ctk.CTkRadioButton(master= self.frame1, text="2nd Booster", font=("Times New Roman",12), variable=self.vaccine_checkbox, value="2nd Booster").pack()
        label_symptomas = ctk.CTkLabel(master= self.frame1, text="Symptoms", font=("Times New Roman", 20), text_color="orange")
        label_symptomas.pack(padx=12, pady=10)
        self.symptomas_fever = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Fever", variable=self.symptomas_fever, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_headache = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Headache", variable=self.symptomas_headache, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_cough = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Cough", variable=self.symptomas_cough, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_sob = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Shortness of breath", variable=self.symptomas_sob, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_colds = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Colds", variable=self.symptomas_colds, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_dob = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Difficulty of breathing", variable=self.symptomas_dob, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_pain = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Muscle/body pains", variable=self.symptomas_pain, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_lot = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Loss of taste", variable=self.symptomas_lot, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_los = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Loss of smell", variable=self.symptomas_los, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_sorethroat = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Sore throat", variable=self.symptomas_sorethroat, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_diarreah = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Diarrhea", variable=self.symptomas_diarreah, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        self.symptomas_nob = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="None of the above", variable=self.symptomas_nob, font=("Times New Roman", 12), onvalue="a", offvalue=None).pack()
        label_covid_contact = ctk.CTkLabel(master= self.frame1, text="Have you ever had any contact with a person positive of covid?", font=("Times New Roman", 15), text_color="orange")
        label_covid_contact.pack(padx=10 , pady=10)
        self.covid_contact = ctk.StringVar()
        ctk.CTkRadioButton(master= self.frame1, text="Yes", font=("Times New Roman",12), variable=self.covid_contact, value="Yes").pack()
        ctk.CTkRadioButton(master= self.frame1, text="No", font=("Times New Roman",12), variable=self.covid_contact, value="No").pack()
        label_covid_tested = ctk.CTkLabel(master= self.frame1, text="Have you been tested for Covid-19 in the last 14 days?", font=("Times New Roman", 15), text_color="orange")
        label_covid_tested.pack(padx=10 , pady=10)
        self.covid_tested = ctk.StringVar()
        ctk.CTkRadioButton(master= self.frame1, text="No", font=("Times New Roman",12), variable=self.covid_tested, value="No").pack()
        ctk.CTkRadioButton(master= self.frame1, text="Yes-Positive", font=("Times New Roman",12), variable=self.covid_tested, value="Yes Positive").pack()
        ctk.CTkRadioButton(master= self.frame1, text="Yes-Negative", font=("Times New Roman",12), variable=self.covid_tested, value="Yes Negative").pack()
        ctk.CTkRadioButton(master= self.frame1, text="Yes-Pending", font=("Times New Roman",12), variable=self.covid_tested, value="Yes Pending").pack()
        # create a method of getting the information and write it in a excel file
        def get_information():
            name = self.first_name.get() +" " +self.last_name.get()
            number = int(self.phone_number.get())
            email = self.email.get()
            address = self.address.get()
            vaccine = self.vaccine_checkbox.get()
            symptoms = {"Fever":self.symptomas_fever.get(), "Headache" : self.symptomas_headache.get(), "Cough": self.symptomas_cough.get(), "Shortness of breath" : self.symptomas_sob.get(), "Colds":self.symptomas_colds.get(), "Difficulty of Breathing": self.symptomas_dob.get(), "Muscles/Body Pain": self.symptomas_pain.get(), "Loss of Taste": self.symptomas_lot.get(), "Loss of Smell": self.symptomas_los.get(), "Sore Throat": self.symptomas_sorethroat.get(), "Diarrhea":self.symptomas_diarreah.get(), "None of the Above": self.symptomas_nob.get()}
            contact_covid = self.covid_contact.get()
            covid_test = self.covid_tested.get()
            syntomps = ' / '.join(key for key, value in symptoms.items() if value != "")
            checkers  = not True
            try:
                with open("respondent_information.csv", "r") as chickrs:
                    reading = csv.reader(chickrs)
                    if any(reading):
                        checkers = True
            except FileNotFoundError:
                pass
            try:
                if not (name and number and email and address and vaccine and contact_covid and covid_test):
                    messagebox.showerror("No Input","Please put an input to everything")
                    return
                elif syntomps == "":
                    messagebox.showerror("No Checkmark","PLease check at least 1 in the symptoms or non of the above")
                else:
                    with open("respondent_information.csv", "a" , newline="") as filler:
                        info = csv.writer(filler)
                        if not checkers:
                            info.writerow(['Name', 'Phone Number', 'Email', 'Address', 'Vaccine', 'Symptoms', 'Contact Covid', 'Covid Tested'])
                        info.writerow([name , number, email, address, vaccine, syntomps, contact_covid, covid_test])
            except ValueError:
                messagebox.showerror("Wrong CHaracters in the phone number", "Please input numbers only")
                return
            self.app.destroy()
        reg_btn = ctk.CTkButton(master=self.frame1, text="Register", font=("Times New Roman",12), command=get_information).pack(pady=10,padx=12)
        
    # create a method for starting the mainloop of the window
    def mainloop(self):
        self.app.mainloop()
    
    
    

                