# Zadanie 1
'''
def czy_doskonala(liczba):
    sum = 0
    for i in range(1,liczba):
        if liczba%i == 0:
            sum += i
    if sum == liczba:
        return True
    else:
        return False

print(czy_doskonala(6))
print(czy_doskonala(28))
print(czy_doskonala(7))
print(czy_doskonala(11))
'''

# Zadanie 2
'''
def czy_doskonala(liczba):
    sum = 0
    for i in range(1,liczba):
        if liczba%i == 0:
            sum += i
    if sum == liczba:
        return True
    else:
        return False

def wypisz_doskonale(n):
    lista = []
    for i in range(1,n):
        if czy_doskonala(i):
            lista.append(i)
    return lista

#print(wypisz_doskonale(30))
#print(wypisz_doskonale(100))
#print(wypisz_doskonale(500))
print(wypisz_doskonale(10000))
'''

# Zadanie 3
'''
def czy_doskonala(liczba):
    sum = 0
    for i in range(1,liczba):
        if liczba%i == 0:
            sum += i
    if sum == liczba:
        return True
    else:
        return False

lista = []
for i in range(100,1000):
    if czy_doskonala(i):
        lista.append(i)
print(*lista)
'''

# Zadanie 4
'''
def sumaDzielnikow(liczba):
    sum = 0
    for i in range(1,liczba):
        if liczba%i == 0:
            sum += i
    return sum

def zaprzy(a,b):
    if a == b:
        return False
    else:
        if sumaDzielnikow(a) == b and sumaDzielnikow(b) == a:
            return True
        else:
            return False

print(zaprzy(220,284))
print(zaprzy(6,6))
print(zaprzy(6,28))
'''

# Zadanie 5
'''
def sumaDzielnikow(liczba):
    sum = 0
    for i in range(1,liczba):
        if liczba%i == 0:
            sum += i
    return sum

def zaprzy(a,b):
    if a == b:
        return False
    else:
        if sumaDzielnikow(a) == b and sumaDzielnikow(b) == a:
            return True
        else:
            return False

def wypisz_zaprzy(n):
    for a in range(1,n):
        for b in range(a+1, n+1):
            if zaprzy(a,b):
                print(a,b)

wypisz_zaprzy(1000)
'''

# Zadanie 6
'''
def sumaDzielnikow(liczba):
    sum = 0
    for i in range(1,liczba):
        if liczba%i == 0:
            sum += i
    return sum

def k_doskonala(n,k):
    return abs(n - sumaDzielnikow(n)) == k

print(k_doskonala(10,2))
print(k_doskonala(6,0))
print(k_doskonala(11,4))
'''

# Zadanie 7
'''
def czy_pierwsza(liczba):
    liczba = int(liczba)
    if liczba < 2: return False
    n = int(liczba**.5)
    for d in range(2,n+1):
        if liczba%d ==0:
            return False
    return True

print(czy_pierwsza(1)) #false
print(czy_pierwsza(7)) #true
print(czy_pierwsza(36)) #false
print(czy_pierwsza(97)) #true
print(czy_pierwsza(2)) #true
print(czy_pierwsza(3)) #true
'''

# Zadanie 8
'''
def czy_pierwsza(liczba):
    liczba = int(liczba)
    if liczba < 2: return False
    n = int(liczba**.5)
    for d in range(2,n+1):
        if liczba%d ==0:
            return False
    return True

def pierwsza(n):
    counter = 0
    tmp = 1
    while counter < n:
        tmp += 1
        if czy_pierwsza(tmp):
            counter += 1
    return tmp

for i in range(1,11):
    print(pierwsza(i))
'''

# Zadanie 9
'''
def czy_pierwsza(liczba):
    liczba = int(liczba)
    if liczba < 2: return False
    n = int(liczba**.5)
    for d in range(2,n+1):
        if liczba%d ==0:
            return False
    return True

lista = []
for i in range(100,1000):
    if czy_pierwsza(i):
        lista.append(i)
print(*lista)
#tmp = len(lista)
#print(tmp)
'''

