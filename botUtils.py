import json
from datetime import date

def readUserList():
    print('readUserList')
    with open('./userList.json') as f:
        userList = json.load(f)
    f.close()
    return userList

def getNewUsers(userList):
    newUserDict = dict()

    with open('./newUser.json') as f:
        newUsers = json.load(f)
    f.close()

    for user in newUsers:
        if user in userList.keys():
            pass
        else:
            newUserDict[user] = {
        		"rank":"new",
        		"dateAdded":"today",
        		"lastActivity":1
        	}
    return newUserDict

def addUsers(newUsers,reddit):
    print('users added')
    # for user in newUsers:
    #     reddit.subreddit('WeCanDoThisToo').contributor.add(user)

def generateFallenList(userList):
    fallenList = dict()

    for key in userList:
        if(userList[key]['rank'] == 'new' and userList[key]['lastActivity']<1):
            fallenList[key] = 0
        if(userList[key]['rank'] == 'senior' and userList[key]['lastActivity']<1):
            fallenList[key] = 0

    return fallenList

def removeFallen(fallenList,reddit):
    print('removed fallen')
    # for user in fallenList:
    #     reddit.subreddit('WeCanDoThisToo').contributor.add(user)

def generateRecapPost(newUsers,fallenList,reddit):

    #TODO find a way to format the body text
    today = date.today()
    title = "Recap: "+str(today)
    body = '#Weekly recap post.\n#Let us welcome our new members\n---------------------\n'
    for user in newUsers:
        body+='##'+"u/"+user+'\n'
    body+='#F in the chat for the fallen\n---------------------\n'
    for user in fallenList:
        body+='##'+"u/"+user+'\n'
    sub = reddit.subreddit('WeCanDoThisToo')
    sub.submit(title,selftext=body)

def updateUsers(userList,newUsers,fallenList):
    for user in fallenList:
        del userList[user]
    for user in newUsers:
        userList[user] = newUsers[user]

    with open('userList.json', 'w') as outfile:
        json.dump(userList, outfile)
    outfile.close()
    return userList

def dailyPostCheck(userList):
    print('dailyPostCheck')
