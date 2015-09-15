#!/usr/bin/python


f = open('sample_text.txt' , 'r').readlines()
total = len(f)

content = ''

for word in f:
    if word[0] == '>':
        content = word[1:].rstrip()

print content

#c = f.count("C")
#g = f.count("G")

#print c

#gc_total = g+c
#gc_content  = gc_total/ float(total)

#print gc_content


