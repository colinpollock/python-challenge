#!/usr/bin/env python3

"""
Use urllib to repeatedly scrape a page and use information on that page to find
the next page.

The answer for this level is 'peak.html'.
"""

import re
import urllib.request


def get_html(url):
    """Return HTML at `url`."""
    return urllib.request.urlopen(url).read().decode()


def find_nothing(url):
    """Find the "nothing" on the page at `url`'s source."""
    html = get_html(url)

    # The first group of nothings (numbers) match this pattern.
    main_pat = re.compile(r'and the next nothing is (\d+)')
    match = main_pat.search(html)
    if match:
        return match.groups()[0]

    # That pattern eventually doesn't match. Instead of another nothing we
    # are told the next nothing is half the previous one.
    div_pat = re.compile(r'Yes. Divide by two and keep going.')
    match = div_pat.match(html)
    if match:
        old_nothing = re.search(r'.*?nothing=(\d+)', url).groups()[0]
        return str(int(old_nothing) / 2)

    # If the previous patterns don't match, return None for failure.
    else:
        return None


def main():
    """Follow the "nothings" until the answer is found."""
    base_url = ('http://www.pythonchallenge.com/pc/def/linkedlist.php'
               '?nothing=%s')
    url = base_url % '12345'

    # Loop until find_nothing fails, at which point print the HTML.
    while True:
        nothing = find_nothing(url)
        if not nothing:
            print(get_html(url))
            return
        url = base_url % nothing
        

if __name__ == '__main__':
    main()
