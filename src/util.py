from typing import List
from random import choice

def parse_lines(filename: str) -> List[str]:
    initial = []
    res = []
    with open(filename, "r", encoding = "utf-8") as f:
        initial = f.readlines()
    
    res = [line.strip() for line in initial if (line and not line.startswith("#") and not line.isspace())]
    return res

def parse_csv_pairs(filename: str) -> dict:
    res = {}
    lines = parse_lines(filename)

    for line in lines:
        pair = line.split(",")
        res[pair[0]] = pair[1]

    return res

# kesiran prvi poziv za internu upotrebu
admin_ids = parse_lines("config/admin_ids.cfg") 
privileged_users = parse_lines("config/privileged_user_ids.cfg")
forbidden_activities = parse_lines("config/forbidden_activities.cfg")

def is_admin(id) -> bool:
    return id in admin_ids

def is_privileged_user(id) -> bool:
    return id in privileged_users

def is_forbidden_activity(activity_name) -> bool:
    for fa in forbidden_activities:
        if fa in activity_name.lower():
            return True
        
    return False

def pick_a_line_from_file(file_name: str) -> str:
    lines = []
    ch = str()
    with open(file_name, "r", encoding = "utf-8") as f:
        lines = f.readlines()
        ch = choice(lines)

    return ch