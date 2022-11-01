import praw
from praw.models import MoreComments
import json

env = json.load(open("env.json"))

reddit = praw.Reddit(
    client_id=env["client_id"],
    client_secret=env["client_secret"],
    user_agent=env["user_agent"],
)


def read_reddit(url):
    comments = {
        "url": url,
        "title": "",
        "data": []
    }
    submission = reddit.submission(url=url)
    comments["title"] = submission.title

    for comment in submission.comments:
        content = comment.body
        if len(content) <= 24:
            continue
        if isinstance(comment, MoreComments):
            continue
        comments["data"].append(
            {"body": comment.body, "url": f"https://www.reddit.com{comment.permalink}"})

    return comments
