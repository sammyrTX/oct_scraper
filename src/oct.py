#!/usr/local/bin/python3

# pip install beautifulsoup4
from bs4 import BeautifulSoup

# pip install requests
import requests


def main():
    r = requests.get('https://ocw.mit.edu/courses/audio-video-courses/')
    print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')


if __name__ == "__main__":
    main()