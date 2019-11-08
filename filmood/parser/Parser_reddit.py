import requests
import praw
import json


"r/TrueFilm ; r/movies"
"стоит обращаться к архивам, а не действующим обсуждениям"
'-----------------------------'
'время действия токена 1 час'
reddit = praw.Reddit(client_id="2OvkRvKd6KbZFg",
                     client_secret="qerkLSKw_sVpnJxnVDDrLcFrsvU",
                     user_agent="comment_reader")

request_data = "joker"

# for submission in reddit.subreddit("TrueFilm").hot(limit = 10):
#     print(f"{submission.title} \n {submission.selftext} \n {20*'-'}")
#
#     comments = submission.comments
#     for comment in comments:
#         print(comment.body)

"""таким образом можно искать обсуждения на сабе труфильм, отбирая что-то, в названии чего есть фильм"""
for submission in reddit.subreddit("TrueFilm").search(request_data):
    print(f"{submission.title} \n {submission.selftext} \n {20*'-'}")
    comments = submission.comments
    for comment in comments:
        print(comment.body)

"""Так делать можно, если принять за аксиому то, что на реддите 100% существуют сабредиты с 
названием фильма"""
for submission in reddit.subreddit(f"{request_data}"):
    print(f"{submission.title} \n {submission.selftext} \n {20*'-'}")
    comments = submission.comments
    for comment in comments:
        print(comment.body)