#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """This function returns the number of subs"""
    subs = requests.get('https://www.reddit.com/r/{}/about.json'
                        .format(subreddit),
                        headers={'User-agent': 'AlafreshBot'})
    if subs.status_code == 404:
        return 0
    subs = subs.json()
    for i in subs.get('data'):
        if i == 'subscribers':
            return subs.get('data')[i]
