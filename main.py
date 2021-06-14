from botUtils import *
import praw
import constant


# I have vastly changed and simplified the main structure. -seco
# edit constant.py to reuse.
def recap():
    reddit = praw.Reddit(
        client_id=constant.CLIENT_ID,
        client_secret=constant.CLIENT_SECRET,
        user_agent=constant.USER_AGENT,
        username=constant.USERNAME,
        password=constant.PASSWORD, )
    users = read_user_list()

    adjust_ranks(reddit.subreddit(constant.TARGET_SUBREDDIT), users)
    fallen = remove_fallen(reddit.subreddit(constant.TARGET_SUBREDDIT), users)
    news = add_users(reddit)

    generate_recap_post(news, fallen, reddit)
    update_users(users, news, fallen)


'''
If everything goes right, we shouldn't have to call the two functions below.
'''


def print_users():
    users = read_user_list()
    for user in users:
        print("####u/" + user)  # + "\nRank:" + users[user]["rank"])


def refresh_user_list():
    reddit = praw.Reddit(
        client_id=constant.CLIENT_ID,
        client_secret=constant.CLIENT_SECRET,
        user_agent=constant.USER_AGENT,
        username=constant.USERNAME,
        password=constant.PASSWORD, )
    users = dict()
    users1 = dict()
    users2 = dict()
    for contributor in reddit.subreddit(constant.TARGET_SUBREDDIT).contributor():
        users[contributor.name] = {
            "rank": constant.RANK_NAMES[0],
            "activityPoint": 0
        }
    update_users(users, users1, users2)
    print_users()


if __name__ == '__main__':
    # refresh_user_list()
    recap()
