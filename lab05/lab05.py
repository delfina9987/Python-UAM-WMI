# procedura coś robi, funkcja coś oblicza

# przykład
'''
def dodaj(a,b,c):
    return a+b+c
print(dodaj(2,3,4))
'''

'''
dod = lambda a, b: a + b
wypisz = lambda cos: print('Wypisalem:', cos)
kw = lambda x: x * x

print(dod(3,5))
wypisz('Olaf')
print(kw(5))
'''

# Zadanie 1
'''
def pokazZnak(znak):
    for i in range(1,11):
        print(i*znak)

#print(pokazZnak('@')) # na koniec będzie none
#pokazZnak('$')
print('Podaj znak:')
znak1 = input()
pokazZnak(znak1)
'''

# Zadanie 2
'''
def pokazZnak(znak, liczba):
    for i in range(liczba+1):
        print(i*znak)
    
#pokazZnak('$', 10) # tu zmieniamy wartość
print('Podaj znak, podaj liczbę:')
znak1, num1 = input().split(',')
num1 = int(num1)

pokazZnak(znak1, num1)
'''

# Zadanie 3
'''
def szescian(liczba):
    V = liczba**3
    return V

print('Podaj wartość:')
bok = szescian(int(input()))
print(bok)
'''

# Zadanie 4
'''
def pole(a,b,c):
    P=2*a*b + 2*a*c + 2*b*c
    return P

show = pole(2,4,5) # tu zmieniamy wartość
print(show)
'''

# Zadanie 5
'''
def kmh_ms(szyb):
    v = szyb/3.6
    return v

print('Podaj liczbę do przeliczenia na m/s:')
show = kmh_ms(int(input())) 
print(f"{show:.2f} m/s")

def ms_kmh(szyb):
    return szyb*3.6

print('Podaj liczbę do przeliczenia na km/h:')
show = ms_kmh(int(input()))
print(f"{show:.2f} km/h")
'''

# Zadanie 6
'''
def pogoda(temp):
    F = (temp-32)*(5/9)
    return F

print('Podaj temp w stopniach Fahrenheita:')
tempF = pogoda(int(input()))
print(f"{tempF:.2f}")
'''

# Zadanie 7
'''
def milimetry(p):
    mm = p*0.750063755419
    return mm

print('Podaj hPa (ciśnienie atmosferyczne):')
show = milimetry(int(input()))
print(f"{show:.3f} mm (milimetry słupa rtęci)")
'''

# Zadanie 8
'''
def wezel(szyb):
    km = 1.852 * szyb
    return km

print('Podaj liczbę węzłów do przeliczenia:')
show = wezel(int(input()))
print(f"{show:.3f} km/h")
'''

# Zadanie 9
'''
def czy_parzysta(liczba):
    if liczba%2 == 0:
        return True
    else:
        return False

print('Podaj liczbę:')
print(czy_parzysta(int(input())))
#print(czy_parzysta(5))
#print(czy_parzysta(8))
'''

# Zadanie 10
'''
def jak_szybko(t):
    v = 1320/t
    return v

print('Podaj czas przelotu:')
show = jak_szybko(float(input()))
print(f"{show:.2f}")
'''

# Zadanie 11
'''
def zamiana(m):
    km = m*1.609
    return km

print('Podaj odległość w milach:')
show = zamiana(float(input()))
print(f"Podana odległość, ale wyrazona w km: {show:.3f}")
'''

# Zadanie 12
'''
def hour(h,m):
    minutes = m+35
    if minutes > 59:
        minutes -= 60
        hour = (22 + h)%24
    else:
        hour = (21 + h)%24
    go = str(hour).rjust(2,'0')
    return f"{go}:{minutes:02d}"

h,m = input().split(':')
h,m = int(h),int(m)
print(hour(h,m))
'''

# Zadanie 13
'''
def godz_nj(g):
    nj = (g-6)%24
    return nj

g,m = input("Podaj czas w Warszawie (hh:mm): ").split(':')
g = int(g)
h = godz_nj(g)
print(f"{h:02d}:{m.rjust(2,'0')}")
'''

# Zadanie 14
'''
def suma_cyfr(liczba):
    sum = 0
    while liczba > 0:
        ostatnia_cyfra = liczba%10
        liczba = (liczba-ostatnia_cyfra)//10
        sum += ostatnia_cyfra
    return sum

print('Podaj liczbę:')
suma = suma_cyfr(int(input()))
print(f"Suma cyfr tej liczby wynosi {suma}")
'''

