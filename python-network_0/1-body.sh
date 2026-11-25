#!/bin/bash
# Sends a GET request to a URL and displays the body of a 200 status code response
curl -sL "$1" -w "%{http_code}" -o /tmp/body.tmp | grep -q "200" && cat /tmp/body.tmp
