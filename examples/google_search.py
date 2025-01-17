"""
    Created by howie.hu at 2021-12-18.
    Description: example
    Changelog: all notable changes to this file will be documented
"""


import pprint
import random
import time
import re

from magic_google import MagicGoogle

################################################
# """
# cd magic_google
# python examples/google_search.py
# """
#################################################

PROXIES = [
    {
        #"http": "http://127.0.0.1:1088",
        "https": "http://127.0.0.1:1088"
    }
]

# Or MagicGoogle()
mg = MagicGoogle(PROXIES)

# The first page of results
# result = mg.search_page(query='python')
# print(result)
#
# time.sleep(random.randint(1, 5))

# Get {'title','url','text'}
def emailre(teststr):
    email = re.compile(r'[a-zA-Z0-9\-\._]+@[0-9a-z\-\.]+')
    emailset = set() #列表
    for em in email.findall(teststr):
        return em



start = 0
for start in range(1, 2):
    for i in mg.search(query="site:Instagram.com  \"dubai\"    \"@gmail.com\"", start=start, num=1, language="en"):
        i["email"] = emailre(i["text"])
        pprint.pprint(i)
        time.sleep(random.randint(5, 30))


# Output
# {'text': 'The official home of the Python Programming Language.',
# 'title': 'Welcome to Python .org',
# 'url': 'https://www.python.org/'}

# Get first page
# for url in mg.search_url(query="python"):
#     pprint.pprint(url)
#
# time.sleep(random.randint(1, 5))

# Output
# 'https://www.python.org/'
# 'https://www.python.org/downloads/'
# 'https://www.python.org/about/gettingstarted/'
# 'https://docs.python.org/2/tutorial/'
# 'https://docs.python.org/'
# 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# 'https://www.codecademy.com/courses/introduction-to-python-6WeG3/0?curriculum_id=4f89dab3d788890003000096'
# 'https://www.codecademy.com/learn/python'
# 'https://developers.google.com/edu/python/'
# 'https://learnpythonthehardway.org/book/'
# 'https://www.continuum.io/downloads'

# Get second page
# for url in mg.search_url(query="python", start=10):
#     pprint.pprint(url)

# Output
# 'https://github.com/python'
# 'https://github.com/python/cpython'
# 'https://www.learnpython.org/'
# 'https://www.raspberrypi.org/documentation/usage/python/'
# 'https://www.reddit.com/r/Python/'
# 'https://www.datacamp.com/courses/intro-to-python-for-data-science'
# 'https://www.coursera.org/learn/python'
# 'https://www.coursera.org/learn/interactive-python-1'
# 'http://abcnews.go.com/US/record-breaking-17-foot-python-captured-south-florida/story?id=51616851'
# 'https://hub.docker.com/_/python/'
