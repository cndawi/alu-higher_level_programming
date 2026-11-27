#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response."""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv.__getitem__(1)
    email = sys.argv.__getitem__(2)
    r = requests.post(url, data={"email": email})
    print(r.text)
