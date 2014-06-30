#!/usr/bin/env python

import sys
import lxml.etree


if __name__ == '__main__':
    try:
        expr = sys.argv[1]
    except IndexError:
        print("Usage: xpath.py <expr>")
        sys.exit(1)

    data = sys.stdin.read()
    xml = lxml.etree.fromstring(data)
    results = xml.xpath(expr, namespaces=xml.nsmap)
    for result in results:
        if isinstance(result, lxml.etree._Element):
            print(lxml.etree.tostring(result, pretty_print=True).encode('utf-8'))

        else:
            print(result.encode('utf-8'))
