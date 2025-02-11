from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions={}

class Cliente(AbstractUserRole):
    available_permissions={}
    