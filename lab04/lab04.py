# BRAKUJĄCE ZADANIA: 20,21,25

# przykład
'''
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
'''

# Zadanie 1
'''
sum = 0

while True:
    a = int(input())
    sum += a
    if a == 0:
        break
    else:
        continue

print('suma =', sum)
'''

# Zadanie 2
'''
countDod = 0
countUj = 0

while True:
    a = int(input())
    if a == 0:
        break
    elif a > 0:
        countDod += 1
    else:
        countUj += 1

print('Liczb ujemnych:', countUj)
print('Liczb dodatnich:', countDod)
'''

# Zadanie 3 
'''
largest_num = 0

while True:
    a = input()
    if a == 'KONIEC':
        break
    else:
        a = int(a)
        if a > largest_num:
            largest_num = a

print(largest_num)
'''

# Zadanie 4
'''
sum = 0
count = 0
a = 1

while a >= 0:
    a = float(input())
    sum += a
    count += 1

print(f"{sum/count:.3f}")
'''

# Zadanie 5 
'''
sum = 0
count = 0

while True:
    a = int(input())
    if a >= -99 and a <= 99:
        sum += a
        count += 1
        #print(sum)
        if sum > 123:
            print(f'Suma liczb wynosi {sum}, a liczba składników to {count}')
            break
    else:
        continue
'''

# Zadanie 6
'''
n = int(input())
ile_cyfr = 0

if n == 0: ile_cyfr = 1
m = n
while n > 0:
    cyfra_jednosci = n%10
    n = (n-cyfra_jednosci) // 10
    ile_cyfr += 1

print(f"Liczba {m} składa się z {ile_cyfr} cyfr.")

#s = input()
#print(len(s))
'''

# Zadanie 7
# pierwszy sposób
'''
n = int(input())
ostatnia = n%10

while n > 0:
    cyfra = n%10
    n = (n - cyfra) // 10

if ostatnia == cyfra:
    print('TAK')
else:
    print('NIE')
'''
#napis = '1234'
#print(napis[0])
#print(napis[-1])
#if napis[0] == napis[-1]: print TAK, else print NIE

# Zadanie 8
'''
sum = 0
n = int(input())
m = n

while n > 0:
    cyfra = n%10
    #print(cyfra)
    #print(n)
    n = (n - cyfra) // 10
    sum += cyfra

print(f"Suma cyfr liczby {m} wynosi {sum}.")
'''

# Zadanie 9
'''
sum = 0
sum1 = 0

while True:
    a = int(input())
    if a == 0:
        break
    elif a > 0:
        #cyfra = a%10
        #print(cyfra)
        #a = (a - cyfra) // 10
        #print(a)
        #sum += cyfra
        #print(sum)
        sum += a
    else:
        continue

while sum > 0:
    cyfra = sum%10
    sum = (sum - cyfra) // 10
    sum1 += cyfra

print(f"Suma cyfr liczb dodatnich wynosi {sum1}")
'''

# Zadanie 10  niby działa
'''
lista = []
sum = 0

while True:
    a = input()
    if a == 'KONIEC':
        #print(lista)
        break
    else:
        a = int(a)
        if a > 0:
            # jezeli liczba jest dodatnia
            m = a
            while a > 0: # sprawdzamy cyfry tej liczby
                cyfra_ostatnia = a%10
                a = (a - cyfra_ostatnia) // 10
                sum += cyfra_ostatnia
            if sum == 11: # jeśli suma jest równa 11, wypisz ją
                #print(sum)
                lista.append(m)
            else: # jeśli nie, to kontynuuj
                sum = 0
                continue
        else:
            continue
print(lista)
'''

# Zadanie 11
'''
lista = []
sum = 0

while True:
    a = int(input())
    if a < 0:
        break
    else:
        if a >= 0:
            # jezeli liczba jest dodatnia
            m = a
            while a > 0: # sprawdzamy cyfry tej liczby
                cyfra_ostatnia = a%10
                a = (a - cyfra_ostatnia) // 10
                sum += cyfra_ostatnia
            if sum <= 30: # jeśli suma jest mniejsza lub równa 30, zapisz ją
                #print(sum)
                lista.append(m)
            else: # jeśli nie, to kontynuuj
                sum = 0
                continue
        else:
            continue
print(lista)
'''

