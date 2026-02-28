import constants
from random import choice

def is_admin(id) -> bool:
    return id in constants.admin_ids

def is_privileged_user(id) -> bool:
    return id in constants.privileged_user_ids

def is_forbidden_activity(activity_name) -> bool:
    for fa in constants.forbidden_activities:
        if fa in activity_name.lower():
            return True
        
    return False

def pick_a_line_from_file(file_name: str) -> str:
    lines = []
    ch = str()
    with open(file_name, "r") as f:
        lines = f.readlines()
        ch = choice(lines)

    return ch