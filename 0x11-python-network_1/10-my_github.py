#!/usr/bin/python3
"""This script takes in your:
    - GitHub credentials (username and password) and
    - uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    URL = "https://api.github.com/user"
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get(URL, auth=auth)
    print(r.json().get("id"))
