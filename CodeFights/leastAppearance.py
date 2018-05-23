#!/bin/python3

'''---------------------------------------------------
| URL:                                               |
| https://codefights.com/challenge/vvaEwn4NbpLYGMt5G |
|                                                    |
| Summary:                                           |
| Append to a new array one integer from each pair   |
| in the input list that is currently least frequent |
| in the new array.                                  |
---------------------------------------------------'''

# imports:

def leastAppearance(choices):
    counts = dict([x, 0] for x in range(1, 101))
    selection = []
    for pair in choices:
        if counts[pair[0]] == counts[pair[1]]:
            selection.append(pair[0])
            counts[pair[0]] += 1
        else:
            least = pair[0] if (counts[pair[0]] < counts[pair[1]]) else pair[1]
            selection.append(least)
            counts[least] += 1
    return selection

if __name__ == '__main__':
    # The function takes in a 2D array/list of sorted integer pairs.
    # Example: [[1, 2], [3, 4], [1, 2]]
    leastAppearance(input())


