#!/usr/bin/python3
"""This script:
    - takes in a URL and an email
    - sends a POST request to the URL and
    - displays the body of the response (decoded in utf-8)
"""
import sys
import requests

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    value = "" if len(sys.argv) == 1 else sys.argv[1]
    r = requests.post(URL, data={"q": value})

    try:
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get("id"), r_json.get("name")))
    except Exception:
        print("Not a valid JSON")
