#!/usr/bin/python3
"""Takes GitHub credentials and uses the GitHub API to display user id."""
import sys
import requests


if __name__ == "__main__":
    user = sys.argv.__getitem__(1)
    passwd = sys.argv.__getitem__(2)
    r = requests.get("https://github.com", auth=(user, passwd))
    print(r.json().get("id"))
