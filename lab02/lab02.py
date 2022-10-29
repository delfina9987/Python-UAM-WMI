# przykład
'''
a, b = input().split()
a = int(a)
b = int(b)
x = int(input())
if x < a:
    print(a - x)
elif b < x:
    print(x - b)
else:
    print("BINGO")
'''

# Zadanie 1
'''
A, B = input().split()
A = float(A)
B = float(B)
iloraz = A/B
print(format(iloraz, ".4f"))
'''

#Zadanie 2
'''
heads, legs = input().split()
heads, legs = int(heads), int(legs)

#dogs + ducks = heads
#4dogs + 2ducks = legs
# rozwiązanie równania
#dogs = (legs - 2 * heads)/2
#ducks = heads - dogs

#dogs = (legs - 2 * heads)/2
#ducks = heads - dogs

ducks = -(legs/2) + 2*heads
dogs = heads - ducks

print('Psy:')
print(format(dogs, ".1f"))
print('Kaczki:')
print(format(ducks, ".1f"))
'''

# Zadanie 3
'''
p,n,m = input().split()
p = int(p)
n = int(n)
m = int(m)
tmp = n-m
x = tmp/p
print(format(x, ".1f"))
'''

# Zadanie 4
'''
liczba_monet, suma_pieniedzy = input().split()
liczba_monet, suma_pieniedzy = int(liczba_monet), int(suma_pieniedzy)

monety_pieciozlotowe = (suma_pieniedzy - 2*liczba_monet)/3
monety_dwuzlotowe = liczba_monet - monety_pieciozlotowe

print('monety dwuzlotowe: ', monety_dwuzlotowe)
print('monety pieciozlotowe: ', monety_pieciozlotowe)
'''

# Zadanie 5
'''
liczba_rzedow_na_parterze, liczba_krzesel_w_rzedzie, liczba_miejsc_na_balkonie, liczba_osob = input().split()
liczba_rzedow_na_parterze, liczba_krzesel_w_rzedzie, liczba_miejsc_na_balkonie, liczba_osob = int(liczba_rzedow_na_parterze), int(liczba_krzesel_w_rzedzie), int(liczba_miejsc_na_balkonie), int(liczba_osob)

wszystkie_miejsca = (liczba_rzedow_na_parterze * liczba_krzesel_w_rzedzie) + liczba_miejsc_na_balkonie
wolne_miejsca = wszystkie_miejsca - liczba_osob

print(wolne_miejsca)
'''

# Zadanie 6 // wychodzi ujemna liczba, kiedy się wszystko od siebie odejmie!
#lczb_fig_dal, lczb_pies_czarny_prawe_ucho, lczb_pies_czarny_lewe_ucho, lczb_pies_białe_uszy = input().split()
#lczb_fig_dal, lczb_pies_czarny_prawe_ucho, lczb_pies_czarny_lewe_ucho, lczb_pies_białe_uszy = int(lczb_fig_dal), int(lczb_pies_czarny_prawe_ucho), int(lczb_pies_czarny_lewe_ucho), int(lczb_pies_białe_uszy)

# Zadanie 7 - nie wiem jak matematycznie to rozwiązać!

# Zadanie 8
'''
a, b = input().split()
a, b = int(a), int(b)
if a > b:
    print('większa liczba to:', a)
elif a < b:
    print('większa liczba to:', b)
else:
    print('liczby są równe')
'''

# Zadanie 9
'''
a, b = input().split()
a, b = int(a), int(b)
if a > b:
    print('A > B')
elif a < b:
    print('A < B')
else:
    print('A == B')
'''

# Zadanie 10
'''
liczba = int(input())

if liczba > 0:
    print('+')
elif liczba < 0:
    print('-')
else:
    print('0')
'''

# Zadanie 11
'''
a, b = input().split()
c = input()
a, b, c = int(a), int(b), int(c)
if c < a:
    print(a-c)
elif c > b:
    print(c-b)
else:
    print('BINGO')
'''

# Zadanie 12
'''
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a + b > c and b + c > a and a + c > b:
    print('TAK')
else:
    print('NIE')
'''

