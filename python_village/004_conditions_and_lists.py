#!/usr/bin/python
def sum_of_odd_numbers_between(a, b):
    list = []
    for i in range(a, b):
        if i % 2 == 1 :
            list.append(i)
    return sum(list)

a = int(raw_input("Give me input a: "))
b = int(raw_input("Give me input b: "))
print sum_of_odd_numbers_between(a, b + 1)
