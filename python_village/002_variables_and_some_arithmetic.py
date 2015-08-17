#!/usr/bin/python 

def sum_of_squares(a, b):
    print a ** 2 + b ** 2

a = raw_input("give me a: ")
b = raw_input("give me b: ")

sum_of_squares(int(a), int(b))
