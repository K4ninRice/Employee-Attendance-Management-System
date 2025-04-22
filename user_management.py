import hashlib
from tkinter import messagebox


class User:
    def __init__(self, connection):
        self.connection = connection

    def register(self, username, password, role):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                (username, hashed_password, role)
            )
            self.connection.commit()
            messagebox.showinfo("Success", f"User {username} registered successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not register user: {e}")
        finally:
            cursor.close()

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT username, role FROM users WHERE username = %s AND password = %s",
            (username, hashed_password)
        )
        user = cursor.fetchone()
        cursor.close()
        return user if user else None
