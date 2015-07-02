#!/usr/bin/env python

def is_palindrome(num):
    num_string = str(num)
    reversed_num_string = num_string[-1::-1]
    return num_string[:len(num_string)/2] == reversed_num_string[:len(reversed_num_string)/2]

def process(num):
    return num + int(str(num)[-1::-1])

def find_palindrome(num, max_steps=10000):
    steps = 0
    while not is_palindrome(num):
        num = process(num)
        steps += 1
        if steps >= max_steps:
            break
    if is_palindrome(num):
        return (num, steps)
    else:
        return (None, steps)


