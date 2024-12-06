from dtos.roles_dto import RolesDto
from utils.settings import DB_NAME
from utils.database_utils import Database
from typing import Optional

db = Database(DB_NAME)

def add_role(role: RolesDto) -> None:
    query = (
        "INSERT INTO roles (role_name) VALUES (?)"
    )
    params = (role.role_name,)
    db.execute_query(query, params)


def get_roles() -> list[RolesDto]:
    query = "SELECT * FROM roles"
    rows = db.fetch_all(query)
    return [RolesDto(*row) for row in rows]


def get_role_by_id(role_id: int) -> Optional[RolesDto]:
    query = "SELECT * FROM roles WHERE role_id = ?"
    row = db.fetch_one(query, (role_id,))
    return RolesDto.from_row(row)


def get_role_by_name(role_name: str) -> Optional[RolesDto]:
    query = "SELECT * FROM roles WHERE role_name = ?"
    row = db.fetch_one(query, (role_name,))
    return RolesDto.from_row(row)


def delete_role(role_id: int) -> None:
    query = "DELETE FROM roles WHERE role_id = ?"
    db.execute_query(query, (role_id,))
