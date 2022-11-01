import praw
import json

env = json.load(open("env.json"))

reddit = praw.Reddit(
    client_id=env["client_id"],
    client_secret=env["client_secret"],
    user_agent=env["user_agent"],
)


def read_reddit(url):
    submission = reddit.submission(url=url)

    for comment in submission.comments:
        print(comment.body)
