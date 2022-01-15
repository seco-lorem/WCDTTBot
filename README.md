# WCDTTBot
Bot for an experimental private subreddit that we use to weekly:\
Adds random users,\
Adjusts users' ranks & flairs\
Kicks inactive users depending on their ranks,\
Posts a recap about it.\
Project with internet friends. We know that this is done before, we just wanted to make one our own.
## To Use
### Set up
In your preferred directory, run the commands below:
```
git clone https://github.com/seco-lorem/WCDTTBot
cd WCDTTBot

echo: >> constant.py & echo # Override the Target Subreddit >> constant.py
echo TARGET_SUBREDDIT = "ENTER PRIVATE SUBREDDIT NAME HERE" >> constant.py
echo CLIENT_ID       = "ENTER CLIENT ID HERE" > credentials.py
echo CLIENT_SECRET   = "ENTER CLIENT SECRET HERE" >> credentials.py
echo USER_AGENT      = "This is not needed" >> credentials.py
echo USERNAME        = "ENTER BOT ACCOUNT NAME HERE" >> credentials.py
echo PASSWORD        = "ENTER BOT ACCOUNT PASSWORD HERE" >> credentials.py

```
You can edit constant.py and credentials.py according to the comments written.\
Getting a client ID & secret for a bot account is expained in the first 4 minutes in this tutorial:\
https://youtu.be/NRgfgtzIhBQ
### Run
Every once in a while (weekly recommended) run using your own python runner command
```
py main.py
```
