import praw
from time import sleep

reddit = praw.Reddit(client_id='id',
               client_secret='secret',
               password='password',
               username='username',
               user_agent='agent')
print("success")

cache = []

for i in range(0,10):
    subreddit = reddit.subreddit('all')
    comment = subreddit.comments(limit = 20)
    for comment in reddit.redditor('user').comments.new(limit=None):
        if (comment.id not in cache):
            comment.reply("text")
            cache.append(comment.id)
            print('whatever')

    sleep(10)
