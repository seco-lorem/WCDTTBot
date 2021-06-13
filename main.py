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
    reddit.subreddit(constant.TARGET_SUBREDDIT).contributor.add("seco-nunesap")
    users = read_user_list()

    adjust_ranks(reddit.subreddit(constant.TARGET_SUBREDDIT), users)
    fallen = remove_fallen(reddit.subreddit(constant.TARGET_SUBREDDIT), users)
    news = add_users(reddit)

    generate_recap_post(news, fallen, reddit)
    update_users(users, news, fallen)


if __name__ == '__main__':
    recap()
