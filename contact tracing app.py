#to be made
import customtkinter as ctk
from GUI_Registration_class import RegistrationGUI
from GUI_Searcher_class import SearcherGUI


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.geometry("850x400")
window.resizable(height=False, width=False)
window.title("Main Page")
frame1= ctk.CTkScrollableFrame(master= window)
frame1.pack(fill=ctk.BOTH,expand="yes",padx= 60 , pady=20)
label_title = ctk.CTkLabel(master= frame1, text="Neil's Contact Tracing Application", font=("Times New Roman", 40), text_color="#7DF9FF")
label_title.pack(padx=10 , pady=12)
label_title_name = ctk.CTkLabel(master= frame1, text="Home Page", font=("Times New Roman", 30), text_color="#7DF9FF")
label_title_name.pack(padx=10 , pady=12)
label_registration = ctk.CTkLabel(master = frame1, text="Registraion app", font=("Times New Roman", 20), text_color="orange")
label_registration.pack(padx=10, pady=12)

def register_information():
    ui_reg = RegistrationGUI()
    ui_reg.registration()
    ui_reg.mainloop()
def search_information():
    ui_srch= SearcherGUI()
    ui_srch.ui_hanap()
    ui_srch.mainloops()

btn_registation = ctk.CTkButton(master= frame1, text="Registration", font=("Times New Roman", 10), command=register_information)
btn_registation.pack(padx=10, pady=12)
label_search = ctk.CTkLabel(master = frame1, text="Search app", font=("Times New Roman", 20), text_color="orange")
label_search.pack(padx=10, pady=12)
btn_search = ctk.CTkButton(master= frame1, text="Search App",font=("Times New Roman", 10), command=search_information)
btn_search.pack(padx=10, pady=12)

window.mainloop()