# import customtkinter
import customtkinter as ctk
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
        self.app.title("Neil's Personal Contact Tracing Application")
    def registration(self):
        self.frame1= ctk.CTkScrollableFrame(master= self.app)
        self.frame1.pack(fill=ctk.BOTH,expand="yes",padx= 60 , pady=20)
        label_Title = ctk.CTkLabel(master= self.frame1, text="Neil's Contact Tracing Application", font=("Times New Roman", 40), text_color="#7DF9FF")
        label_Title.pack(padx=10 , pady=12)
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
        label_symptoms = ctk.CTkLabel(master= self.frame1, text="Symptoms", font=("Times New Roman", 20), text_color="orange")
        label_symptoms.pack(padx=12, pady=10)
        checkbox_symptoms_options = ["Fever","Headache","Cough","Shortness of breath","Colds", "Difficulty of breathing", "Muscle/body pains", "Loss of taste", "Loss of smell", "Sore throat", "Diarrhea"]
        self.symptoms_checkbox = ctk.StringVar()
        ctk.CTkCheckBox(self.frame1, text="Fever", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Fever").pack()
        ctk.CTkCheckBox(self.frame1, text="Headache", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Headache").pack()
        ctk.CTkCheckBox(self.frame1, text="Cough", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Cough").pack()
        ctk.CTkCheckBox(self.frame1, text="Shortness of breath", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Shortness of breath").pack()
        ctk.CTkCheckBox(self.frame1, text="Colds", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Colds").pack()
        ctk.CTkCheckBox(self.frame1, text="Difficulty of breathing", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Difficulty of breathing").pack()
        ctk.CTkCheckBox(self.frame1, text="Muscle/body pains", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Muscle/body pains").pack()
        ctk.CTkCheckBox(self.frame1, text="Loss of taste", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Loss of taste").pack()
        ctk.CTkCheckBox(self.frame1, text="Loss of smell", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Loss of smell").pack()
        ctk.CTkCheckBox(self.frame1, text="Sore throat", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Sore throat").pack()
        ctk.CTkCheckBox(self.frame1, text="Diarrhea", variable=self.symptoms_checkbox, font=("Times New Roman", 12), onvalue="Diarrhea").pack()
        reg_btn = ctk.CTkButton(master=self.frame1, text="Register", font=("Times New Roman",12), command=self.get_information).pack()
    # create a method for starting the mainloop of the window
    def mainloop(self):
        self.app.mainloop()
    # create a method of getting the information and write it in a excel file
    def get_information(self):
        print("yolo")        
                