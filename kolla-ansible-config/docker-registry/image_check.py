#!/usr/bin/env python3

import requests
import sys

base = "https://hub.docker.com/v2/repositories"

if len(sys.argv) <= 2:
    (u, p) = ("linaro", "debian-source", )
else:
    (u, p) = (sys.argv[1], sys.argv[2], )

def _r(e, s=100):
  return requests.get("{0}/{1}/?page_size={2}".format(base, e, s)).json()['results']


def _latest(user, pattern):
    for image in filter(lambda i: i['name'].startswith(pattern),  _r(user)):
        yield image, sorted(_r("{0}/{1}/tags".format(user, image['name'])), key=lambda i: i['last_updated'])[-1]

def main():
    for i, t in _latest(u, p):
        print("{0} - latest tag:{1} - updated_at: {2}".format(i['name'], t['name'], t['last_updated']))

if __name__ == "__main__":
    main()

