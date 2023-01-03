# Zadanie 1
'''
class Prostokat:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Prostokąt o bokach a={self.a} b={self.b}"

    def pole(self):
        p = self.a * self.b
        return f'Pole = {p}'

    def obwod(self):
        obw = self.a*2 + self.b*2
        return f'Obwód = {obw}'
 
    def wypisz(self):
        print("Hej, to ja prostokąt!")

class Kwadrat(Prostokat):

    def __init__(self, a):
        Prostokat.__init__(self, a, a)

    def wypisz(self):
        Prostokat.wypisz(self)
        print("Jestem kwadratem!")

    def __repr__(self):
        return f'Kwadrat o boku a={self.a}'

    def rysuj(self):
        for i in range(self.a):
            print('* ' * self.a)


tmp = Prostokat(4,10)

print(tmp) # metoda __str__
print([tmp]) # metoda _repr__
print(tmp.pole()) # metoda pole
print(tmp.obwod()) # metoda obwod
tmp.wypisz() # metoda wypisz

print()

tmp1 = Kwadrat(6)
print(tmp1) # metoda _repr__
tmp1.wypisz() # metoda wypisz
print(tmp1.pole()) # metoda pole
print(tmp1.obwod()) # metoda obwod
tmp1.rysuj() # metoda rysuj
'''

# Zadanie 2
'''
class Osoba:

    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f'Hej, jestem {self.imie} {self.nazwisko} i mam {self.wiek} lat')

    def urodziny(self):
        w = self.wiek
        self.wiek = self.wiek + 1
        return w

    def __repr__(self):
        return '{} {}'.format(self.imie, self.nazwisko)

class Student(Osoba):

    def __init__(self, imie, nazwisko, wiek, rok=1):
        super().__init__(imie, nazwisko, wiek)
        self.rok = rok

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'Wiek = {self.wiek}, rok = {self.rok}')

    def __repr__(self):
        x = super().__repr__()
        x += f', rok = {self.rok}'
        return x

    def kolejny_rok(self):
        self.rok += 1


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, wiek, ile, zawod):
        Osoba.__init__(self, imie, nazwisko, wiek)
        self.ile = ile
        self.zawod = zawod

    def przedstaw_sie(self):
        Osoba.przedstaw_sie(self)
        print(f'Zarabiam {self.ile} zł')

    def __repr__(self):
        return f'{self.imie} zarabia {self.ile}'

    def podwyzka(self, n):
        przed = self.ile
        self.ile = self.ile*(1+n*.01)
        return przed

class Nauczyciel(Pracownik):

    def __init__(self, imie, nazwisko, wiek, ile, przedmioty=None):
        super().__init__(imie, nazwisko, wiek, ile, 'naczyciel')
        if przedmioty == None:
            przedmioty = []
        else:
            self.przedmioty = przedmioty

    def przedstaw_sie(self):
        Osoba.przedstaw_sie(self)
        print('Mogę uczyć:', *self.przedmioty)

    def __repr__(self):
        x = super().__repr__()
        x += ' i jest naczycielem.'
        return x
    
    def nowy_przedmiot(self, przedm):
        self.przedmioty.append(przedm)
        self.podwyzka(5)


tmpOsoba = Osoba('Dean', 'Winchester', 48)
print(tmpOsoba.przedstaw_sie())
print(tmpOsoba.urodziny())
print(tmpOsoba)
print()
tmpStudent = Student('Sam', 'Winchester', 44, 2)
print(tmpStudent)
tmpStudent.przedstaw_sie()
tmpStudent.urodziny()
tmpStudent.kolejny_rok()
print(tmpStudent)
print()
tmpPracownik = Pracownik('Crowley', 'King', 57, 20000, 'Demon')
print(tmpPracownik)
tmpPracownik.przedstaw_sie()
tmpPracownik.podwyzka(10)
tmpPracownik.urodziny()
print(tmpPracownik)
print()
tmpNauczyciel = Nauczyciel('Castiel', 'Winchester', 42, 10000, ['historia', 'biologia'])
print(tmpNauczyciel)
tmpNauczyciel.przedstaw_sie()
tmpNauczyciel.nowy_przedmiot('teoria sztuki')
print(tmpNauczyciel)
tmpNauczyciel.przedstaw_sie()
'''

