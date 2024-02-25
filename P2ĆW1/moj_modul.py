import kalkulator
import konwersja
import statystyka
import geometryczne

def powitanie():
    print("Witaj w moim module!")

# Użycie modułu kalkulator
print("dodawanie:", kalkulator.dodawanie(5, 3))
print("odejmowanie:", kalkulator.odejmowanie(10, 6))
print("mnożenie:", kalkulator.mnozenie(7, 8))
print("dzielenie:", kalkulator.dzielenie(20, 4))

# Użycie modułu konwersja
print("kilometry na mile:", konwersja.kilometry_na_mile(5))
print("cale na centymetry:", konwersja.cale_na_centymetry(10))
print("litry na galony:", konwersja.litry_na_galony(3))

# Użycie modułu statystyka
lista = [5, 10, 15, 20, 25]
print("średnia:", statystyka.srednia(lista))
print("mediana:", statystyka.mediana(lista))
print("wariancja:", statystyka.wariancja(lista))

# Użycie modułu geometryczne
print("pole prostokąta:", geometryczne.pole_prostokata(5, 3))
print("pole trójkąta:", geometryczne.pole_trojkata(10, 6))
print("pole koła:", geometryczne.pole_kola(7))
print("objętość sześcianu:", geometryczne.objetosc_szescianu(3))
print("objętość walca:", geometryczne.objetosc_walca(2, 4))
print("objętość stożka:", geometryczne.objetosc_stozka(3, 5))
