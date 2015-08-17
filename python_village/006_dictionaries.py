#!/usr/bin/python

with open("long_line.txt") as f:
    data = f.read()
    our_dict = {}
    for word in data.strip().split(' '):
        our_dict[word] = our_dict.get(word, 0) + 1

    for key, value in our_dict.iteritems():
        print key, value
