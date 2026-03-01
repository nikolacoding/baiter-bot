import util

def test_is_admin():
    for admin_id in util.parse_lines("config/admin_ids.cfg"):
        assert util.is_admin(admin_id) == True

def test_is_privileged_user():
    for user_id in util.parse_lines("config/privileged_user_ids.cfg"):
        assert util.is_privileged_user(user_id)

def test_is_forbidden_activity():
    for fa in util.parse_lines("config/forbidden_activities.cfg"):
        assert util.is_forbidden_activity(fa)
        assert util.is_forbidden_activity(fa.upper()) 

def test_pick_a_line_from_file():
    test_file_name = "pozdravi.txt"
    test_file_lines = []

    with open(test_file_name, "r") as f:
        test_file_lines = f.readlines()
        for i in range(50):
            assert util.pick_a_line_from_file(test_file_name) in [line.strip() for line in test_file_lines]

def test_parse_lines():
    lines = util.parse_lines("tests/test_parse_lines_helper.txt")

    # hardkodovani primjeri iz fajla ^
    assert lines[0].strip() == "A"
    assert lines[1].strip() == "Bb"
    assert lines[2].strip() == "Ccc"
    assert lines[3].strip() == "Dddd"
    assert lines[4].strip() == "Eee"
    assert lines[5].strip() == "Ff"
    assert lines[6].strip() == "G"

def test_parse_csv_pairs():
    pairs = util.parse_csv_pairs("tests/test_parse_csv_pairs_helper.txt")

    # hardkodovani primjeri iz fajla ^
    assert pairs["jedan"].strip() == "dva"
    assert pairs["1"].strip() == "2"
    assert pairs["emoji"].strip() == "✌🏻"
    assert pairs["whitespace"].strip() == ""
    assert pairs["int"].strip() == "123"
    assert pairs["4.5"].strip() == "float"