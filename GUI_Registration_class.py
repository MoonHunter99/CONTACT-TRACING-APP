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
        app = customtkinter.CTk()
        app.geometry("1600x900")
        app.title("Neil's Personal Contact Tracing Application")
        frame1= customtkinter.CTkFrame(master= app)
        frame1.pack(padx= 60 , pady=20)
        label_Title = customtkinter.CTkLabel(master= frame1, text="Neil's Contact Tracing Application", font=("Times New Roman", 40), text_color="blue")
        label_Title.pack(padx=10 , pady=12)
        label_first_name = customtkinter.CTkLabel(master= frame1, text="First Name", font=("Times New Roman", 20), text_color="orange")
        label_first_name.pack(padx=10 , pady=10)
        first_name = customtkinter.CTkEntry(master=frame1, placeholder_text="First Name")
        first_name.pack(pady=10, padx=10)
        app.mainloop()
# create a method for starting the mainloop of the window
# create a method of getting the information and write it in a excel file