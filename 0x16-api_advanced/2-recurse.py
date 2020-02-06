#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], count=300, after=''):
    """This function returns a list containing
    the titles of all hot articles for a given subreddit"""
    subs = requests.get('https://www.reddit.com/r/{}/hot.json'
                        .format(subreddit),
                        headers={'User-agent': 'AlafreshBot'},
                        params={"limit": count, "after": after})
    if after is None:
        return hot_list
    if subs.status_code == 404:
        return None
    subs = subs.json()
    for i in subs.get('data')['children']:
        hot_list.append(i['data']['title'])
    after = subs.get('data')['after']
    return recurse(subreddit, hot_list, count, after)
