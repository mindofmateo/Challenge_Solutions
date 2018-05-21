from math import sqrt



def answer(n):
    # your code here
    if n < 0 or n > 10000:
        return
    prime_string = "2"
    prime_list = [2]
    next_int = 11
    length = len(prime_string)
    i = 2
    # while (len(prime_string) < n + 4):
    for i in xrange(3, 21500):
        root = sqrt(i) + 1
        for j in prime_list: #xrange(2, i):
            if (i % j == 0) or (j > root):
                break
            elif j == prime_list[-1] or i == j:
                prime_string += str(i)
                prime_list.append(i)
                break
        # i += 1
    return prime_string[n: n + 5]

if __name__ == '__main__':
    print answer(int(input('Enter an index: ')))



'''

from math import sqrt



def answer(n):

    # your code here

    if n < 0 or n > 10000:

        return

    prime_string = ""

    prime_list = set([2])

    next_int = 11

    length = len(prime_string)

    i = 2

    # while (len(prime_string) < n + 4):

    for i in xrange(2, 20000):

        for j in prime_list: #xrange(2, i):

            if i == j:

                prime_string += str(j)

                prime_list.add(i)

                print prime_string

            if i % j == 0:

                break

        # i += 1

    return prime_string[n:]

    

    # ' ' '

    while (n < length + 4):

        isPrime = True

        root = sqrt(n)

        gen = (x for x in prime_list if x < root)

        for prime in gen:

            if next_int % prime == 0:

                isPrime = False

                break

        if isPrime:

            prime_list.append(next_int)

            prime_string += str(next_int)

            length += len(str(next_int))

        next_int += 2

    return prime_string[n:] # ' ' '

if __name__ == '__main__':

    print answer(int(input('Enter an index: ')))

'''
