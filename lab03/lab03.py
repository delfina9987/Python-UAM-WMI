# przyklady
'''
for i in range(int(input())):
    print(i, end=' ')


for z in 'Ala ma kota':
    print(z.swapcase(), end=' ')
'''

# Zadanie 1
'''
sum = 0
for i in range(5):
    i = int(input())
    sum += i
print(sum)
'''

# Zadanie 2
'''
sum = 0
n = int(input())
for i in range(n):
    i = int(input())
    sum += i
print(sum)
'''

# Zadanie 3
'''
lista = []
for i in range(5):
    i = int(input())
    lista.append(i)
print(max(lista))
'''

# Zadanie 4
'''
lista = []
n = int(input())

if n < 1:
    print('Błędne dane')
else:
    for i in range(n):
        i = int(input())
        lista.append(i)
    print(min(lista))
'''

# Zadanie 5
'''
lista = []
iloczyn = 1
n = int(input())
for i in range(n):
    i = int(input())
    iloczyn *= i
print(iloczyn)
'''

# Zadanie 6
'''
a = input()
tab = input().split()

counter = 0
for n in tab:
    if n == a:
        counter += 1

if counter == 0:
    print('NIE')
else:
    print('TAK')
'''

# Zadanie 7
'''
counter = 0
a = input()
tab = input().split()

for n in tab:
    if n == a:
        counter += 1
print(counter)
'''

# Zadanie 8
'''
counter = 0
a = input()
tab = input().split()

for n in tab:
    for i in n:
        if i == a:
            counter += 1
print(counter)
'''

# Zadanie 9
'''
tab = input().split()

for n in tab:
    n = int(n)
    szescian = n**3
    print(szescian, end=' ')
'''

# Zadanie 10
'''
tab = input().split()

for n in tab:
    n = int(n)
    if n%2 == 0:
        print('P', end='')
    else:
        print('N', end='')
'''

# Zadanie 11
'''
num = 0
num_list = []
a,n = input().split(',')
a,n = int(a), int(n)

for i in range(0,n):
    num = num + a
    num_list.append(num)
    #print(str(num), end=' ')
print(num_list)
'''

# Zadanie 12
'''
n = int(input())

for i in range(1,n):
    if n%i == 0:
        print(str(i), end=', ')
print(n)
'''

# Zadanie 13
'''
sum = 0
a,b = input().split(',')
a,b = int(a), int(b)

if a > b:
    print('błędne dane, pierwsza liczba musi być mniejsze od drugiej!')
else:
    for i in range(a,b+1):
        #print(i)
        sum += i
    print(sum)
'''

# Zadanie 14
'''
n = int(input())
s = input()

for znak in s:
    print(znak*n)
'''

# Zadanie 15
'''
x,a,b = input().split()
a=int(a)
b=int(b)
x=int(x)

if a < b:
    for i in range(a,b+1):
        if i%x==0:
            print(i, end=' ')
else:
    for i in range(a,b-1,-1):
        if i%x==0:
            print(i, end=' ')
'''

# Zadanie 16
'''
lista = []
suma = 0
tab = input().split(',')

for i in tab:
    i = int(i)
    lista.append(i)

#print(lista[-1])

if(lista[-1] != 0):
    print('ostatnią liczbą musi być zero')
else:
    #print(lista)
    for i in lista:
        i = int(i)
        suma += i
    #print(suma)
    x = len(lista)-1
    print(format(suma/x, '.3f'))
'''
 
# Zadanie 17
'''
lista = []
count = 0
tab = input().split(';')

for i in tab:
    i = int(i)
    lista.append(i)

largest_num = lista[0]

for num in lista:
    if num >= largest_num:
        largest_num = num

for num2 in lista:
    if num2 >= largest_num:
        count += 1

#print(largest_num)
print(count)
'''

# Zadanie 18
'''
a,b = input().split()
pn = input()
a,b = int(a), int(b)

for i in range(a,b+1):
    if pn == 'p':
        if i%2 == 0:
            print(i, end=',')
    elif pn == 'n':
        if i%2 != 0:
            print(i, end=',')
    else:
        print('proszę wprowadzić p lub n')
'''

# Zadanie 19
'''
sum = 0
a,b = input().split(',')
a,b = int(a), int(b)

for i in range(a,b):
    if i%2 != 0:
        sum += i
print(sum)
'''

# Zadanie 20
'''
sum = 0
pow = 0
a,b = input().split(';')
a,b = int(a), int(b)

for i in range(a,b+1):
    pow = i**3
    sum += pow
print(sum)
'''

# Zadanie 21
'''
znak = input()

for i in range(6):
    for j in range(9):
        print(znak, end=' ')
    print()
'''

# Zadanie 22
'''
znak, ilosc = input().split()
ilosc = int(ilosc)

for i in range(ilosc):
    for j in range(ilosc):
        print(znak, end=' ')
    print()
'''

# Zadanie 23
'''
znak, a, b = input().split()
a,b = int(a), int(b)

for i in range(a):
    for j in range(b):
        print(znak, end=' ')
    print()
'''

# Zadanie 24
'''
a, b = input().split(',')
a = int(a)
b = int(b)

dane = input().split(';')

wynik = 0

for x in dane:
    x = int(x)
    if x < a:
        wynik += a-x
    elif x > b:
        wynik += x-b
    else:
        wynik = 0

print(wynik)
'''

# Zadanie 25
'''
sum = 0
lista = []
n = input().split(',')

for i in n:
    lista.append(i)
#print(lista)

lista.remove(max(lista))
lista.remove(min(lista))
#print(lista)

for j in lista:
    j = float(j)
    sum += j
print(format(sum/len(lista), ".2f"))
'''

# Zadanie 26
'''
for i in range(0,1):
    print('@' * 9)
for i in range(0,1):
    print(' ' + '@' * 7 + ' ')
for i in range(0,1):
    print(' ' * 2 + '@' * 5 + ' ' * 2)
for i in range(0,1):
    print(' ' * 3 + '@' * 3 + ' ' * 3)
for i in range(0,1):
    print(' ' * 4 + '@' + ' ' * 4)
'''

'''
for i in range(0,4):
    print('@' * 2)
for i in range(0,2):
    print('@' * 6)
'''

'''
for i in range(0,1):
    print('@' * 6)
for i in range(0,5):
    print(' ' * 2 + '@' * 2 + ' ' * 2)
'''

'''
for i in range(0,1):
    print('@' * 7)
for i in range(0,1):
    print(' ' + '@' * 5 + ' ')
for i in range(0,1):
    print(' ' * 2 + '@' * 3 + ' ' * 2)
for i in range(0,1):
    print(' ' * 3 + '@' + ' ' * 3)
for i in range(0,1):
    print(' ' * 3 + '@' + ' ' * 3)
for i in range(0,1):
    print(' ' * 2 + '@' * 3 + ' ' * 2)
for i in range(0,1):
    print(' ' + '@' * 5 + ' ')
for i in range(0,1):
    print('@' * 7)
'''

# Zadanie 26 inaczej
'''
for i in range(5):
    print(i*' ', '@'*(9 - 2*i), sep='')

print()

for i in range(4):
    print(2*'@')
for i in range(2):
    print(6*'@')

print()

print(6*'@')
for i in range(5):
    print('  @@')

print()

for i in range(4):
    print(i*' ', '@'*(7 - 2*i), sep='')
for i in range(3, -1, -1):
    print(i*' ', '@'*(7 - 2*i), sep='')
'''
