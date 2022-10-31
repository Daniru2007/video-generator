import praw
import json

env = json.load(open("env.json"))

reddit = praw.Reddit(
    client_id=env["client_id"],
    client_secret=env["client_secret"],
    user_agent=env["user_agent"],
)


submission = reddit.submission(
    url="https://www.reddit.com/r/Kerala/comments/w1jr2j/nris_what_are_some_funny_questionsassumptions_you/")

for comment in submission.comments:
    print(comment.body)
