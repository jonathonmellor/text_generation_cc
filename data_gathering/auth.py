import praw
import time

def login():
    NotLoggedIn = True
    while NotLoggedIn:
        try:
            reddit = praw.Reddit(client_id=#INSERT YOURS HERE,
                            client_secret=#INSERT YOURS HERE,
                            user_agent=#INSERT YOURS HERE)
            print("Logged in")
            NotLoggedIn = False
        except praw.errors.InvalidUserPass:
            print("Wrong username or password")
            exit(1)
        except Exception as err:
            print(str(err))
            time.sleep(5)
    return reddit 
