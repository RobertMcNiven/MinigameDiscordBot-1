import praw
import os
import discord
from requests import Session
from dotenv import load_dotenv

session = Session()
session.verify = "/path/to/certfile.pem"

load_dotenv()
CLIENT_ID = os.getenv('REDDITCLIENTID')
CLIENT_SECRET = os.getenv('REDDITCLIENTSECRET')
USER_AGENT = os.getenv('REDDITUSERAGENT')

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT,
)

async def pullRedditPost(ctx, subredditname: str="okaybuddyretard"):
    subreddit = reddit.subreddit(subredditname)
    submission = subreddit.random()
    await ctx.send(f"Post from r/{subredditname} {submission.url}")
    