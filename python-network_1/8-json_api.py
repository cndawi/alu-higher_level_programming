#!/usr/bin/python3
"""Sends a POST request to search_user with a letter parameter."""
import sys
import requests


if __name__ == "__main__":
    q = sys.argv.__getitem__(1) if len(sys.argv) > 1 else ""
    r = requests.post("http://0.0.0", data={"q": q})
    try:
        json_res = r.json()
        if json_res:
            print("[{}] {}".format(json_res.get("id"), json_res.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
