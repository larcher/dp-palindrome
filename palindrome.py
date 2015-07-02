#!/usr/bin/env python

def is_palindrome(num):
    # Tried a few variations on checking ... 
    # very subtle differences in speed, at least in checking 1 to 1000 

    # ... with this code:
    #num_string = str(num)
    #reversed_num_string = num_string[::-1]
    #return num_string[:len(num_string)/2] == reversed_num_string[:len(reversed_num_string)/2]
    # ... time ./palindrome.py says this:
    #./palindrome.py  55.32s user 0.00s system 86% cpu 1:04.23 total

    # ... with this code:
    num_string = str(num)
    return num_string == num_string[::-1]
    # ... time says: 
    # ./palindrome.py  55.20s user 0.02s system 85% cpu 1:04.21 total

    # ... with this code:
    # return num == int(str(num)[::-1])
    # ... time says:
    # ./palindrome.py  61.90s user 0.01s system 80% cpu 1:16.72 total
    # ./palindrome.py  61.86s user 0.04s system 80% cpu 1:16.62 total


def process(num):
    return num + int(str(num)[::-1])

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


lychrel = []
palindromes = []

for num in xrange(1, 1000):
    (pal, steps) = find_palindrome(num)
    if pal:
        print "%d gets palindromic after %d steps: %d" % (num, steps, pal)
        palindromes += [pal]
    else:
        print "%d may be a Lychrel number - not palindromic after %d steps" % (num, steps)
        lychrel += [num]

print "Found %d total possible Lychrel numbers:" % (len(lychrel))
print lychrel
