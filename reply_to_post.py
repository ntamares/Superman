import praw
import pdb
import re
import os


reddit = praw.Reddit('superman', user_agent="Grammar Police")

# create empty list if this hasn't been run before
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# otherwise, load posts that have been replied to previously
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('bot_sandbox_testing')
for submission in subreddit.hot(limit=25):
    if submission.id not in posts_replied_to:
        if re.search("he does good", submission.title, re.IGNORECASE):
            submission.reply("Superman does good. He did well.")
            print("replying to: ", submission.title)

            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")


