from botUtils import *
import praw
def runBotScript():
    run = True
    # count number of days
    recapCount = 1

    reddit = praw.Reddit(
            client_id='**********',
            client_secret='**********',
            username='**********',
            password='**********!',
            user_agent='**********'
    )

    while run:

        currentUserList = readUserList()


        dailyPostCheck(currentUserList)



        # once weekly run this
        if( recapCount == 7):
            # find new users and add them to the list and
            newUsers = getNewUsers(currentUserList)

            #approveNewUsers
            addUsers(newUsers,reddit)

            # find existing members and remove them for inactivity
            fallenList = generateFallenList(currentUserList)

            #remove fallenUsers from approval list
            removeFallen(fallenList,reddit)

            # generate recap post with new members and fallen
            generateRecapPost(newUsers, fallenList,reddit)

            #update the userList and save
            updateUsers(currentUserList,newUsers,fallenList)


            count = 0
            run = False
        # increment day count by
        recapCount+=1

        # TODO: add sleep function for 24 hrs




if __name__ == '__main__':
    runBotScript()
