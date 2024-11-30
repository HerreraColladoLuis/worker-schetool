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
    id_inserted = cursor.lastrowid
    db.close()
    return id_inserted
