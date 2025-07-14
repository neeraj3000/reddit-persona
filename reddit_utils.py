import re
import praw
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def extract_username(profile_url):
    match = re.search(r'reddit\.com/user/([^/]+)/?', profile_url)
    return match.group(1) if match else None

def get_user_data(username, limit=50):
    user = reddit.redditor(username)
    posts, comments = [], []
    try:
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "body": submission.selftext,
                "url": f"https://reddit.com{submission.permalink}"
            })

        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "url": f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching data: {e}")
    return posts, comments
