import praw
import re


GRAMMAR_CORRECTION_HE = "Superman does good. He did well."
#SHE
#I
#YOU
#THEY


def main():
    reddit = authenticate()
    # while True:
    #   run_bot(reddit)
    run_bot(reddit)


def run_bot(reddit):
    print("running bot")
    subreddit = reddit.subreddit('bot_sandbox_testing')
    for comment in subreddit.stream.comments():
        print(comment.body)
        #if "he did good" in comment.body:
        #   comment.reply(GRAMMAR_CORRECTION_HE)
        if re.search("he does good", comment.body, re.IGNORECASE):
            comment.reply(GRAMMAR_CORRECTION_HE)


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('superman', user_agent="Grammar Police")
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit

if __name__ == '__main__':
    main()
