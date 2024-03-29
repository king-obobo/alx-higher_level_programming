#!/usr/bin/python3
"""This script:
    -takes in a URL
    - sends a request to the URL and
    - displays the X-Request-Id variable found in the header of the response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
