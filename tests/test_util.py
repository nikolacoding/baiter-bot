from util import is_admin
from constants import admin_ids

def test_is_admin():
    for admin_id in admin_ids:
        assert is_admin(admin_id) == True