# Zadanie 13
# a+c=b+d     warunek wpisania okręgu w czworokąt
'''
a, b, c, d = input().split()
a, b, c, d = float(a), float(b), float(c), float(d)

if a + c == b + d:
    print('TAK')
else:
    print('NIE')
'''

# Zadanie 14
'''
a, b = input().split()
a, b = int(a), int(b)

if b % a == 0:
    print('TAK')
else:
    print('NIE')
'''

# Zadanie 15 - DO ZROBIENIA!

# Zadanie 16
'''
a,b = input().split()
a,b = float(a), float(b)

if b == 0:
    print('Nie można dzielić przez 0!')
else:
    print(format(a/b, ".2f"))
'''

# Zadanie 17
'''
a = int(input())
if a%2 == 0:
    print(a%3)
else:
    print(a%5)
'''

# Zadanie 18
'''
a = int(input())
if a%6 == 0 and not a%4 == 0:
    print('TAK')
else:
    print('NIE')
'''

# Zadanie 19
'''
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if a <= b <= c:
    print('TAK')
else:
    print('NIE')
'''

# Zadanie 20
'''
wyraz1, wyraz2, wyraz3 = input().split()
wyraz1, wyraz2, wyraz3 = str(wyraz1), str(wyraz2), str(wyraz3)

wyrazy = [wyraz1, wyraz2, wyraz3]

ilosc1 = wyrazy.count(wyraz1)
ilosc2 = wyrazy.count(wyraz2)
ilosc3 = wyrazy.count(wyraz3)

if wyraz1 != wyraz2 and wyraz1 != wyraz3 and wyraz2 != wyraz3:
    print(wyraz1, ilosc1, wyraz2, ilosc2, wyraz3, ilosc3)
elif wyraz1 == wyraz2 and wyraz1 != wyraz3 and wyraz2 != wyraz3:
    print(wyraz1, ilosc1, wyraz3, ilosc3)
elif wyraz1 == wyraz3 and wyraz1 != wyraz2 and wyraz3 != wyraz2:
    print(wyraz1, ilosc1, wyraz2, ilosc2)
elif wyraz2 == wyraz3 and wyraz2 != wyraz1 and wyraz3 != wyraz1:
    print(wyraz2, ilosc2, wyraz1, ilosc1)
elif wyraz1 == wyraz2 and wyraz1 == wyraz3 and wyraz2 == wyraz3:
    print(wyraz1, ilosc1)
'''

# Zadanie 21
'''
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
numbers = [a, b, c]
print(sorted(numbers))
'''

# Zadanie 22 // zrobione inaczej
'''
a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
result = abs(a-b) + abs(b-c) + abs(c-d)
print(result)
'''

# Zadanie 23
'''
a, b = input().split()
a, b = int(a), int(b)

suma = a+b
reszta = suma%10

if reszta%3 == 0:
    print('TAK')
else:
    print('NIE')
'''

# Zadanie 24
'''
year = int(input())

if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print('TAK')
else:
    print('NIE')
'''

# Zadanie 25
'''
year1, month1, day1 = input().split()
year1, month1, day1 = int(year1), int(month1), int(day1)
year2, month2, day2 = input().split()
year2, month2, day2 = int(year2), int(month2), int(day2)

if year1 == year2:
    if month1 == month2:
        if day1 == day2:
            print('Daty są równe')
        elif day1 < day2:
            print(year1, month1, day1)
        else:
            print(year2, month2, day2)
    elif month1 < month2:
        print(year1, month1, day1)
    else:
        print(year2, month2, day2)
elif year1 < year2:
    print(year1, month1, day1)
else:
    print(year2, month2, day2)
'''

# Zadanie 26
#year1, month1, day1 = input().split()
#year1, month1, day1 = int(year1), int(month1), int(day1)
#year2, month2, day2 = input().split()
#year2, month2, day2 = int(year2), int(month2), int(day2)

#if year1-year2 == 18 and month1 == month2 and day1 == day2:
#    print('wszystkiego najlepszego') 
#elif year1-year2 >= 18:
#    print('TAK')
#else:
#    print('NIE')
