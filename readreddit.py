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
    print("reading comments")
    comments = {
        "url": url,
        "title": "",
        "data": [],
        "id": ""
    }
    submission = reddit.submission(url=url)
    comments["title"] = submission.title
    comments["id"] = f"#t3_{submission.id}"
    comments["len"] = len(submission.title)/10.5

    for comment in submission.comments:
        content = comment.body
        if len(content) <= 24:
            continue
        if isinstance(comment, MoreComments):
            continue
        comments["data"].append(
            {"body": comment.body, "url": f"https://www.reddit.com{comment.permalink}", "id": f"#t1_{comment.id}", "len": len(comment.body)/10.5})

    return comments
