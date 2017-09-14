#!/usr/bin/python3

from sys import stdin
from itertools import repeat

def bruteSort(liste):
    for i in range(0, len(liste)-1):
        for p in range( i+1, len(liste)):

            if (liste[i][0] > liste[p][0]):
                inter = liste[i]
                liste[i] = liste[p]
                liste[p] = inter
    return liste
def merge(decks):
    mergedDeck = []
    for deck in decks:
        for tuppel in deck:
            mergedDeck.append(tuppel)
    sortedDeck = bruteSort(mergedDeck)
    sortedDeck = mergeSort(mergedDeck)
    returnString = ""
    for tuppel in sortedDeck:
        returnString = returnString + tuppel[1]
    return returnString



def mergeSort(liste):
    if len(liste) == 0:
        return liste
    elif len(liste) == 1:
        return liste
    else:
        if len(liste) % 2 != 0:
            indexSplit = (len(liste) - 1) / 2
        else:
            indexSplit = len(liste) / 2
        liste1 = mergeSort(liste[0:indexSplit])
        liste2 = mergeSort(liste[indexSplit:])
        returnList = []
        p = 0
        q = 0
        o = 0
        while len(returnList) != len(liste1) + len(liste2):
            if p >= len(liste1):
                for x in range(q, len(liste2)):
                    returnList.append(liste2[x])
            elif q >= len(liste2):
                for x in range(p, len(liste1)):
                    returnList.append(liste1[x])
            else:
                if liste1[p][0] >= liste2[q][0]:
                    returnList.append(liste2[q])
                    q = q + 1
                else:
                    returnList.append(liste1[p])
                    p = p + 1
        return returnList


        # SKRIV DIN KODE HER


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


#if __name__ == "__main__":
   # main()
dock = []
dick = [[(-1, 'h'), (3, 'h'), (7, 'h'), (2, 'u')], [(5, 'u')], [(8, 'u'), (3, 'e')], [(6, 'e')], [(9, 'e')]]
deck = [[(3,'i'),(5,'i'),(8,'i')], [(2,'n')], [(4,'t'),(7,'t')], [(6,'a')], [(9,'v')]]
print(merge(dick))