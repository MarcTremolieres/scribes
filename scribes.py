import sys
from math import floor

lignes = sys.stdin.readlines()
N = int(lignes[0])

def cumule(pages, diviseur):
    resultat = [0]
    cumul = pages[0]
    for page in pages[1:]:
        cumul += page
        resultat.append(floor((cumul - 1) / diviseur))
    return resultat

def affiche(pages, scribes):
    resultat = str(pages[0])
    scribe_courant = scribes[0]
    for index in range(1,len(pages)):
        scribe = scribes[index]
        if scribe == scribe_courant:
            resultat += ' ' + str(pages[index])
        else:
            resultat += ' / ' + str(pages[index])
        scribe_courant = scribe
    print(resultat)


for n in range(N):
    index1 = 1 + 2*n
    index2 = 2 + 2*n
    ligne1 = lignes[index1].split(' ')
    ligne2 = lignes[index2].split(' ')
    m = int(ligne1[0])
    k = int(ligne1[1])
    pages = []
    for index in range(m):
        pages.append(int(ligne2[index]))
    somme = sum(pages)
    diviseur = somme / k
    scribes = cumule(pages, diviseur)
    affiche(pages, scribes)
