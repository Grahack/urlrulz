#!/usr/bin/env python
"""Simple URL tester.

Reads lines in `urlz.txt` as `url [content]` and checks them all.
See sample `urlz.txt` file.

Some errors are not nicely presented to the user (stacktrace instead):

* Bad server name,
* 404,
* ...

"""

import urllib2

def check(filename='urlz.txt'):
    "Check URLs in the given file."
    for line in open(filename).read().split('\n'):
        splitted_line = line.split(' ', 1)
        if len(splitted_line) == 1:
            url, expected_content = 2*splitted_line
        else:
            url, expected_content = splitted_line
        if not url or url.startswith('#'):
            continue
        actual_content = urllib2.urlopen(url).read()
        stripped_content = actual_content.rstrip('\n')
        if stripped_content != expected_content:
            tpl = """At {}, expected \n'{}' but got \n'{}'"""
            exit(tpl.format(url, expected_content, stripped_content))

if __name__ == '__main__':
    check()
