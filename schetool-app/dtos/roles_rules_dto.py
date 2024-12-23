from dataclasses import dataclass


@dataclass
class RolesRulesDto:
    role_id: int
    rule_id: int

    @staticmethod
    def from_row(row):
        return RolesRulesDto(*row) if row else None
