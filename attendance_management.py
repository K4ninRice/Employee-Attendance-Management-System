class Attendance:
    def __init__(self, connection, role):
        self.connection = connection
        self.role = role

    def add(self, employee_id, attendance_date, status):
        if self.role != 'admin':
            return "Permission denied: Only admins can add attendance."
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO attendance (employee_id, attendance_date, status) VALUES (%s, %s, %s)",
                (employee_id, attendance_date, status)
            )
            self.connection.commit()
            return "Attendance added successfully!"
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()

    def update(self, attendance_id, status):
        if self.role != 'admin':
            return "Permission denied: Only admins can update attendance."
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "UPDATE attendance SET status = %s WHERE attendance_id = %s",
                (status, attendance_id)
            )
            self.connection.commit()
            return f"Attendance ID {attendance_id} updated successfully."
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()

    def delete(self, attendance_id):
        if self.role != 'admin':
            return "Permission denied: Only admins can delete attendance."
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM attendance WHERE attendance_id = %s", (attendance_id,))
            self.connection.commit()
            return f"Attendance ID {attendance_id} deleted successfully."
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()

    def view(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM attendance")
        records = cursor.fetchall()
        cursor.close()
        return records
