from dataclasses import dataclass


@dataclass
class EmployeeRulesDto:
    employee_id: int
    rule_id: int

    @staticmethod
    def from_row(row):
        return EmployeeRulesDto(*row) if row else None
