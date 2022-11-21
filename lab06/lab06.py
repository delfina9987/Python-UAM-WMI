# do zrobienia: 5-17

# Zadanie 1
'''
def pary(s):
    counter = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            counter += 1
    return counter

s = input("Podaj łańcuch: ")
print(pary(s))
'''
    
# Zadanie 2
'''
def ta(s):
    n = ''
    for i in s:
        if i in 'CGT':
            n += '*'
        else:
            n += i
    return n

s = input("Podaj łańcuch: ")
print(ta(s))
'''

# Zadanie 3
'''
def hamming(s,t):
    counter = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            counter += 1
    return counter

result = hamming('TATCA', 'CATTA')
print(f"\nOdległość Hamminga dla tych łańcuchów wynosi: {result}\n")
'''

# Zadanie 4
'''
name = input("Podaj miejscowość: ")
city = name[1::2]
print(*city)
'''

# Zadanie 5
'''
listColors = []

def get_max_str(lst):
    return max(lst, key=len)

for i in range(10):
    colors = input("Podaj nazwę koloru: ")
    listColors.append(colors)
print(get_max_str(listColors))
'''

# Zadanie 6
'''
letters = input().split()
for l in letters:
    print(l.swapcase(), end = '')
'''

# Zadanie 7
'''
tmp = input("Podaj łańcuch znaków: ")

for t in tmp:
    if t.isupper():
        print(t, end='')
'''

# Zadanie 8
'''
wzorzec = input("Podaj swój wzorzec: ")
counter = 0

wyraz = input("Podaj wyraz: ")
while wyraz != '***':
    if wyraz == wzorzec:
        counter += 1
    wyraz = input("Podaj wyraz: ")

print(counter)
'''

# Zadanie 9
'''
def ile_sam(s):
    counter = 0
    for z in s:
        if z in 'aeiouy':
            counter += 1
    return counter

s = input("Podaj łańcuch znaków: ")
print(f"Liczba samogłosek to: {ile_sam(s)}")
'''

# Zadanie 10
'''
def czy_metagram(s,t):
    ds = len(s)
    dt = len(t)
    if ds != dt:
        return False
    counter = 0
    for i in range(ds):
        if s[i] != t[i]:
            counter += 1
    if counter == 1:
        return True
    return False

s = input("Podaj pierwszy wyraz: ")
t = input("Podaj drugi wyraz: ")
print(czy_metagram(s,t))
'''   

# Zadanie 11
'''
def usun_sam(s):
    new = ''
    for z in s:
        if z in 'aeiouy':
            new += '_'
        else:
            new += z
    return new

s = input("Podaj łańcuch znaków: ")
print(f"Po usunięciu samogłosek: {usun_sam(s)}")
'''

# Zadanie 12
'''
def ile(tekst, wzorzec):
    dt = len(t)
    dw = len(w)
    counter = 0
    for i in range(dt-dw+1):      
        if tekst[i:i+dw] == wzorzec:
            counter += 1
    return counter

t = input("Podaj tekst: ")
w = input("Podaj wzorzec: ")
print(ile(t,w))
'''          
        
# Zadanie 13
'''
def gdzie(tekst, wzorzec):
    dt = len(t)
    dw = len(w)
    for i in range(dt-dw+1):      
        if tekst[i:i+dw] == wzorzec:
            return i+1
    return -1

t = input("Podaj tekst: ")
w = input("Podaj wzorzec: ")
print(gdzie(t,w)) 
'''

# Zadanie 14
'''
def compres(s):
    znak = s[0]
    count = 0
    new = ''
    for z in s:
        if z == znak:
            count += 1
        else:
            new += znak
            new += str(count)
            znak = z
            count = 1
    new += znak
    new += str(count)
    if len(new) > len(s):
        return s
    return new

s = input('Podaj łańcuch: ')
print(compres(s))
'''

# Zadanie 15
'''
for i in range(127800, 127901):
    print(chr(i), end = ' ')
'''

# Zadanie 16
'''
for i in range(32, 127):
    print(chr(i), end = ' ')
'''

# Zadanie 17
'''
p = ord('A')
k = ord('Z')
s = (p+k)//2 + 1

for i in range(p,s):
    print(chr(i), end=' ')
print()
for i in range(s,k+1):
    print(chr(i), end=' ')
'''