# Zadanie 1
'''
class Prostokat:
    #definicja klasy

    def __init__(self,a,b):
        self.a = a
        self.b = b 
        print('Utowrzenie prostokąta.')

    def __str__(self):
        return f'Prostokąt o bokach {self.a} i {self.b}.'

    def __repr__(self):
        return f'a = {self.a}, b = {self.b}'

    def pole(self):
        p = self.a * self.b
        pole = f'Pole = {p}'
        return pole

    def obwod(self):
        obw = self.a*2 + self.b*2
        return obw

    def rysuj(self):
        for i in range(self.a):
            print('* ' * self.b)
 
    def wypisz(self):
        print(f'Prostokąt ma obwód równy {self.obwod()}.')

tmp = Prostokat(4,10)

print(tmp) # metoda __str__
print([tmp]) # metoda _repr__
print(tmp.pole()) # metoda pole
print("Obwód =", tmp.obwod()) # metoda obwod
tmp.rysuj() # metoda rysuj
tmp.wypisz() # metoda wypisz
'''

# Zadanie 2
'''
class Kolo:
    def __init__(self,r):
        self.r = r
        print('Utowrzenie koła')

    def __str__(self):
        return f'Koło ma promień {self.r}'

    def __repr__(self):
        return f'promień = {self.r}'

    def pole(self):
        p = self.r * self.r * 3.14
        pole = f'Pole = {p}'
        return pole

    def obwod(self):
        obw = (self.r + self.r) * 3.14
        return obw
 
    def wypisz(self):
        print(f'Koło ma obwód równy {self.obwod()}')

tmp = Kolo(4)

print(tmp) # metoda __str__
print([tmp]) # metoda _repr__
print(tmp.pole()) # metoda pole
print("Obwód =", tmp.obwod()) # metoda obwod
tmp.wypisz() # metoda wypisz
'''

# Zadanie 3
'''
class Kwadrat:
    def __init__(self,a):
        self.a = a
        print('Utowrzenie kwadratu')

    def __str__(self):
        return f'Kwadrat ma bok o długości {self.a}'

    def __repr__(self):
        return f'długość boku = {self.a}'

    def pole(self):
        p = self.a * self.a
        pole = f'Pole = {p}'
        return pole

    def obwod(self):
        obw = self.a * 4
        return obw
    
    def rysuj(self):
        for i in range(self.a):
            print('* ' * self.a)
 
    def wypisz(self):
        print(f'Kwadrat ma obwód równy {self.obwod()}')

tmp = Kwadrat(6)

print(tmp) # metoda __str__
print([tmp]) # metoda _repr__
print(tmp.pole()) # metoda pole
print("Obwód =", tmp.obwod()) # metoda obwod
tmp.rysuj() # metoda rysuj
tmp.wypisz() # metoda wypisz
'''

# Zadanie 4
'''
class Prostopadloscian:
    #definicja klasy

    def __init__(self,a,b,c):
        self.a = a
        self.b = b 
        self.c = c
        print('Utowrzenie prostopadłościanu')

    def __str__(self):
        return f'Prostopadłościan o bokach {self.a}, {self.b} i {self.c}'

    def __repr__(self):
        return f'a = {self.a}, b = {self.b}, c = {self.c}'

    def pole(self):
        p = 2 * (self.a * self.b + self.a * self.c + self.b * self.c)
        pole = f'Pole = {p}'
        return pole

    def objetosc(self):
        obj = self.a * self.b * self.c
        return obj
 
    def wypisz(self):
        print(f'Prostopadłościan ma objętość równą {self.objetosc()} oraz {self.pole()}')

tmp = Prostopadloscian(3,4,5)

print(tmp) # metoda __str__
print([tmp]) # metoda _repr__
print(tmp.pole()) # metoda pole
print("Objętość =", tmp.objetosc()) # metoda objetosc
tmp.wypisz() # metoda wypisz
'''

# Zadanie 5
'''
class Szescian:
    def __init__(self,a):
        self.a = a
        print('Utowrzenie sześcianu')

    def __str__(self):
        return f'Sześcian ma bok o długości {self.a}'

    def __repr__(self):
        return f'długość boku = {self.a}'

    def pole(self):
        p = 6*self.a**2
        pole = f'Pole = {p}'
        return pole

    def objetosc(self):
        obj = self.a**3
        return obj
 
    def wypisz(self):
        print(f'Sześcian ma objętość równą {self.objetosc()} oraz {self.pole()}')

tmp = Szescian(3)

print(tmp) # metoda __str__
print([tmp]) # metoda _repr__
print(tmp.pole()) # metoda pole
print("Objętość =", tmp.objetosc()) # metoda objetosc
tmp.wypisz() # metoda wypisz
'''

# Zadanie 6
'''
class Punkt:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print('Utowrzenie punktu')

    def __str__(self):
        return f'Punkt o współrzędnych {self.x} oraz {self.y}'

    def __repr__(self):
        return f'współrzędne punktu x = {self.x} oraz y = {self.y}'

    def odleglosc(self):
        d = (self.x**2 + self.y**2)**.5
        return d
 
    def wypisz(self):
        print(f'To jest punkt {self.x}, {self.y}')

tmp = Punkt(-4,3)

print(tmp) # metoda __str__
print([tmp]) # metoda _repr__
print(tmp.odleglosc()) # metoda odleglosc
tmp.wypisz() # metoda wypisz
'''