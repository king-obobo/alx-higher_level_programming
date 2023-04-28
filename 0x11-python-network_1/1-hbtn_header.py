#!/usr/bin/python3
"""This script:
    -takes in a URL
    - sends a request to the URL and
    - displays the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers).get("X-Request-Id"))
