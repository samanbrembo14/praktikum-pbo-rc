import tkinter as tk
from tkinter import ttk, messagebox

class RegisterQuestionsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registration Questions")
        self.geometry("700x470")
        self.parent = parent

        self.questions = [
            {"question": "Siapa orang paling ganteng?", "options": ["Chris Evan", "Chaeunwoo", "Alwi", "V"], "answer": "Alwi", "error_message": "Masa gatau siapa yg ganteng"},
            {"question": "Siapa orang Pacar Alwi sekarang?", "options": ["Zee", "Shani", "Gita", "Ella"], "answer": "Ella", "error_message": "Masa lu gatau pacar gw bang"},
            {"question": "Kenapa Ella mau sama Alwi ?", "options": ["Ya karna ganteng lah", "Gatau", "Halu bejir", "Pinter banget anjr"], "answer": "Halu bejir", "error_message": "plis bang bilang aku halu bejir"}
        ]
        
        self.answers = []

        self.create_widgets()

    def create_widgets(self):
        for i, question_data in enumerate(self.questions):
            question_label = tk.Label(self, text=question_data["question"])
            question_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

            selected_option = tk.StringVar(value=None)

            options_frame = tk.Frame(self)
            options_frame.grid(row=i, column=1, padx=10, pady=5, sticky="w")

            for j, option in enumerate(question_data["options"]):
                rb = tk.Radiobutton(options_frame, text=option, variable=selected_option, value=option)
                rb.grid(row=j, column=0, sticky="w")

            self.answers.append(selected_option)

        ttk.Button(self, text="Submit", command=self.validate_answers).grid(row=len(self.questions), column=0, columnspan=2, padx=10, pady=10)

    def validate_answers(self):
        for i, question_data in enumerate(self.questions):
            if self.answers[i].get() != question_data["answer"]:
                messagebox.showerror("ADUH BANG", question_data["error_message"])
                return

        messagebox.showinfo("MANTAP BANG", "KAWAN TEBAIK AKU.")
        self.parent.enable_registration()

class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Register Form")
        self.geometry("300x150")
        self.parent = parent

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.add_label_entry("Username:", self.username_var, row=0)
        self.add_label_entry("Password:", self.password_var, row=1)

        ttk.Button(self, text="Register", command=self.validate_registration).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def add_label_entry(self, label_text, var, row):
        tk.Label(self, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(self, textvariable=var)
        if label_text == "Password:":
            entry.config(show="*")
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")

    def validate_registration(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if not username.strip() or not password.strip():
            messagebox.showerror("Registration Failed", "Username and password cannot be empty!")
            return

        if username in registered_users:
            messagebox.showerror("Registration Failed", "Username already exists!")
        else:
            # Store registration data and open security questions window
            self.parent.registration_data = {"username": username, "password": password}
            RegisterQuestionsWindow(self)

    def enable_registration(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if not username.strip() or not password.strip():
            messagebox.showerror("Registration Failed", "Username and password cannot be empty!")
            return

        registered_users[username] = password
        messagebox.showinfo("MANTAP BANG", "YEEEE!")
        self.destroy()

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("300x150")

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.registration_data = {}

        self.add_label_entry("Username:", self.username_var, row=0)
        self.add_label_entry("Password:", self.password_var, row=1)

        ttk.Button(self, text="Login", command=self.validate_login).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        ttk.Button(self, text="Register", command=self.open_register_window).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_label_entry(self, label_text, var, row):
        tk.Label(self, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = tk.Entry(self, textvariable=var)
        if label_text == "Password:":
            entry.config(show="*")
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")

    def validate_login(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if username in registered_users and registered_users[username] == password:
            messagebox.showinfo("Login Successful", f"HALO BANG {username}!")
        else:
            messagebox.showerror("Login Failed", "ANJR LU SIAPA?")

    def open_register_window(self):
        RegisterWindow(self)

if __name__ == "__main__":
    registered_users = {"alwi": "ganteng"}  # Menambahkan satu username dan password awal
    login_window = LoginWindow()
    login_window.mainloop()

