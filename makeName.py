#!/usr/bin/python
from sys import argv
from json import dumps


l = []
pre = argv[1]
for line in open(argv[2]):
    y = line.replace('\n', '').replace('\r', '').split('\t')
    l.append(dumps(y[1::], separators=(',', ':'), ensure_ascii=False))

print('%s[%s]%s' % (pre, ','.join(l), ';' if len(pre) else ''))