# Zadanie 10
'''
def czy_pierwsza(liczba):
    liczba = int(liczba)
    if liczba < 2: return False
    n = int(liczba**.5)
    for d in range(2,n+1):
        if liczba%d ==0:
            return False
    return True

def najwieksza(n):
    if n < 3:
        return -1
    while True:
        n -= 1
        if czy_pierwsza(n):
            return n

print(najwieksza(20))
print(najwieksza(13))
print(najwieksza(3))
print(najwieksza(2))
'''

# Zadanie 11
'''
def czy_pierwsza(liczba):
    liczba = int(liczba)
    if liczba < 2: return False
    n = int(liczba**.5)
    for d in range(2,n+1):
        if liczba%d ==0:
            return False
    return True

def dzielniki(n):
    lista = []
    for i in range(2,n+1):
        if n%i == 0 and czy_pierwsza(i):
            lista.append(i)
    return lista

print(dzielniki(1))
print(dzielniki(2))
print(dzielniki(11))
print(dzielniki(12))
print(dzielniki(1024))
print(dzielniki(15))
'''

# Zadanie 12
'''
def czy_pierwsza(liczba):
    liczba = int(liczba)
    if liczba < 2: return False
    n = int(liczba**.5)
    for d in range(2,n+1):
        if liczba%d ==0:
            return False
    return True

def blizniacze(n):
    licznik = 0
    a = 1
    b = 3
    while licznik < n:
        a += 2
        b += 2
        if czy_pierwsza(a) and czy_pierwsza(b):
            licznik += 1   
    return a,b

for i in range(1,11):
    print(blizniacze(i))
'''

# Zadanie 13
'''
def czy_pierwsza(liczba):
    liczba = int(liczba)
    if liczba < 2: return False
    n = int(liczba**.5)
    for d in range(2,n+1):
        if liczba%d ==0:
            return False
    return True

def sumaCyfr(n):
    n = int(n)
    suma = 0
    while n > 0:
        c = n%10
        suma += c
        n = (n-c)//10
    return suma

#def sumaCyfr2(n):
 #   n = str(n)
  #  suma = 0
   # for c in n:
    #    suma += int(c)
    #return suma

def super_pierwsza(n):
    if czy_pierwsza(n) == False:
        return False
    s = sumaCyfr(n)
    if czy_pierwsza(s):
        return True
    return False

print(super_pierwsza(2))
print(super_pierwsza(11))
print(super_pierwsza(101))
print(super_pierwsza(111))
print(super_pierwsza(17))
'''

# Zadanie 14
'''
def czy_pierwsza(liczba):
    liczba = int(liczba)
    if liczba < 2: return False
    n = int(liczba**.5)
    for d in range(2,n+1):
        if liczba%d ==0:
            return False
    return True

def czworacze(n):
    n += 1
    while True:
        if czy_pierwsza(n) and czy_pierwsza(n+2)and czy_pierwsza(n+6) and czy_pierwsza(n+8):
            return n
        n += 1

print(czworacze(2))
print(czworacze(5))
print(czworacze(10))
print(czworacze(50))
print(czworacze(100))
'''

# Zadanie 15
'''
def przedzial(n,m):
    lista = []
    tmp1 = n**2
    tmp2 = m**2
    for i in range(tmp1,tmp2+1):
        lista.append(i)
    return lista

print(przedzial(5,6))
'''

# Zadanie 16
'''
n = 10
while True:
    if n%5==1 and n%6==1 and n%7==1 and n%8==1 and n%9==1:
        print(n)
        break
    n += 1
'''

# Zadanie 17
'''
def collatz(number):
  lst=[]
  lst.append(number)
  while(number != 1):
      if(number%2 == 0):
          number = number//2
          lst.append(number)
      else:
          number = number*3+1
          lst.append(number)
  print(*lst)

collatz(10)
'''