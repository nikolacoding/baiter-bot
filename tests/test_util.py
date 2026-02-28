import util
import constants

def test_is_admin():
    for admin_id in constants.admin_ids:
        assert util.is_admin(admin_id) == True

def test_is_privileged_user():
    for user_id in constants.privileged_user_ids:
        assert util.is_privileged_user(user_id)

def test_is_forbidden_activity():
    for fa in constants.forbidden_activities:
        assert util.is_forbidden_activity(fa)
        assert util.is_forbidden_activity(fa.upper()) 

def test_pick_a_line_from_file():
    test_file_name = "pozdravi.txt"
    test_file_lines = []

    with open(test_file_name, "r") as f:
        test_file_lines = f.readlines()
        for i in range(50):
            assert util.pick_a_line_from_file(test_file_name) in test_file_lines