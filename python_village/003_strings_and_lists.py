#!/usr/bin/python

input_string = raw_input("give the input string: ")

a, b, c, d = raw_input("give me the input indices: ").split(' ')

print input_string[int(a):int(b) + 1], input_string[int(c):int(d) + 1]
