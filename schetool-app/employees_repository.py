from dtos.employees_dto import EmployeesDto
from utils.settings import DB_NAME
from utils.database_utils import (get_connection, ADD_EMPLOYEES_QUERY, GET_ALL_EMPLOYEES_QUERY,
                                  GET_EMPLOYEE_BY_ID_QUERY, DELETE_EMPLOYEE_QUERY)


def add_employee(employee: EmployeesDto):
    db = get_connection(DB_NAME)
    cursor = db.cursor()
    cursor.execute(ADD_EMPLOYEES_QUERY, (EmployeesDto.employee_name, EmployeesDto.employee_surname,
                                         EmployeesDto.employee_email, EmployeesDto.employee_phone_number,
                                         EmployeesDto.employee_role))
    db.commit()
    employee.employee_id = cursor.lastrowid
    db.close()
    return employee


def get_employees():
    db = get_connection(DB_NAME)
    cursor = db.cursor()
    cursor.execute(GET_ALL_EMPLOYEES_QUERY)
    employees = cursor.fetchall()
    db.close()
    return employees


def get_employee(employee_id: int):
    db = get_connection(DB_NAME)
    cursor = db.cursor(GET_EMPLOYEE_BY_ID_QUERY, str(employee_id))
    cursor.execute()
    employee = cursor.fetchone()
    db.close()
    return employee


def delete_employee(employee_id: int):
    db = get_connection(DB_NAME)
    cursor = db.cursor()
    cursor.execute(DELETE_EMPLOYEE_QUERY, str(employee_id))
    db.commit()
    db.close()
