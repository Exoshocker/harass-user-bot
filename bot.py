import praw
from time import sleep

reddit = praw.Reddit(client_id='TQbgDnQypTZ25g',
               client_secret='7-ZfYPyzgwzRC0AKzG6AszhkFYA',
               password='bearcat001',
               username='hatesBillthedwarf',
               user_agent='Dont Care')
print("success")

cache = []

for i in range(0,10):
    subreddit = reddit.subreddit('all')
    comment = subreddit.comments(limit = 20)
    for comment in reddit.redditor('billthedwarf').comments.new(limit=None):
        if (comment.id not in cache):
            comment.reply("I hate you u/billthedwarf")
            cache.append(comment.id)
            print('F')

    sleep(10)
