#!/usr/bin/env python3

"""
Find the "rarest characters" in a comment in the level's source.
"""

import re
import urllib.request
import collections
import operator

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
html = urllib.request.urlopen(url).read().decode()

# Find the "mess" of characters.
pat = re.compile(r'-->\s*<!--(.*?)-->', re.DOTALL)
mess = pat.search(html).groups()[0]

# Make a dict from characters in the mess to their frequencies.
store = collections.defaultdict(int)
for char in mess:
    store[char] = store.get(char, 0) + 1

# Convert the dictionary `store` to a list of (key, value) tuples and sort
# the list by value.
_sorted = sorted(store.items(), key=operator.itemgetter(1))

# There are 8 characters that occur only once, while the rest occur at least
# a thousand times. Print out those 8 characters.

# There are 8 characters that occur only once, while the rest occur at least
# a thousand times. Create a list of those 8 characters.
good_chars = [tup[0] for tup in _sorted if tup[1] == 1]

# The characters lost their order when put in a dictionary, so filter the mess,
# keeping only characters in `good_chars`.
answer = filter(lambda char: char in good_chars, mess)
print(''.join(answer))

