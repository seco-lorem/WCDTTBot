
import credentials

TARGET_SUBREDDIT = ""                       # The Private Subreddit

CLIENT_ID       = credentials.CLIENT_ID
CLIENT_SECRET   = credentials.CLIENT_SECRET
USER_AGENT      = credentials.USER_AGENT
USERNAME        = credentials.USERNAME
PASSWORD        = credentials.PASSWORD
ADD_PERR_RECAP  = 100
INTOLERANCY_RATE= 4                         # How many weeks earn you a weak of inactivity pass.
RANK_LIMITS     = [4, 20]                   # in weeks. 0-3 New, 4-19 Usual, 20+ Senior
RANK_NAMES      = ["New", "Usual", "Senior", "ClubFuture"]  # rank at index 3 is invincible (ClubFuture)
