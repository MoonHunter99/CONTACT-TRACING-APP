# import customtkinter
import customtkinter
# import csv
import csv
# create a class for the registration segment
class RegistrationGUI:
    # create a constructor of a gui to use for getting the information of registration
    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.app = customtkinter.CTk()
        self.app.geometry("1600x900")
        self.app.title("Neil's Personal Contact Tracing Application")
        frame1= customtkinter.CTkScrollableFrame(master= self.app)
        frame1.pack(fill=customtkinter.BOTH,expand="yes",padx= 60 , pady=20)
        label_Title = customtkinter.CTkLabel(master= frame1, text="Neil's Contact Tracing Application", font=("Times New Roman", 40), text_color="blue")
        label_Title.pack(padx=10 , pady=12)
        label_first_name = customtkinter.CTkLabel(master= frame1, text="First Name", font=("Times New Roman", 20), text_color="orange")
        label_first_name.pack(padx=10 , pady=10)
        self.first_name = customtkinter.CTkEntry(master=frame1, placeholder_text="First Name")
        self.first_name.pack(pady=10, padx=10, )
        label_last_name = customtkinter.CTkLabel(master= frame1, text="Last Name", font=("Times New Roman", 20), text_color="orange")
        label_last_name.pack(padx=10 , pady=10)
        self.last_name = customtkinter.CTkEntry(master=frame1, placeholder_text="Last Name")
        self.last_name.pack(pady=10, padx=10,)
        phone_number_label = customtkinter.CTkLabel(master= frame1, text="Phone Number", font=("Times New Roman", 20), text_color="orange")
        phone_number_label.pack(padx=10 , pady=10)
        self.phone_number = customtkinter.CTkEntry(master=frame1, placeholder_text="09XXXXXXXXX")
        self.phone_number.pack(pady=10, padx=10, )
        label_email = customtkinter.CTkLabel(master= frame1, text="E-mail", font=("Times New Roman", 20), text_color="orange")
        label_email.pack(padx=10 , pady=10)
        self.email = customtkinter.CTkEntry(master=frame1, placeholder_text="E-mail")
        self.email.pack(pady=10, padx=10, )
        label_address = customtkinter.CTkLabel(master= frame1, text="Address", font=("Times New Roman", 20), text_color="orange")
        label_address.pack(padx=10 , pady=10)
        self.address = customtkinter.CTkEntry(master=frame1, placeholder_text="Address")
        self.address.pack(pady=10, padx=10,)
        label_vaccine = customtkinter.CTkLabel(master=frame1, text= "Vaccine", font=("Times New Roman", 20), text_color="orange")
        label_vaccine.pack(padx=12 , pady=10)
        checkbox_vaccine_options = ["No Vaccine","1st Dose","2nd Dose","1st Booster","2nd Booster"]
        self.vaccine_checkbox = [customtkinter.IntVar() for _ in range(len(checkbox_vaccine_options))]
        for i, option in enumerate(checkbox_vaccine_options):
            customtkinter.CTkCheckBox(frame1, text=option, variable=self.vaccine_checkbox[i], font=("Times New Roman", 12)).pack()
        label_symptoms = customtkinter.CTkLabel(master= frame1, text="Symptoms", font=("Times New Roman", 20), text_color="orange")
        label_symptoms.pack(padx=12, pady=10)
        checkbox_symptoms_options = ["Fever","Headache","Cough","Shortness of breath","Colds", "Difficulty of breathing", "Muscle/body pains", "Loss of taste", "Loss of smell", "Sore throat", "Diarrhea"]
        self.symptoms_checkbox = [customtkinter.IntVar() for _ in range(len(checkbox_symptoms_options))]
        for i, option in enumerate(checkbox_symptoms_options):
            customtkinter.CTkCheckBox(frame1, text=option, variable=self.symptoms_checkbox[i], font=("Times New Roman", 12)).pack()
    # create a method for starting the mainloop of the window
    def mainloop(self):
        self.app.mainloop()
    # create a method of getting the information and write it in a excel file