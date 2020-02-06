#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """This function returns the top ten topics of subreddit"""
    subs = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                        .format(subreddit),
                        headers={'User-agent': 'AlafreshBot'})
    if subs.status_code == 404:
        print(None)
        return
    subs = subs.json()
    for i in subs.get('data')['children']:
        for j in i.get('data'):
            if j == 'title':
                print(i.get('data')[j])
