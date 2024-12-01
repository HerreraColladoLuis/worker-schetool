import sqlite3


ADD_EMPLOYEES_QUERY = ("INSERT INTO employees (employee_name, employee_surname, employee_email, employee_phone_number, "
                       "employee_role) VALUES (?, ?, ?, ?, ?, ?)")
GET_ALL_EMPLOYEES_QUERY = "SELECT * FROM employees"
GET_EMPLOYEE_BY_ID_QUERY = "SELECT * FROM employees WHERE employee_id = ?"
DELETE_EMPLOYEE_QUERY = "DELETE FROM employees WHERE employee_id = ?"


def get_connection(database: str):
    return sqlite3.connect(database)
