import praw
import time


GRAMMAR_CORRECTION_HE = "Superman does good. He did well."


def main():
    reddit = authenticate()
    #while True:
     #   run_bot(reddit)
    run_bot(reddit)

def run_bot(reddit):
    subreddit = reddit.subreddit('bot_sandbox_testing')
    for comment in reddit.subreddit.stream.comments():
    if "he did good" in comment.body:
        comment.reply(GRAMMAR_CORRECTION_HE)
    time.sleep(2)

def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('superman', user_agent="Grammar Police")
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit

if __name__ == '__main__':
    main()
