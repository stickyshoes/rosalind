#!/usr/bin/python


f = [line.strip() for line in open('gc_content_data.txt' , 'r').readlines()]

def find_gc_content(strand):
    return (strand.count('C') + strand.count('G')) * 100.0 / (len(strand) * 1.0)

name = ""
content = ""
gc_content_list = []

for line in f:
    if line[0] == '>':
        if name:
            gc_content_list += [(find_gc_content(content), name)]
            content = ""
        name = line[1:]
    else:
        content = content + line

gc_content_list += [(find_gc_content(content), name)]
candidate = sorted(gc_content_list)[-1]

print candidate[1]
print candidate[0]
