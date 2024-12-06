from dtos.employees_dto import EmployeesDto
from utils.settings import DB_NAME
from utils.database_utils import Database
from typing import Optional

db = Database(DB_NAME)

def add_employee(employee: EmployeesDto) -> None:
    query = (
        "INSERT INTO employees (employee_name, employee_surname, employee_email, employee_phone_number, "
        "employee_role) VALUES (?, ?, ?, ?, ?, ?)"
    )
    params = (employee.employee_name, employee.employee_surname,employee.employee_email,
              employee.employee_phone_number, employee.employee_role)
    db.execute_query(query, params)


def get_employees() -> list[EmployeesDto]:
    query = "SELECT * FROM employees"
    rows = db.fetch_all(query)
    return [EmployeesDto(*row) for row in rows]


def get_employee_by_id(employee_id: int) -> Optional[EmployeesDto]:
    query = "SELECT * FROM employees WHERE employee_id = ?"
    row = db.fetch_one(query, (employee_id,))
    return EmployeesDto.from_row(row)


def delete_employee_by_id(employee_id: int) -> None:
    query = "DELETE FROM employees WHERE employee_id = ?"
    db.execute_query(query, (employee_id,))
