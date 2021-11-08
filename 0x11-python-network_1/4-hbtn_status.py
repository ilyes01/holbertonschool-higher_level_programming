#!/usr/bin/python3
import requests
"""
Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print('Body response:\n\
\t- type: {}\n\
\t- content: {}'.format(type(text), text))#!/usr/bin/python3
import requests
"""
Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    text = r.text
    print('Body response:\n\
\t- type: {}\n\
\t- content: {}'.format(type(text), text))
