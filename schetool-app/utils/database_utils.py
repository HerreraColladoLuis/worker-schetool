import sqlite3


ADD_EMPLOYEES_QUERY = ("INSERT INTO employees (employee_name, employee_surname, employee_email, employee_phone_number, "
                       "employee_weekly_hours, employee_role) VALUES (?, ?, ?, ?, ?, ?)")


def get_connection(database: str):
    return sqlite3.connect(database)
