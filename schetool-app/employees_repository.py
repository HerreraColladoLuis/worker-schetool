from dtos.employees_dto import EmployeesDto
from utils.settings import DB_NAME
from utils.database_utils import get_connection, ADD_EMPLOYEES_QUERY


def add_employee(employee: EmployeesDto):
    db = get_connection(DB_NAME)
    cursor = db.cursor()
    cursor.execute(ADD_EMPLOYEES_QUERY, (EmployeesDto.employee_name, EmployeesDto.employee_surname,
                                         EmployeesDto.employee_email, EmployeesDto.employee_phone_number,
                                         EmployeesDto.employee_weekly_hours, EmployeesDto.employee_role))
    db.commit()
    employee.employee_id = cursor.lastrowid
    db.close()
    return employee


def get_employees():
    db = get_connection(DB_NAME)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    db.close()
    return employees


def get_employee(employee_id: int):
    db = get_connection(DB_NAME)
    cursor = db.cursor("SELECT * FROM employees WHERE employee_id = ?", str(employee_id))
    cursor.execute()
    employee = cursor.fetchone()
    db.close()
    return employee


def delete_employee(employee_id: int):
    db = get_connection(DB_NAME)
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE employee_id = ?", str(employee_id))
    db.commit()
    db.close()
