import employees_repository as repository
from dtos.employees_dto import EmployeesDto
from typing import Optional


def add_employee(employee: EmployeesDto) -> None:
    repository.add_employee(employee)

def get_employees() -> list[EmployeesDto]:
    return repository.get_employees()

def get_employee_by_id(employee_id: int) -> Optional[EmployeesDto]:
    return repository.get_employee_by_id(employee_id)

def delete_employee(employee_id: int) -> None:
    repository.delete_employee(employee_id)
