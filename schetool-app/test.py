import roles_service as roles_service
from dtos.roles_dto import RolesDto
import employees_service as employees_service


role = RolesDto(
    role_id=None,
    role_name="DEPENDIENTE"
)
#add_role(role)
print(employees_service.get_employees())
print(roles_service.get_roles())
print(roles_service.get_role_by_id(1).role_name)
