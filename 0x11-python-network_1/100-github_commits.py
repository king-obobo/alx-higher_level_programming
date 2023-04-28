#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest) of the repository
"""
import requests
import sys

if __name__ == "__main__":
    URL = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    r = requests.get(URL)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
