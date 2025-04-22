class Employee:
    def __init__(self, connection, role):
        self.connection = connection
        self.role = role

    def add(self, first_name, last_name, email, phone, hire_date, department_id):
        if self.role != 'admin':
            return "Permission denied: Only admins can add employees."
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO employees (first_name, last_name, email, phone, hire_date, department_id) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (first_name, last_name, email, phone, hire_date, department_id)
            )
            self.connection.commit()
            return "Employee added successfully!"
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()

    def delete(self, employee_id):
        if self.role != 'admin':
            return "Permission denied: Only admins can delete employees."
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM employees WHERE employee_id = %s", (employee_id,))
            self.connection.commit()
            return f"Employee with ID {employee_id} deleted successfully."
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()

    def update(self, employee_id, email, phone):
        if self.role != 'admin':
            return "Permission denied: Only admins can update employees."
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "UPDATE employees SET email = %s, phone = %s WHERE employee_id = %s",
                (email, phone, employee_id)
            )
            self.connection.commit()
            return f"Employee with ID {employee_id} updated successfully."
        except Exception as e:
            return f"Error: {e}"
        finally:
            cursor.close()

    def view(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        cursor.close()
        return employees
