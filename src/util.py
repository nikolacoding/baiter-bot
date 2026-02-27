import constants

def is_admin(id) -> bool:
    return id in constants.admin_ids