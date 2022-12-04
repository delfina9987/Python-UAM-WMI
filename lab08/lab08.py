#text = 'abcdefgh'
#print(text[0::2]) # nieparzyste
#print(text[1::2]) # parzyste

# Zadanie 1
'''
def szyfr(s):
    s = s.lower() # małe litery
    d = len(s) # długość łańcucha
    new = ''
    for i in range(1,d,2): # w pętli co 2
        new += s[i]
        new += s[i-1]
    if d%2 == 1:
        new += s[-1]
    return new

#print(szyfr('abcdef'))
#print(szyfr('abcdefg'))
#print(szyfr('hUlaEnma'))
dane = input("Podaj łańcuch znaków: ")
print(szyfr(dane))
'''

# Zadanie 2
'''
def parkan(s):
    s = s.lower().replace(' ','')
    new = s[0::2] + s[1::2]
    return new

#print(parkan('ab cd EFG h'))
#print(parkan('ab Cde f'))
#print(parkan('A bc deF g'))
dane = input("Podaj łańcuch znaków: ")
print(parkan(dane))
'''

# Zadanie 3
'''
def czy_palindrom(s):
    s = s.lower()
    return s[::-1] == s # porównanie odwróconego wyrazu od orginalnego 

#print(czy_palindrom('sos'))
#print(czy_palindrom('aNna'))
#print(czy_palindrom('nie'))
dane = input("Podaj palindrom: ")
print(czy_palindrom(dane))
'''

# Zadanie 4
'''
def czy_palindrom2(s):
    s = s.replace(' ','').lower()
    return s[::-1] == s # porównanie odwróconego wyrazu od orginalnego 

print(czy_palindrom2('Kobyła ma mały bok'))
print(czy_palindrom2('nie kotek'))
print(czy_palindrom2('Ile Roman ładny dyndał na moreli'))
'''

# Zadanie 5
'''
def ukryj(s):
    from random import randint
    nowy = ''
    for znak in s[:-1]:
        z = randint(ord('a'), ord('z'))
        z = chr(z)
        nowy += znak
        nowy += z
    nowy += s[-1]
    return nowy

print(ukryj('Olaf'))
print(ukryj('Elsa'))
print(ukryj('Anna'))
'''

# Zadanie 6
'''
def anagram(s):
    s = s.lower()
    s = sorted(s)
    new = ''.join(s)
    return new

print(anagram('wuYqNoaGQb'))
print(anagram('kinder'))
'''

# Zadanie 7
'''
def anagramy(s,t):
    s = s.lower().replace(' ','')
    t = t.lower().replace(' ','')
    ss = sorted(s)
    tt = sorted(t)
    return ss == tt

print(anagramy('kinder','deiknr'))
print(anagramy('deiknr','kinder'))
print(anagramy('bguj','bdkah'))
'''

# Zadanie 8
'''
def rot(s):
    d = (ord('A') + ord('Z'))/2
    new = ''
    for i in s:
        code = ord(i)
        if code <= d:
            new += chr(code + 13)
        else:
            new += chr(code - 13)
    return new

n = ''
for i in range(ord('A'), ord('Z')+1): # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    n += chr(i)
print(n)
print(rot(n))
print(rot('A'))
print(rot('J'))
'''

# Zadanie 9
'''
def cezar_znak(znak,klucz):
    litery = 'abcdefghijklmnopqrstuvwxyz'
    indeks = (litery.index(znak) + klucz)%26
    return litery[indeks]

print(cezar_znak('a',3))
print(cezar_znak('a',4))
print(cezar_znak('y',4))
'''

# Zadanie 10
'''
def cezar_znak(znak, klucz):
    litery = 'abcdefghijklmnopqrstuvwxyz'
    indeks = (litery.index(znak) + klucz)%26
    return litery[indeks]

def cezar(tekst, klucz):
    nowy = ''
    for z in tekst:
        nowy += cezar_znak(z,klucz)
    return nowy
    
print(cezar('abc',3))
print(cezar('abc',4))
print(cezar('vwxyz',4))
'''       

# Zadanie 11
'''
def cezar_znak(znak, klucz):
    litery = 'abcdefghijklmnopqrstuvwxyz'
    indeks = (litery.index(znak) - klucz)%26
    return litery[indeks]

def deszyfruj(tekst, klucz):
    nowy = ''
    for z in tekst:
        nowy += cezar_znak(z,klucz)
    return nowy

print(deszyfruj('abc',3))
print(deszyfruj('vwxyz',4))
'''

# Zadanie 12
'''
def cezar_znak(znak, klucz):
    litery = 'abcdefghijklmnopqrstuvwxyz'
    indeks = (litery.index(znak) + klucz)%26
    return litery[indeks]

def cezar2(tekst, klucz1, klucz2):
    nowy = ''
    i = 0
    d = len(tekst)
    for i in range(1,d,2):
        nowy += cezar_znak(tekst[i-1],klucz1)
        nowy += cezar_znak(tekst[i],klucz2)
    if d%2==1:
        nowy += cezar_znak(tekst[-1],klucz1)   
    return nowy
    
print(cezar2('abcdef',3,2))
print(cezar2('abcdefh',3,2))
'''      

# Zadanie 13
'''
def cezar_znak(znak, klucz):
    litery = 'abcdefghijklmnopqrstuvwxyz'
    indeks = (litery.index(znak) + klucz)%26
    return litery[indeks]

def cezar(tekst, klucz):
    nowy = ''
    for z in tekst:
        nowy += cezar_znak(z,klucz)
    return nowy

def jaki(tekst_jawny, szyfrogram):
    k = (ord(szyfrogram[0]) - ord(tekst_jawny[0]))%26
    if cezar(tekst_jawny,k) != szyfrogram:
        return -1
    return k
    
print(jaki('abcd','fghi'))
print(jaki('wxy','abc'))
print(jaki('abc', 'fgi'))
'''

# Zadanie 14
'''
def szyfruj(tekst,k):
    d = len(tekst)
    if d%k != 0:
        ile = k - (d%k)
        tekst = (ile*'X') + tekst
    nowy = ''
    for i in range(0,d,k):
        nowy += tekst[i:i+k][::-1]
    return nowy

print(szyfruj('ABCDEFG',3))
print(szyfruj('ABCDEFGH',3))
print(szyfruj('ABCDEFGHI',3))
'''

# Zadanie 15
'''
def cezar_znak(znak, klucz):
    litery = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    indeks = (litery.index(znak) + klucz)%52
    return litery[indeks]

def cezar(tekst, klucz):
    nowy = ''
    for z in tekst:
        nowy += cezar_znak(z,klucz)
    return nowy

print(cezar('ABC',30))
print(cezar('xyz',5))
'''      

# Zadanie 16
'''
def cezar_znak(znak, klucz):
    LITERY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    litery = 'abcdefghijklmnopqrstuvwxyz'
    if znak in litery:
        indeks = (litery.index(znak) + klucz)%26
        return litery[indeks]
    else:
        indeks = (LITERY.index(znak) + klucz)%26
        return LITERY[indeks]
    
def cezar(tekst, klucz):
    nowy = ''
    for z in tekst:
        nowy += cezar_znak(z,klucz)
    return nowy

print(cezar('AbC',3))
print(cezar('xYz',5))
'''