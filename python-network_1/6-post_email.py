#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response."""
import sys
import requests


if __name__ == "__main__":
    r = requests.post(sys.argv.__getitem__(1), data={"email": sys.argv.__getitem__(2)})
    print(r.text)
