#!/usr/bin/env python3
"""Simple URL tester.

Reads lines in `urlz.txt` as `url [content]` and checks them all.
See sample `urlz.txt` file.

Filename(s) can also be specified on the command line.

The base urllib exception is catched to nicely display errors of type:

* Bad server name,
* 404,
* ...

"""

import sys
from urllib import request
from urllib.error import URLError

def check(filename='urlz.txt'):
    "Check URLs in the given file."
    for line in open(filename).read().split('\n'):
        splitted_line = line.split(' ', 1)
        if len(splitted_line) == 1:
            url, expected_content = splitted_line[0], None
        else:
            url, expected_content = splitted_line
        if not url or url.startswith('#'):
            continue
        print("Testing {}...".format(url))
        if expected_content is not None:
            expected_content = expected_content.lstrip()
            actual_content = request.urlopen(url).read().decode("utf-8").rstrip('\n')
            if actual_content != expected_content:
                tpl = """At {}, expected \n'{}' but got \n'{}'"""
                print(tpl.format(url, expected_content, actual_content))
                break
        else:
            try:
                request.urlopen(url)
            except URLError as e:
                print(e)
                break

if __name__ == '__main__':
    if len(sys.argv) == 1:
        check()
    else:
        for filename in sys.argv[1:]:
            check(filename)
