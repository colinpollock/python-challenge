#!/usr/bin/env python3

"""
Use re to find "One small letter, surrounded by EXACTLY three big bodyguards on
each of its sides" within in a comment in the page's source.
"""

import re
import urllib.request

# Download the page's source. Put the comment containing the answer in `mess`.
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
html = urllib.request.urlopen(url).read().decode()
pat = re.compile(r'</html>\s*<!--(.*?)-->', re.DOTALL)
mess = pat.search(html).groups()[0]

# Find all occurrences of exactly 3 capitals on either side of a lowercase.
pat = re.compile(r"""[^A-Z]   # Not a capital (so that we don't get [A=Z]{4}
                     [A-Z]{3} # 3 capital letters
                     ([a-z])  # The lowercase letter we want
                     [A-Z]{3} # 3 more capital letters
                     [^A-Z]   # Another non-capital
                     """, re.VERBOSE)

found = pat.findall(mess)
print(''.join(found))

