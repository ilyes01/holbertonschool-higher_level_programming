#!/usr/bin/python3
"""Python script that takes in a URL, sends
a request to the URL and displays the value """

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