# Zadanie 3
'''
class Zespolona:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def modul(self):
        return (self.x**2 + self.y**2) ** .5

    def __repr__(self):
        return f'{self.x} + {self.y} i '

    def dodaj(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Zespolona(x,y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Zespolona(x,y)

    def razy_skalar(self, sk):
        x = self.x * sk
        y = self.y * sk
        return Zespolona(x,y)

    def __mull__(self, sk):
        x = self.x * sk
        y = self.y * sk
        return Zespolona(x,y)

    def __rmul__(self, sk):
        x = self.x * sk
        y = self.y * sk
        return Zespolona(x,y)

class Rzeczywista(Zespolona):

    def __init__(self, x):
        Zespolona.__init__(self, x, 0)

    def __repr__(self):
        return str(self.x)

    def dodaj(self, other):
        return self.x + other

    def __add__(self, other):
        return self.x + other

    def __radd__(self, other):
        return self.x + other

    def reszta(self, m):
        return self.x % m


z1 = Zespolona(5,12)
print('z1 =', z1)
print("|z1| =", z1.modul())
z2 = Zespolona(3,4)
print('z2 =', z2)
print('z1.dodaj(z2) =', z1.dodaj(z2))
print("z1 + z2 =", z1 + z2)
#print('z1 * 10 =', z1 * 10)
print('10 * z2 =', 10 * z2)
print('z2.razy_skalar(100) =', z2.razy_skalar(100))
r1 = Rzeczywista(-8)
print('r1 =', r1)
print('|r1| =', r1.modul())
print('r1.dodaj(10) =', r1.dodaj(10))
print('r1 + 3 =', r1 + 3)
print('4 + r1 =', 4 + r1)
print('r1.razy_skalar(10) =', r1.razy_skalar(10))
#print('r1 * 100 = ', r1 * 100)
print('100 * r1 = ', 100 * r1)
print('r1.reszta(3) = ', r1.reszta(3))
'''

# Zadanie 4
'''
class Prostopadloscian:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b 
        self.c = c

    def __repr__(self):
        return f'Prostopadłościan o bokach {self.a}, {self.b} i {self.c}'

    def pole(self):
        p = 2 * (self.a * self.b + self.a * self.c + self.b * self.c)
        return p

    def objetosc(self):
        obj = self.a * self.b * self.c
        return obj
 
    def wypisz(self):
        print(f'Prostopadłościan ma objętość równą {self.objetosc()} oraz pole równe {self.pole()}')

class Szescian(Prostopadloscian):

    def __init__(self,a):
        super().__init__(a,a,a)

    def __repr__(self):
        return f'Sześcian o krawędzi {self.a}'

    def wypisz(self):
        super().wypisz()
        print('I jestem sześcianem.')

    def suma_krawedzi(self):
        return self.a*12

p1 = Prostopadloscian(3,4,5)
print(p1)
print("pole =", p1.pole())
print("objetosc =", p1.objetosc())
p1.wypisz()

s1 = Szescian(8)
print(s1)
s1.wypisz()
print("pole =", s1.pole())
print("objetosc =", s1.objetosc())
print("suma długości krawędzi =", s1.suma_krawedzi())
'''

# Zadanie 5
'''
class Zwierzak:

    def __init__(self, imie, wiek, gatunek):
        self.imie = imie
        self.wiek = wiek
        self.gatunek = gatunek

    def __repr__(self):
        return '{}: {}'.format(self.__class__.__name__,self.__dict__)

    def urodziny(self):
        self.wiek += 1
        return self.wiek

    def przedstaw_sie(self):
        print("Czesc! Nazywam się {}, mam {} lat  i jestem {}.".format(
            self.imie, self.wiek, self.gatunek))

    def powiedz(self, tekst):
        print(self.imie, "mowi:", tekst)

class Pies(Zwierzak):

    def __init__(self, imie, wiek, rasa):
        Zwierzak.__init__(self, imie, wiek, "pies")
        self.rasa = rasa

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("Moja rasa to {}.".format(self.rasa))

    def powiedz(self, tekst= "Hau!"):
        Zwierzak.powiedz(self, tekst)

    def jedzenie(self):
        print ("Mniam!!!")


z = Zwierzak("Milka", 3, "krolik")
print(z)
z.urodziny()
z.przedstaw_sie()
z.powiedz("Za goraco!")

p = Pies("Idefix", 2, "pies")
print(p)
p.urodziny()
p.przedstaw_sie()
p.powiedz()
p.jedzenie()
'''