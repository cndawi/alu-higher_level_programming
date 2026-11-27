#!/usr/bin/python3
"""Fetches https://hbtn.io using requests."""
import requests


if __name__ == "__main__":
    r = requests.get("https://hbtn.io")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
