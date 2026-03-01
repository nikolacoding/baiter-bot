from util import parse_lines as pl
from util import parse_csv_pairs as pcsv

admin_ids = pl("config/admin_ids.cfg")
privileged_user_ids = pl("config/privileged_user_ids.cfg")
channel_ids = pcsv("config/channel_ids.cfg")
content_reactions = pcsv("config/content_reactions.cfg")
forbidden_activities = pl("config/forbidden_activities.cfg")