# kopia tablicy np
'''
tab=[1,['a','b']]
ntab=tab[:]
print(tab) # [1, ['a', 'b']]
print(ntab) # [1, ['a', 'b']]
ntab = tab.copy()
tab[0] = 'olaf'
tab[1][0] = 'c'
print(tab) # ['olaf', ['c', 'b']]
print(ntab) # [1, ['a', 'b']]
'''
#tab = {'imie':'olaf', 'wiek':8}

# Zadanie 1
'''
# sposób 1
suma = 0
dane = input("Podaj liczby odzielone spacją: ").split()
for i in dane:
    suma += int(i)

print(suma)

# sposób 2
dane = [int(i) for i in input("Podaj liczby odzielone spacją: ").split()]
print(sum(dane))
'''

# Zadanie 2
'''
dane = input("Podaj liczby odzielone spacją: ").split()
dane.reverse()
print(*dane, end=' ')
'''

# Zadanie 3
'''
# sposób 1 
dane = input("Podaj liczby odzielone spacją: ").split()
dane = dane[1::2] # zaczyna od indeksu 1, krok (:) co 2
#print(dane)
dane.reverse()
for i in dane:
    print(i, end=' ')

# sposób 2 
dane = input("Podaj liczby odzielone spacją: ").split()
print(*dane[1::2][::-1])
'''

# Zadanie 4
'''
dane = input("Podaj liczby odzielone spacją: ").split()
dane.reverse()
print(*dane[0::3])
#print(*dane[0::3], end=' ')
'''

# Zadanie 5
'''
dane = input("Podaj napis: ")
dane = dane[::-1]
print(dane)
'''

# Zadanie 6
'''
# sposób 1
dane = input("Podaj liczby odzielone spacją: ").split()
dane.reverse()
for i in dane:
    if i.isupper():
        print(i, end=' ')
print()

# sposób 2
print(*[i for i in input().split()[::-1] if i.isupper()])
'''

# Zadanie 7
'''
def ile_cyfr(tab):
    slownik = dict.fromkeys(range(10),0)
    for i in tab:
        slownik[i] += 1
    return slownik

lista = [1,5,4,6,8,9,0,7,8,6,5,4,5,6,1,2,3,2,1,4,8,7,6,0]
print(ile_cyfr(lista))
'''

# Zadanie 8
'''
from random import randint

def moneta(n):
    slownik = {'o':0, 'r':0}
    for i in range(n):
        rz = randint(0,1)
        if rz==0:
            slownik['o'] += 1
        else:
            slownik['r'] += 1
    return slownik

print(moneta(20))
print(moneta(50))
print(moneta(100))
print(moneta(500))
print(moneta(1000))
'''

# Zadanie 9
'''
from random import randint

def kostki(n):
    slownik = dict.fromkeys(range(2,13), 0)
    for i in range(n):
        k1 = randint(1,6)
        k2 = randint(1,6)
        suma = k2 + k1
        slownik[suma] += 1
    return slownik

print(kostki(100))
print(kostki(1000))
print(kostki(10000))
print(kostki(100000))
print(kostki(1000000))
'''

# Zadanie 10
'''
s1 = input("Podaj pierwszy wyraz: ")
s2 = input("Podaj drugi wyraz: ")

s1 = set(s1)
#print(f"Zbiór s1: {s1}")
s2 = set(s2)
#print("Zbiór s2: ", s2)

result = s1.intersection(s2) # The intersection() method returns a set that contains the similarity between two or more sets.
print(result)
print(*result)

#litery występujące jednocześnie w dwóch słowach
iloczyn = s1 & s2
print(iloczyn) # {'A', 'K', 'R'}
print(*iloczyn) # A K R
'''

# Zadanie 11
'''
def ile(s):
    slownik = {'A':0, 'C':0, 'G':0, 'T':0}
    for z in s:
        if z in slownik:
            slownik[z] += 1
    return slownik

print(ile("AABCGCGTGTTT"))
'''

# Zadanie 12
'''
def oduz(s):
    slownik = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    s = s[::-1]
    nowys = ''
    for z in s:
        if z in slownik:
            nowys += slownik[z]
        else:
            nowys += z
    return nowys

print(oduz("AABCGCGTGTTT"))
'''

# Zadanie 13
'''
slownik = dict.fromkeys('abcdefghijklmnopqrstuvwxyz',0)

tekst = input().lower()
for z in tekst:
    if z in slownik:
        slownik[z] += 1

print(slownik)
'''

# Zadanie 14
'''
tab = []
slowo = input()
while slowo != '***':
    tab.append(slowo)
    slowo = input().strip()

zbior = set(tab)
tab = sorted(zbior)
print(*tab)
'''

# Zadanie 15
'''
n = int(input())
slownik = {}
for i in range(n):
    wo, fp = input().split()
    slownik[wo] = fp

zdanie = input().split()
for s in zdanie:
    print(slownik.get(s,s), end= ' ')
'''

# Zadanie 16
'''
def litery(s):
    s = s.lower()
    s = s.replace(' ','')
    s = set(s)
    s = sorted(s)
    return s

print(litery('Ala ma kota a Sierotka ma Rysia'))
'''

# Zadanie 17
'''
x, y = input().split()
x = int(x)
y = int(y)
dane = [int(z) for z in input().split()]

wynik = 0
for z in dane:
    if z<x:
        wynik += x-z
    elif z>y:
        wynik += y-z
    else:
        wynik = 0
        
print(wynik)
'''

# Zadanie 18
'''
M = int(input())
glosy = [int(x) for x in input().split()]

slownik = dict.fromkeys(range(1,M+1), 0)
for x in glosy:
    slownik[x] += 1

wygrany = 1
for k in slownik:
    print(f"{k}: {slownik[k]}")
    if slownik[wygrany] < slownik[k]:
        wygrany = k

print(wygrany)
'''