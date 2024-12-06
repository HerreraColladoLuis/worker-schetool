from dataclasses import dataclass


@dataclass
class RolesDto:
    role_id: int
    role_name: str

    @staticmethod
    def from_row(row):
        return RolesDto(*row) if row else None
