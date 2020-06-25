import praw
import time

def login():
    NotLoggedIn = True
    while NotLoggedIn:
        try:
            reddit = praw.Reddit(client_id='A9km-PBOjcEZIQ',
                            client_secret='suoLBrusB7mma4j_44zPaoPQ1mA',
                            user_agent='script:AITAscraper:v1.0.0 (by /u/AcquiredNightIn)')
            print("Logged in")
            NotLoggedIn = False
        except praw.errors.InvalidUserPass:
            print("Wrong username or password")
            exit(1)
        except Exception as err:
            print(str(err))
            time.sleep(5)
    return reddit 