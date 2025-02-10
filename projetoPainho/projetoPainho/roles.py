from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions={'ver_avisos':True, 'gerenciar_notas': True, 'ver_notas':True, 'gerenciar_diarios': True, 'ver_diarios':True, 'ver_avisos' :True, 'ver_calendario':True}

class Cliente(AbstractUserRole):
    available_permissions={'ver_notas': True, 'ver_diarios': True, 'ver_avisos':True}
    