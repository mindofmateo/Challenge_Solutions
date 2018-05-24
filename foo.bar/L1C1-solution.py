#!/bin/python3

'''---------------------------------------------------------------|
| Date: 20180520                                                  |
| URL:                                                            |
| https://foobar.withgoogle.com/                                  |
| Summary:                                                        |
| From an "infinite list" of prime numbers, find the nth to n+5th |
| digits.  Constraints: 0 <= n <= 10000                           |
|---------------------------------------------------------------'''

from math import sqrt

def answer(n):
    if n < 0 or n > 10000:
        print 'EDOM: input is not in domain'
        return ""
    prime_string = "2"
    prime_list = [2]

    for i in xrange(3, 21500, 2):
        root = sqrt(i) + 1
        for j in prime_list:
            if (i % j == 0):
                break
            elif (j == prime_list[-1]) or (j > root):
                prime_string += str(i)
                prime_list.append(i)
                break
        if (len(prime_string) >= n + 5):
            break
    return prime_string[n: n + 5]

if __name__ == '__main__':
    print answer(int(input('Enter an index: ')))

