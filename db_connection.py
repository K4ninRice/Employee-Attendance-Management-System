import mysql.connector
from tkinter import messagebox


class ConnectionToDatabase:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost", user="root", passwd="EAsystem", database="employee_management"
            )
            if self.connection.is_connected():
                return self.connection
        except mysql.connector.Error as error:
            messagebox.showerror("Database Error", f"Cannot connect to database: {error}")
            return None

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
