from dataclasses import dataclass

@dataclass
class EmployeesDto:
    employee_id: int
    employee_name: str
    employee_surname: str
    employee_email: str
    employee_phone_number: str
    employee_weekly_hours: int
    employee_role: int
