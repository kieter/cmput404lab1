#!/usr/bin/env python

import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.headers)

this_file = requests.get("https://raw.githubusercontent.com/kieter/cmput401lab1/master/main.py")
print(this_file.text)