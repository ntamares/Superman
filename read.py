import praw

reddit = praw.Reddit('superman', user_agent="Grammar Police")

subreddit = reddit.subreddit('bot_sandbox_testing')

for submission in subreddit.hot(limit=25):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
time.sleep(2)