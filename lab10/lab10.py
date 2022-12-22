# Zadanie 1
'''
f = open('tekst.txt', 'w')
print('Pierwsza linia', file=f)
print('Druga linia', file=f)
print('Trzecia linia', file=f)
f.close()
'''

# Zadanie 2
'''
f = open('tekst.txt', 'w')
f.write('Pierwsza linia\n')
f.write('Druga linia\n')
f.write('Trzecia linia\n')
f.write('Czwarta linia\n')
f.close()
'''

# Zadanie 3
'''
f = open('tekst.txt', 'w')
num1 = 1
num2 = 1.45
tab = [1,2,3]
f.write(str(num1) + '\n')
f.write(str(num2) + '\n')
f.write(str(tab) + '\n')
f.close()

# lub

f = open('tekst.txt', 'w')
f.write(str(13) + '\n')
f.write('{}\n'.format(2.56))
f.write('%s\n'%(['cos',1,8.98]))
f.close()
'''

# Zadanie 4
'''
f = open('tekst.txt', 'w')
tab = [str(1589), '\n', str(2.654), '\n', str([4,'s',287]), '\n', 'Olaf\n']
f.writelines(tab)
f.close()
'''

# Zadanie 5
'''
f = open('tekst2.txt', 'w')
for i in range(3,20,4):
    print(i, file=f)
f.close()
'''

# Zadanie 6
'''
f = open('tekst2.txt', 'w')
napis = 'Ala ma kota'
for i in napis:
    f.write(i+i+i + '\n')
f.close()
'''

# Zadanie 7
'''
f = open('tekst.txt', 'r')
dane = f.read()
print(dane)
f.close()
'''

# Zadanie 8
'''
f = open('linie.txt', 'r')
dane = f.read(50)
print(dane)
f.close()
'''

# Zadanie 9
'''
f = open('linie.txt', 'r')
dane = f.read(40)
print(dane)

f.seek(0)
dane = f.readlines()
print(*dane)

f.close()
'''

# Zadanie 10
'''
f = open('linie.txt', 'r')
for line in f:
    print(line, end='')
f.close()
'''

# Zadanie 11
'''
f = open('tekst.txt', 'r')
dane = f.readline()
dane = dane.strip()

while dane:
    print(dane, f.tell())
    dane = f.readline()
    dane = dane.strip()

f.close()
'''

# Zadanie 12
'''
n = int(input("Podaj liczbę: "))
f = open('tekst.txt', 'r')

for i in range(n):
    dane = f.readline()
    dane = dane.strip()
    print(dane)

f.close()
'''

# Zadanie 13
'''
f = open('tekst2.txt', 'r+')
f.seek(0,2)
f.write('\ndowolny tekst')
f.seek(0)
dane = f.read()
print(dane)
f.close()
'''

# Zadanie 14
'''
f = open('tekst.txt', 'r')
dane = f.readlines()
f.close()

n = int(input("Podaj liczbę: "))
print(*dane[-n:], sep='')
'''

# Zadanie 15
'''
f = open('tekst.txt', 'r')
tab = []
for line in f:
    tab.append(line)
print(tab)
f.close()
'''

# Zadanie 16
'''
f = open('tekst.txt')
tmp = 0
for line in f:
    mL = len(line)
    if mL > tmp:
        tmp = mL
        maxLine = line
f.close()
print(maxLine, tmp)
'''

# Zadanie 17
'''
f = open('tekst.txt')
counter = 0
for line in f:
    counter += 1
f.close()
print(counter)
'''

# Zadanie 18
'''
f1 = open('tekst.txt', 'r')
dane = f1.read()
f1.close()

f2 = open('tekst2.txt', 'a')
f2.write(dane)
f2.close()


# lub inaczej

f1 = open('tekst.txt')
f2 = open('tekst2.txt', 'a')

for line in f1:
    f2.write(line)
    
f1.close()
f2.close()
'''

# Zadanie 19
'''
f = open('tekst2.txt')
tab = f.readlines()
f.close()

dl = len(tab)
from random import randint
k = randint(0,dl-1)

print(tab[k])
'''

# Zadanie 20
'''
def ile_s(file):
    counter = 0
    f = open(file)
    for line in f:
        line = line.split()
        counter += len(line)
    f.close()
    return counter

print(ile_s('tekst.txt'))
print(ile_s('tekst2.txt'))
'''

# Zadanie 21
'''
def wypisz_slowa(file):
    f = open(file)
    for line in f:
        line = line.split()
        for word in line:
            if len(word) <= 4:
                print(word)
    f.close()

print(wypisz_slowa('tekst.txt'))
print(wypisz_slowa('tekst2.txt'))
'''

# Zadanie 22
'''
def ile_s(file):
    counter = 0
    f = open(file)
    for line in f:
        line = line.split()
        for word in line:
            if word[-1] == 'a':
                counter += 1
    f.close()
    return counter

print(ile_s('tekst.txt'))
print(ile_s('tekst2.txt'))
'''

# Zadanie 23
'''
def dopisz_znak(file, mark):
    f = open(file)
    for line in f:
        for m in line:
            print(m+mark, end='')
    f.close()

dopisz_znak('tekst.txt', '#')
dopisz_znak('tekst2.txt', '$')
'''

# Zadanie 24
'''
def zamien(file, m1, m2):
    f = open(file)
    for line in f:
        for m in line:
            if m==m1: print(m2, end='')
            else: print(m, end='')
    f.close()

zamien('tekst.txt', 'n', '*')
zamien('tekst2.txt', 'a', '++')
'''