# Zadanie 15
'''
def samolot767(liczba1, liczba2):
    sum = 0
    biz = liczba1*4
    eko = liczba2*8
    sum = biz+eko
    return sum

print('Podaj ilość rzędów w klasie biznesowej oraz ilość rzędów w klasie eko:')
s1,s2 = input().split(',')
s1,s2 = int(s1), int(s2)
suma = samolot767(s1,s2)
print(f"Ilość miejsc w samolocie wynosi {suma}")
'''

# Zadanie 16
'''
def czy_podzielna3(liczba):
    if liczba%3 == 0:
        return True
    else:
        return False

print('Podaj liczbę:')
print(czy_podzielna3(int(input())))
'''

# Zadanie 17
'''
def kto(pesel):
    lista = []
    while pesel > 0:
        ostatnia_cyfra = pesel%10
        pesel = (pesel-ostatnia_cyfra)//10
        lista.append(ostatnia_cyfra)
    lista.reverse()
    #print(lista[9])
    if lista[9]%2 == 0:
        return 1
    else:
        return 2

print('Podaj pesel:')
show = kto(int(input()))
print(show)
'''

# Zadanie 18
'''
def zeroCount(tab):
    count = 0
    for n in tab:
        if n == 0:
            count += 1
    return count

def zeroCount2(tab):
    return tab.count(0)

tab = [7,0,55,4,9,0,3,2,0,0,0,4]
print(zeroCount(tab))
print(zeroCount2(tab))
'''

# Zadanie 19
'''
def pary6(lista):
    n = len(lista)
    count = 0
    for i in range(n-1):
        if lista[i] == lista[i+1] and lista[i] == 6:
            count += 1
    return count

tab = [1,6,6,6,4,3,6,6,4] # tu zmieniamy wartość
print(pary6(tab))
'''

# Zadanie 20
'''
def suma_dzielnikow(n):
    sum = 0
    for d in range(1,n):
        if n%d == 0:
            sum += d
    return(sum)

#print(suma_dzielnikow(1))
#print(suma_dzielnikow(2))
#print(suma_dzielnikow(11))
#print(suma_dzielnikow(25))
#print(suma_dzielnikow(12))

print('Podaj liczbę:')
print(suma_dzielnikow(int(input())))
'''

# Zadanie 21 oraz Zadanie 22
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

a,b = input().split(',')
a,b = int(a), int(b)

print(f"NWD({a}, {b}) = {nwd(a,b)}")
print(f"NWW({a}, {b}) = {nww(a,b)}")
'''

# Zadanie 23
'''
def suma(a,b, sum):
    return sum

sum = lambda a,b: a+b
#print(sum(3,5))
print('Podaj 2 liczby odzielone przecinkiem:')
a,b = input().split(',')
a,b = int(a), int(b)
show = sum(a,b)
print(f"Suma podanych liczb wynosi {show}")
'''

# Zadanie 24
'''
def suma(a,b,c, sum):
    return sum

sum = lambda a,b,c: a+b+c

print('Podaj 3 liczby odzielone przecinkiem:')
a,b,c = input().split(',')
a,b,c = int(a), int(b), int(c)
show = sum(a,b,c)
print(f"Suma podanych liczb wynosi {show}")
'''

# Zadanie 25
'''
def iloczyn(a,b, il):
    return il

il = lambda a,b: a*b

print('Podaj 2 liczby odzielone przecinkiem:')
a,b = input().split(',')
a,b = int(a), int(b)
show = il(a,b)
print(f"Iloczyn podanych liczby wynosi {show}")
'''

# Zadanie 26
'''
def higherNum(a,b,largestNum):
    if largestNum == a:
        return a
    else:
        return b

largestNum = lambda a,b: max(a,b)

#check = largestNum(7,5)
#print(check)

print('Podaj 2 liczby odzielone przecinkiem:')
a,b = input().split(',')
a,b = int(a), int(b)
show = largestNum(a,b)
print(show)
'''

# Zadanie 27
'''
def EvenOddNum(num, even):
    if even == 0:
        return True
    else:
        return False

even = lambda num: num%2==0

#print(even(4)) #True
#print(even(7)) #False
#print(even(1)) #False
#print(even(0)) #Truse

print('Podaj liczbę:')
print(even(int(input())))
'''

# Zadanie 27 inaczej
'''
czy_pa = lambda a: True if a%2 == 0 else False
czy_pa2 = lambda a: a%2 == 0

print(czy_pa(0), czy_pa2(0))
print(czy_pa(8), czy_pa2(8))
print(czy_pa(5), czy_pa2(5))
'''
