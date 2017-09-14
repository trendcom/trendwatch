#!/usr/bin/python3
from sys import stdin
from itertools import repeat


def merge2(left, right):

    array, lp, rp, write = [0]*(len(left)+len(right)), 0, 0, 0

    try:
        while 1:
            if left[lp][0] > right[rp][0]:
                array[write] = right[rp]
                rp += 1
            else:
                array[write] = left[lp]
                lp += 1
            write += 1
    except:
        elementsleft = len(left) + len(right)-rp-lp
        del array[-elementsleft:]
        array.extend(left[lp:])
        array.extend(right[rp:])

    return array


def merge(decks):

    s = mergesort(decks)

    return ''.join([item[1] for item in s])


def mergesort(decks):
    if len(decks) == 1:
        return decks[0]

    mid = len(decks)//2
    left, right = decks[mid:], decks[:mid]
    left, right = mergesort(left), mergesort(right)
    return merge2(left, right)


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))

if __name__ == "__main__":
    main()