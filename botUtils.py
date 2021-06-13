import json
from datetime import date
import constant


def read_user_list():
    print('readUserList')
    with open('./userList.json') as f:
        userList = json.load(f)
    f.close()
    return userList


def update_users(user_list, newUsers, fallenList):
    for user in fallenList:
        del user_list[user]
    for user in newUsers:
        user_list[user] = newUsers[user]

    with open('userList.json', 'w') as outfile:
        json.dump(user_list, outfile)
    outfile.close()
    return user_list


def generate_recap_post(newUsers, fallenList, reddit):
    today = date.today()
    title = "Recap: " + str(today)
    body = '#Weekly recap post.\n---------------------\n#New members\n'
    for user in newUsers:
        body += '##' + "u/" + user + '\n'
    body += '#\n---------------------\nUsers removed:\n'
    for user in fallenList:
        body += '##' + "u/" + user + '\n'
    body += "\n---------------------\n\n\n##Why am I here?\nYou have been chosen by the algorithm.\n##How do I get out"\
            + "\nWait. You'll be kicked due to inactivity.\n\n##If\nyou do not post or comment on any post made "\
            + "beginning bg this recap, till next recap. \nEach " + str(constant.INTOLERANCY_RATE)\
            + " weeks you stay, you gain 1 more chance."

    sub = reddit.subreddit(constant.TARGET_SUBREDDIT)
    sub.submit(title, selftext=body)


'''
Anything over this comment, I did not modify the codes functionality.
        below this comment, I have completely rewritten. -seco
'''


def adjust_ranks(subreddit, users):
    # I think we may use a different Ranking algorithm.
    for user in users:
        users[user]["activityPoint"] += 1
        if users[user]["activityPoint"] == constant.RANK_LIMITS[0] and users[user]["rank"] == constant.RANK_NAMES[0]:
            users[user]["rank"] = constant.RANK_NAMES[1]
        elif users[user]["activityPoint"] == constant.RANK_LIMITS[1] and users[user]["rank"] == constant.RANK_NAMES[1]:
            users[user]["rank"] = constant.RANK_NAMES[2]


# DOES NOT COUNT THE COMMENTS TO OLDER POSTS. IN OTHER WORDS, YOU MAY BE KICKED EVEN IF YOU COMMENT ON A POST PRIOR TO
# LAST RECAP. We may want to use a different randomly adding algorithm. But this one has the advantage of not operating
# according to time but only to last recap.
def remove_fallen(subreddit, users):
    actives = []
    fallen = dict()
    file = open(r"last_post_id.txt", "r")
    last_post_id = file.read()
    file.close()

    first_iteration = True
    for submission in subreddit.new():
        if first_iteration:
            file1 = open("last_post_id.txt", "w")
            file1.write(submission.id)
            file1.close()

        actives.append(submission.author.name)
        for comment in submission.comments:
            actives.append(submission.author.name)
        if submission.id == last_post_id:
            break
        first_iteration = False

    for user in users:
        active = False
        for x in actives:
            if x == user:
                active = True
                break
        if not active:
            # How should we behave to inactives depending on their ranks?
            users[user]["activityPoint"] -= constant.INTOLERANCY_RATE
            if users[user]["activityPoint"] < 0 and users[user]["rank"] != constant.RANK_NAMES[3]:
                fallen[user] = {
                    "rank": users[user]["rank"],
                    "activityPoint": users[user]["activityPoint"]
                }
                subreddit.contributor.remove(user)

    return fallen


def add_users(reddit):
    news = dict()
    # I think we may use a different randomly adding algorithm.
    for submission in reddit.subreddit("Turkey").hot(limit=constant.ADD_PERR_RECAP):
        for top_level_comment in submission.comments:
            reddit.subreddit(constant.TARGET_SUBREDDIT).contributor.add(top_level_comment.author.name)
            news[top_level_comment.author.name] = {
                "rank": constant.RANK_NAMES[0],
                "activityPoint": 0
            }
            break;
    return news