# Zadanie 12
'''
sum = 0
countT = 0
countN = 0
lista = []

n = int(input())

while (n):
    cyfra_ostatnia = n%10
    lista.append(cyfra_ostatnia)
    n = (n - cyfra_ostatnia) // 10

lista.reverse()
#print(lista)

listaToCheck = sorted(lista)
#print(lista)
#print(listaToCheck)

if lista == listaToCheck:
    print('TAK')
else:
    print('NIE')
'''

# Zadanie 13
'''
lista = []
s = ""
n = int(input())

while n != 0: # dopóki liczba n jest rózna od zera
    cyfra_ostatnia = n%10
    lista.append(cyfra_ostatnia)
    n = (n - cyfra_ostatnia) // 10

for i in lista:
    s += str(i) # połącz znaki
print(s)
'''

# Zadanie 14 // co z 0 lub liczbą ujemną?
'''
n = int(input())
num = 2
pow = 1
lista = []

while n > 0:
    result = num**pow
    if result >= n:
        break
    else:
        lista.append(result)
        pow += 1   
#print(lista)
print(lista[-1])
'''

# Zadanie 15
'''
n = int(input())
result = ""

if n == 0:
    print(0)
while (n):
    result += str(n%2) 
    n = n//2
print(result[::-1])
'''
#s = "napis"
#print(s[::-1]) # sipan

# Zadanie 16
'''
n = int(input()) 
result = ""

if n == 0:
    print(0)
while (n):
    result += str(n%8) 
    n = n//8
print(result[::-1])
'''

# Zadanie 17
'''
d,n = input().split(',')
d,n = int(d), int(n)

if n == 0:
    nl = '0'
else:
    nl = ''

tab_c = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n > 0:
    c = n%d
    n = (n-c)//d
    nl = tab_c[c] + nl # tablica cyfr[index tej cyfry] + nowy znak doklejany łańcucha

print(nl)
'''

# Zadanie 18
'''
a,b = input().split(';')
a,b = int(a), int(b)

aa = a
bb = b

while bb > 0:
    aa,bb = bb,aa%bb
    nwd = aa

print(f'NWD({a},{b}) = {nwd}')
'''

# Zadanie 19
'''
a,b = input().split(',')
a,b = int(a), int(b)

aa = a
bb = b

while bb > 0:
    aa,bb = bb,aa%bb
    nwd = aa

nww = (a * b) // nwd

print(f'NWW({a},{b}) = {nww}')
'''

# Zadanie 18 oraz 19 jako funkcje:
'''
def nwd(a,b):
    while a != b:
        if a > b:
            a -= b
        else: 
            b -= a
    return a

def nww(a,b):
    nw = a*b // nwd(a,b)
    return nw

a,b = input().split(';')
a,b = int(a), int(b)

print(f"NWD({a}, {b}) = {nwd(a,b)}")
print(f"NWW({a}, {b}) = {nww(a,b)}")
'''

# Zadanie 20 POPRAWIĆ!!!
'''


while True:
    a = int(input())
    if a == 0:
        break
    else:
        a,a = a,a%a
        nwd = a 

print(nwd)
'''

# Zadanie 21 wtf

# Zadanie 22
'''
a,b = input().split(',')
a,b = int(a), int(b)

aa = a
bb = b

while bb > 0:
    aa,bb = bb,aa%bb
    nwd = aa

print(nwd)
'''

# Zadanie 23
'''
a,b = input().split(',')
a,b = int(a), int(b)
sum = a+b # suma obu grup

aa = a
bb = b

while bb > 0:
    aa,bb = bb,aa%bb
    nwd = aa

print(format(sum/nwd,".0f")) # sumę obu grup dzielimy przez nwd
'''

# Zadanie 24
'''
a,b = input().split(';')
a,b = int(a), int(b)

aa = a
bb = b

while bb > 0:
    aa,bb = bb,aa%bb
    nwd = aa

nww = (a * b) // nwd

print(nww)
'''

# Zadanie 25 | do zrobienia


# Zadanie 26
'''
from random import randint
los = randint(0,100)
num = -1
count = 0

while (los != num):
    count+=1
    print("Próba nr:", count)
    num = int(input())
    if los > num:
        print('Za mała')
    elif los < num:
        print('Za duza')
    else:
        print('Brawo!')
'''
