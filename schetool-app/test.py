from roles_repository import *



role = RolesDto(
    role_id=None,
    role_name="DEPENDIENTE"
)
#add_role(role)
print(get_roles())
print(get_role_by_id(1).role_name)
