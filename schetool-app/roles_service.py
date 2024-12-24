import roles_repository as repository
from dtos.roles_dto import RolesDto
from typing import Optional


def add_role(role: RolesDto) -> None:
    repository.add_role(role)

def get_role_by_id(role_id: int) -> Optional[RolesDto]:
    return repository.get_role_by_id(role_id)

def get_roles() -> list[RolesDto]:
    return repository.get_roles()

def get_role_by_name(role_name: str) -> Optional[RolesDto]:
    return repository.get_role_by_name(role_name)

def delete_role(role_id: int) -> None:
    repository.delete_role(role_id)
