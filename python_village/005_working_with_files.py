#!/usr/bin/python

f = open('sample-rosalind_test','r')
lines = f.readlines()
for line in [lines[i] for i in range(1, len(lines), 2)]:
    print line,
