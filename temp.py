import tkinter as tk
from tkinter import Checkbutton, Entry, messagebox
import json
import re

class Person:
    def __init__(self, user_id, name, password, role="",phone="", email="", gender=""):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.role=role
        self.phone = phone
        self.email = email
        self.gender = gender

class Teacher(Person):
    def __init__(self, user_id, name, password,role,subject, phone="", email="", gender=""):
        super().__init__(user_id, name, password,role,phone, email, gender)
        self.subject = subject

class Student(Person):
    def __init__(self, user_id, name, password,role, department, phone="", email="", gender=""):
        super().__init__(user_id, name, password, role,phone, email, gender)
        self.department = department
class UGStudent(Student):
    def __init__(self, user_id, name, password, role,department, phone="", email="", gender=""):
        super().__init__(user_id, name, password,role,phone, email, gender)
        self.department = department

class PGStudent(Student):
    def __init__(self, user_id, name, password,department, phone="", email="", gender=""):
        super().__init__(user_id, name, password,phone, email, gender)
        self.department = department




class RegistrationGUI:
    def __init__(self, master, user_database, main_app):
        self.master = master
        self.main_app = main_app
        self.user_database = user_database
        self.master.title("New User Registration")

        bg_color = "#333333"  
        button_bg_color = "#4CAF50"  # Green
        button_fg_color = "white"  # White
        label_fg_color = "white" 
        entry_bg_color = "white"


        # Main frame
        main_frame = tk.Frame(master, padx=20, pady=30, bg=bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Labels and Entry Widgets
        self.name_label = tk.Label(main_frame, text="Name*:", bg=bg_color, fg=label_fg_color)
        self.name_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.user_id_label = tk.Label(main_frame, text="User ID*:", bg=bg_color, fg=label_fg_color)
        self.user_id_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.password_label = tk.Label(main_frame, text="Password*:", bg=bg_color, fg=label_fg_color)
        self.password_entry = tk.Entry(main_frame, show="*", bg=entry_bg_color)
        self.check_button = Checkbutton(main_frame, text="Show Password", command=self.show_password, bg=bg_color,fg="white",selectcolor=bg_color,activebackground=bg_color)

        self.role_var = tk.StringVar(master)
        self.role_var.set("Teacher")
        self.role_label = tk.Label(main_frame, text="Role:", bg=bg_color, fg=label_fg_color)
        self.role_menu = tk.OptionMenu(main_frame, self.role_var, "Teacher", "UG Student", "PG Student")
        self.subject_label = tk.Label(main_frame, text="Subject/Department*:", bg=bg_color, fg=label_fg_color)
        self.subject_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.phone_label = tk.Label(main_frame, text="Phone:", bg=bg_color, fg=label_fg_color)
        self.phone_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.email_label = tk.Label(main_frame, text="Email:", bg=bg_color, fg=label_fg_color)
        self.email_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.phone_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.phone_entry.grid(row=6, column=1, padx=10, pady=10)
        self.email_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")
        self.email_entry.grid(row=7, column=1, padx=10, pady=10)
        self.gender_label = tk.Label(main_frame, text="Gender:", bg=bg_color, fg=label_fg_color)
        self.gender_entry = tk.Entry(main_frame, bg=entry_bg_color)

        # self.register_button = tk.Button(main_frame, text="Register", command=self.register_user, bg=button_bg_color, fg=button_fg_color)
        # self.cancel_button = tk.Button(main_frame, text="Cancel", command=self.on_cancel, bg=button_bg_color, fg=button_fg_color)

        # Layout
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.user_id_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.user_id_entry.grid(row=1, column=1, padx=10, pady=10)
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        self.check_button.grid(row=3, column=1, pady=5)
        self.role_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.role_menu.grid(row=4, column=1, pady=10)
        self.subject_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.subject_entry.grid(row=5, column=1, padx=10, pady=10)
        self.phone_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.phone_entry.grid(row=6, column=1, padx=10, pady=10)
        self.email_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")
        self.email_entry.grid(row=7, column=1, padx=10, pady=10)

        self.gender_label.grid(row=8, column=0, padx=10, pady=10, sticky="e")
        self.gender_entry.grid(row=8, column=1, padx=10, pady=10)
        self.compulsory_label = tk.Label(main_frame, text="Fields indicated by * are Compulsory", bg=bg_color, fg=label_fg_color)
        self.compulsory_label.grid(row=9, column=1, pady=5, sticky="w")


        button_frame = tk.Frame(main_frame, bg=bg_color)
        button_frame.grid(row=10, column=1, columnspan=2, pady=10)

        self.register_button = tk.Button(button_frame, text="Register", command=self.register_user, bg=button_bg_color, fg=button_fg_color)
        self.cancel_button = tk.Button(button_frame, text="Cancel", command=self.on_cancel, bg=button_bg_color, fg=button_fg_color)
        self.register_button.grid(row=0, column=0, padx=15)
        self.cancel_button.grid(row=0, column=1, padx=10)


        self.master.protocol("WM_DELETE_WINDOW", self.on_cancel)  # Handle window closing event

    def on_cancel(self):
        self.master.destroy()
        self.main_app.show_main_application()

    def show_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def PasswordCheck(self,password):
        l, u, p, d = 0, 0, 0, 0
        special_char=["!","@","#","%","&","$","*"]
        if (len(password) >= 8):
            for i in password:
        
                # counting lowercase alphabets 
                if (i.islower()):
                    l+=1
                # counting uppercase alphabets
                if (i.isupper()):
                    u+=1
                # counting digits
                if (i.isdigit()):
                    d+=1
                # counting the mentioned special characters
                if(i in special_char):
                    p+=1
        if (l<1 or u<1 or p<1 or d<1 or l+p+u+d!=len(password)):
            messagebox.showerror("Invalid Password", "Password must be 8-12 characters long, "
                                                    "contain at least one uppercase letter, "
                                                    "one digit, and one special character.")
            return False
        else:
            return True

    def register_user(self):
        name = self.name_entry.get()
        user_id = self.user_id_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()
        subject_or_department = self.subject_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        gender = self.gender_entry.get()
        

        if not name or not user_id or not password  or not subject_or_department:
            messagebox.showerror("Empty Fields", "All fields are required. Please fill in all the details.")
            return False

        # Check email format only if an email is provided
        if email and not self.is_valid_email(email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return False
        if phone and not self.is_valid_phone_number(phone):
            messagebox.showerror("Invalid Phone Number", "Phone number must contain exactly 10 digits.")
            return False
        if self.PasswordCheck(password):
            if user_id in self.user_database:
                messagebox.showerror("Registration Error","User ID already exists. Please enter another User ID")
                return False
            else:

                if role == "Teacher":
                    user = Teacher(user_id, name, password, role,subject_or_department, phone, email, gender)
                else:
                    user = Student(user_id, name, password,role, subject_or_department, phone, email, gender)

                self.user_database[user_id] = user.__dict__

                messagebox.showinfo("Registration Successful", "User registered successfully.")
                self.master.destroy()
                self.main_app.show_main_application()
                return True
       
    def is_valid_email(self, email):
        # Regular expression for basic email validation
        email_regex = r'^\S+@\S+\.\S+$'
        return re.match(email_regex, email) is not None

    def is_valid_phone_number(self, phone):
        # Check if the phone number is exactly 10 digits
        return phone.isdigit() and len(phone) == 10

class AcademicSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Academic System")
        self.user_database = {}
        self.load_user_data()  # Load user data from file on application start

        bg_color = "#333333"  # Dark Grey
        text_color = "#ffffff"  # White
        button_bg_color = "#4CAF50"  # Green
        button_fg_color = "#ffffff"  # White

        # Main frame with the same dark background color
        main_frame = tk.Frame(master, padx=20, pady=20, bg=bg_color)
        main_frame.pack()
        self.master.configure(bg=bg_color)
        # Labels and Entry Widgets
        self.user_id_label = tk.Label(main_frame, text="User ID:", bg=bg_color, fg=text_color)
        self.user_id_entry = tk.Entry(main_frame, bg="white")
        self.password_label = tk.Label(main_frame, text="Password:", bg=bg_color, fg=text_color)
        self.password_entry = tk.Entry(main_frame, show="*", bg="white")
        self.check_button = Checkbutton(main_frame, text="Show Password", command=self.show_password,bg=bg_color,fg=text_color,selectcolor=bg_color,activebackground=bg_color)

        self.login_button = tk.Button(main_frame, text="Login", command=self.login, bg=button_bg_color, fg=button_fg_color)
        self.login_attempts = 3
        self.btn = tk.Button(main_frame, text="Sign Up", command=self.open_registration_window, bg=button_bg_color, fg=button_fg_color)

        # Layout
        self.user_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.user_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        self.check_button.grid(row=2, column=1, pady=10)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew")
        self.btn.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window closing event


    def on_closing(self):
        self.save_user_data()  # Save user data to file before closing the window
        self.master.destroy()

    def save_user_data(self):
        with open("user_data.json", "w") as file:
            json.dump(self.user_database, file)

    def load_user_data(self):
        try:
            with open("user_data.json", "r") as file:
                self.user_database = json.load(file)
        except FileNotFoundError:
            # If the file is not found, it means there's no user data saved yet.
            pass

    def show_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def login(self):
        user_id = self.user_id_entry.get()
        password = self.password_entry.get()

        # Perform authentication (check against stored records)
        authenticated_user = self.authenticate_user(user_id, password)

        if authenticated_user:
            self.open_user_window(user_id)
        else:
            if user_id in self.user_database:
                self.login_attempts -= 1
                if self.login_attempts > 0:
                    messagebox.showwarning("Login Failed", "Invalid credentials. {} attempts left.".format(self.login_attempts))
                else:
                    messagebox.showerror("Account Deactivated", "Too many unsuccessful attempts. Account deactivated.")
                    del self.user_database[user_id]
                    self.master.destroy()

    def authenticate_user(self, user_id, password):
        if user_id in self.user_database:
            user_data = self.user_database.get(user_id, {})
            stored_password = user_data.get("password")
            
            if stored_password == password:
                return True
            else:
                return False
        else:
            messagebox.showerror("Login Error", "User ID does not exist.")
            return False

    def open_user_window(self, user_id):
        self.hide_main_application()
        new_window = tk.Toplevel(self.master)
        new_window.geometry("500x500")
        user_app = UserGUI(new_window, user_id, self.user_database, self)

    def open_registration_window(self):
        self.hide_main_application()
        new_window = tk.Toplevel(self.master)
        new_window.geometry("500x500")
        registration_app = RegistrationGUI(new_window, self.user_database, self)

    def hide_main_application(self):
        self.master.iconify()  # Minimize the main application window

    def show_main_application(self):
        self.master.deiconify()  # Restore the main application window

class EditProfileGUI:
    def __init__(self, master, user_id, user_database, main_app):
        self.master = master
        self.user_database = user_database
        self.user_id = user_id
        self.main_app = main_app
        self.master.title("Edit Profile")

        bg_color = "#333333"  
        button_bg_color = "#4CAF50"  
        button_fg_color = "white"  
        label_fg_color = "white" 
        entry_bg_color = "white" 

        # Main frame
        main_frame = tk.Frame(master, padx=20, pady=20, bg=bg_color)
        main_frame.pack()

        # Labels and Entry Widgets
        self.name_label = tk.Label(main_frame, text="Name:", bg=bg_color, fg=label_fg_color)
        self.name_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.name_entry.insert(0, user_database.get(user_id, {}).get("name", ""))

        self.userid_label = tk.Label(main_frame, text="User ID:", bg=bg_color, fg=label_fg_color)
        self.userID_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.userID_entry.insert(0, self.user_id)

        self.phone_label = tk.Label(main_frame, text="Phone Number:", bg=bg_color, fg=label_fg_color)
        self.phone_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.phone_entry.insert(0, user_database.get(user_id, {}).get("phone", ""))

        self.password_label = tk.Label(main_frame, text="Password:", bg=bg_color, fg=label_fg_color)
        self.password_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.password_entry.insert(0, user_database.get(user_id, {}).get("password", ""))

        self.role_label = tk.Label(main_frame, text="Role:", bg=bg_color, fg=label_fg_color)
        self.role_var = tk.StringVar(master)
        self.role_var.set(user_database.get(user_id, {}).get("role", ""))
        self.role_options = ["Teacher", "UG Student", "PG Student"]
        self.role_menu = tk.OptionMenu(main_frame, self.role_var, *self.role_options)
        self.role_menu.config(bg=entry_bg_color)
        self.role_menu.grid(row=4, column=1, padx=10, pady=10)


        # New Label and Entry Widget for Subject/Department
        self.subject_label = tk.Label(main_frame, text="Subject/Department:", bg=bg_color, fg=label_fg_color)
        self.subject_entry = tk.Entry(main_frame, bg=entry_bg_color)
        if user_database.get(user_id, {}).get("role", "") == "Teacher":
            self.subject_entry.insert(0, user_database.get(user_id, {}).get("subject", ""))
        else:
            self.subject_entry.insert(0, user_database.get(user_id, {}).get("department", ""))

        self.mail_label = tk.Label(main_frame, text="Email:", bg=bg_color, fg=label_fg_color)
        self.mail_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.mail_entry.insert(0, user_database.get(user_id, {}).get("email", ""))

        self.gender_label = tk.Label(main_frame, text="Gender:", bg=bg_color, fg=label_fg_color)
        self.gender_entry = tk.Entry(main_frame, bg=entry_bg_color)
        self.gender_entry.insert(0, user_database.get(user_id, {}).get("gender", ""))


        save_button = tk.Button(main_frame, text="Save Changes", command=self.save_changes, bg=button_bg_color, fg=button_fg_color)
        cancel_button = tk.Button(main_frame, text="Cancel", command=self.on_cancel, bg=button_bg_color, fg=button_fg_color)

        # Layout
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.userid_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.userID_entry.grid(row=1, column=1, padx=10, pady=10)
        self.phone_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.phone_entry.grid(row=2, column=1, padx=10, pady=10)
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10)
        self.role_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        # self.role_entry.grid(row=4, column=1, padx=10, pady=10)
        self.subject_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.subject_entry.grid(row=5, column=1, padx=10, pady=10)
        self.mail_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.mail_entry.grid(row=6, column=1, padx=10, pady=10)
        self.gender_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")
        self.gender_entry.grid(row=7, column=1, padx=10, pady=10)

        save_button.grid(row=8, column=1, pady=10)
        cancel_button.grid(row=9, column=1, pady=10)

        self.master.protocol("WM_DELETE_WINDOW", self.on_cancel)

    def is_valid_phone_number(self, phone):
        # Check if the phone number is exactly 10 digits
        return phone.isdigit() and len(phone) == 10
    def is_valid_email(self, email):
        # Regular expression for basic email validation
        email_regex = r'^\S+@\S+\.\S+$'
        return re.match(email_regex, email) is not None
    
    def check_unique_user_id(self, new_user_id):
        if new_user_id in self.user_database and new_user_id != self.user_id:
            messagebox.showerror("Invalid User ID", "User ID already exists. Please choose another User ID.")
            return False
        else:
            return True

    def save_changes(self):

        new_name = self.name_entry.get()
        new_phone = self.phone_entry.get()
        new_password = self.password_entry.get()
        new_userID = self.userID_entry.get()
        new_role = self.role_var.get()
        new_subject = self.subject_entry.get()
        new_email=self.mail_entry.get()
        new_gender=self.gender_entry.get()
        if not self.check_unique_user_id(new_userID):
            return  
        # Check email format only if an email is provided
        if new_email and not self.is_valid_email(new_email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return False
        if new_phone and not self.is_valid_phone_number(new_phone):
            messagebox.showerror("Invalid Phone Number", "Phone number must contain exactly 10 digits.")
            return False
        self.user_database[self.user_id]["name"] = new_name
        self.user_database[self.user_id]["phone"] = new_phone
        self.user_database[self.user_id]["password"] = new_password
        self.user_database[self.user_id]["mail"]=new_email
        self.user_database[self.user_id]["gender"]=new_gender
        # self.user_database[self.user_id]["subject"] = new_subject
        if new_role == "Teacher":
            if new_role!=self.user_database.get(self.user_id, {}).get("role", ""):
                del self.user_database[self.user_id]["department"]
            self.user_database[self.user_id]["subject"] = new_subject
        else:
            if self.user_database.get(self.user_id, {}).get("role", "") == "Teacher" :
                del self.user_database[self.user_id]["subject"]
            self.user_database[self.user_id]["department"] = new_subject
        self.user_database[self.user_id]["role"] = new_role
        if new_userID != self.user_id:
            self.user_database[new_userID] = self.user_database[self.user_id].copy()
            self.user_database[new_userID]["user_id"] = new_userID
            del self.user_database[self.user_id]

        messagebox.showinfo("Changes Saved", "Profile updated successfully!")
        self.master.destroy()
        new_window = tk.Toplevel(self.main_app.master)
        new_window.geometry("500x500")
        user_app = UserGUI(new_window, new_userID, self.user_database, self.main_app)

        # self.main_app.show_main_application()

    def on_cancel(self):
        self.master.destroy()
        new_window = tk.Toplevel(self.main_app.master)
        new_window.geometry("500x500")
        user_app = UserGUI(new_window, self.user_id, self.user_database, self.main_app)
        
class UserGUI:
    def __init__(self, master, user_id, user_database, main_app):
        self.master = master
        self.main_app = main_app
        self.user_database = user_database
        self.user_id = user_id
        name = self.user_database.get(user_id, {}).get("name")
        self.master.title(name)
        
        bg_color = "#333333"  
        button_bg_color = "#4CAF50"  # Green
        button_fg_color = "white"  # White
        label_fg_color = "white" 
        text_color = "white"


        # Top frame for displaying user information
        top_frame = tk.Frame(master, bg=bg_color)
        top_frame.pack(pady=10)

        self.master.configure(bg=bg_color)
        welcome_label = tk.Label(top_frame, text=f"Welcome, {name}!", font=('Helvetica', 18), bg=bg_color, fg=text_color )
        welcome_label.pack(pady=10)

        user_info_label = tk.Label(top_frame, text="User Information", font=('Helvetica', 14, 'underline'), bg=bg_color, fg=text_color)
        user_info_label.pack(pady=5)

        for key, value in user_database[user_id].items():
            if value:
                label_text = f"{key.capitalize()} : {value.capitalize()}"
                label = tk.Label(top_frame, text=label_text, padx=10, pady=5, bg=bg_color, fg=text_color)
                label.pack()

        # Functionality frame
        function_frame = tk.Frame(master, bg=bg_color)
        function_frame.pack(pady=10)

        edit_profile_button = tk.Button(function_frame, text="Edit Profile", command=self.open_edit_profile, bg=button_bg_color, fg=button_fg_color)
        edit_profile_button.grid(row=0, column=0, padx=10)

        logout_button = tk.Button(function_frame, text="Logout", command=self.on_logout, bg=button_bg_color, fg=button_fg_color)
        logout_button.grid(row=0, column=1, padx=10)

        delete_account_button = tk.Button(function_frame, text="Delete Account", command=self.on_delete_account, bg=button_bg_color, fg=button_fg_color)
        delete_account_button.grid(row=0, column=2, padx=10)
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window closing event

    def on_closing(self):
        self.main_app.show_main_application()
        self.master.destroy()

    def open_edit_profile(self):
        self.master.withdraw()
        edit_profile_window = tk.Toplevel(self.main_app.master)
        edit_profile_window.geometry("500x500")
        edit_profile_window.configure(bg="#333333") 
        EditProfileApp = EditProfileGUI(edit_profile_window, self.user_id, self.user_database, self.main_app)

    def on_logout(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure you want to logout?')
        if answer:
            self.master.destroy()
            self.main_app.show_main_application()

    def on_delete_account(self):
        answer = messagebox.askyesno(title='Confirmation', message='Are you sure you want to delete your account?')
        if answer:
            del self.user_database[self.user_id]
            messagebox.showinfo("Account Deleted", "Your account has been successfully deleted.")
            self.master.destroy()
            self.main_app.show_main_application()



if __name__=="__main__":

    root = tk.Tk()
    root.geometry("500x500")
    app = AcademicSystemGUI(root)
    root.mainloop()
