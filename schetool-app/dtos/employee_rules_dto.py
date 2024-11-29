from dataclasses import dataclass


@dataclass
class EmployeeRulesDto:
    employee_id: int
    rule_id: int
