#!/usr/bin/python3
"""This script:
    - takes in a URL and an email
    - sends a POST request to the URL and
    - displays the body of the response (decoded in utf-8)
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    r = requests.post(url, data=values)
    print(r.text)
