#!/usr/bin/python
from sys import argv
from json import dumps

if len(argv) == 1:
    print("Please provide a filename")
    exit()

l = []
f = open(argv[1])
for line in f:
    y = line.replace('\n', '').replace('\r', '').split('\t')
    l.append(dumps(y[1::], separators=(',', ':'), ensure_ascii=False))

print('[%s]' % ','.join(l))

