from dataclasses import dataclass


@dataclass
class EmployeesDto:
    employee_id: int
    employee_name: str
    employee_surname: str
    employee_email: str
    employee_phone_number: str
    employee_role: int

    @staticmethod
    def from_row(row):
        return EmployeesDto(*row) if row else None
