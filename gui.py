import tkinter as tk
from tkinter import messagebox
from db_connection import ConnectionToDatabase
from user_management import User
from employee_management import Employee
from attendance_management import Attendance


class DatabaseGUI:
    def __init__(self, root):
        self.root = root
        self.db = ConnectionToDatabase()
        self.connection = self.db.connect()
        self.logged_in_user = None
        self.user = User(self.connection)

        # Main Window
        self.root.title("Employee Management System")
        self.root.geometry("900x900")
        self.login_screen()

    def login_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Employee Management System", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def login():
            username = username_entry.get()
            password = password_entry.get()
            user = self.user.login(username, password)
            if user:
                self.logged_in_user = user
                self.create_main_menu()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        tk.Button(self.root, text="Login", command=login).pack(pady=10)
        tk.Button(self.root, text="Register", command=self.register_screen).pack(pady=10)

    def register_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Register New User", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        tk.Label(self.root, text="Role (admin/user):").pack()
        role_entry = tk.Entry(self.root)
        role_entry.pack()

        def register_user():
            username = username_entry.get()
            password = password_entry.get()
            role = role_entry.get()
            if role.lower() not in ["admin", "user"]:
                messagebox.showerror("Error", "Role must be 'admin' or 'user'.")
                return
            self.user.register(username, password, role)
            self.login_screen()

        tk.Button(self.root, text="Register", command=register_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.login_screen).pack(pady=5)

    def create_main_menu(self):
        self.clear_window()
        tk.Label(self.root, text=f"Welcome, {self.logged_in_user[0]}", font=("Arial", 14)).pack(pady=20)

        tk.Button(self.root, text="View Employees", command=self.view_employees_window).pack(pady=5)
        tk.Button(self.root, text="Add Employee", command=self.add_employee_window).pack(pady=5)
        tk.Button(self.root, text="Update Employee", command=self.update_employee_window).pack(pady=5)
        tk.Button(self.root, text="Delete Employee", command=self.delete_employee_window).pack(pady=5)

        tk.Button(self.root, text="View Attendance", command=self.view_attendance_window).pack(pady=5)
        tk.Button(self.root, text="Add Attendance", command=self.add_attendance_window).pack(pady=5)
        tk.Button(self.root, text="Update Attendance", command=self.update_attendance_window).pack(pady=5)
        tk.Button(self.root, text="Delete Attendance", command=self.delete_attendance_window).pack(pady=5)

        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=10)

   

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

